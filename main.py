import os
import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QTextEdit, QMessageBox,
    QFileDialog, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QMovie

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.media_player = QMediaPlayer()
        self.songs = []
        self.current_song_index = 0
        self.media_player.mediaStatusChanged.connect(self.handle_media_status)
        self.substitution_dict_upper = self.load_substitution_dict('CTabecedario')
        self.substitution_dict_lower = self.load_substitution_dict('CLabecedario')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Custom Encrypt/Decrypt App')
        self.setStyleSheet("background-color: #2A2A2A; color: #FFFFFF;")

        main_layout = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.text_area = QTextEdit(self)
        self.text_area.setStyleSheet("border: 2px solid white; color: #FFFFFF;")
        self.layout.addWidget(self.text_area)

        self.encode_btn = QPushButton('Encode', self)
        self.encode_btn.clicked.connect(self.encode)
        self.layout.addWidget(self.encode_btn)

        self.encrypted_area = QTextEdit(self)
        self.encrypted_area.setReadOnly(True)
        self.encrypted_area.setStyleSheet("border: 2px solid white; color: #FFFFFF;")
        self.layout.addWidget(self.encrypted_area)

        controls_layout = QHBoxLayout()

        self.layout.addLayout(controls_layout)

        self.save_btn = QPushButton('Save Encrypted Message', self)
        self.save_btn.clicked.connect(self.save_file)
        self.layout.addWidget(self.save_btn)

        self.load_btn = QPushButton('Load Encrypted File', self)
        self.load_btn.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_btn)

        self.decode_btn = QPushButton('Decode', self)
        self.decode_btn.clicked.connect(self.decode)
        self.layout.addWidget(self.decode_btn)

        self.gif_label = QLabel(self)
        self.movie = QMovie("")
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        main_layout.addLayout(self.layout)
        main_layout.addWidget(self.gif_label)

        self.setLayout(main_layout)

    def load_substitution_dict(self, folder):
        substitution_dict = {}
        for filename in os.listdir(folder):
            if filename.endswith('.txt'):
                char = filename[0]
                with open(os.path.join(folder, filename), 'r', encoding='utf-8') as file:
                    enc_string = file.read().strip()
                    substitution_dict[char] = enc_string
        return substitution_dict

    def encrypt_message(self, message):
        substitution_dict = self.substitution_dict_upper if message.isupper() else self.substitution_dict_lower
        return ''.join(substitution_dict.get(char, char) for char in message)

    def decrypt_message(self, encrypted_message):
        substitution_dict = self.substitution_dict_upper if encrypted_message.isupper() else self.substitution_dict_lower
        reverse_dict = {v: k for k, v in substitution_dict.items()}
        decrypted_message = []
        i = 0
        while i < len(encrypted_message):
            for enc_char in reverse_dict:
                if encrypted_message.startswith(enc_char, i):
                    decrypted_message.append(reverse_dict[enc_char])
                    i += len(enc_char)
                    break
            else:
                decrypted_message.append(encrypted_message[i])
                i += 1
        return ''.join(decrypted_message)

    def load_and_play_music(self):
        music_folder = "CHMusica"
        if not os.path.exists(music_folder):
            QMessageBox.warning(self, 'Error', 'La carpeta CHMusica no existe.')
            return

        self.songs = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]

        if self.songs:
            self.current_song_index = 0
            self.play_sound(self.songs[self.current_song_index])
        else:
            QMessageBox.warning(self, 'Error', 'No hay canciones en la carpeta CHMusica.')

    def play_sound(self, sound_file):
        if os.path.exists(sound_file):
            print(f"Reproduciendo: {sound_file}")
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(sound_file)))
            self.media_player.play()
            subprocess.Popen(['start', '', sound_file], shell=True)
        else:
            QMessageBox.warning(self, 'Error', f'El archivo {sound_file} no existe.')

    def play_previous_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index - 1) % len(self.songs)
            self.play_sound(self.songs[self.current_song_index])

    def play_next_song(self):
        if self.songs:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
            self.play_sound(self.songs[self.current_song_index])

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.play_next_song()

    def encode(self):
        message = self.text_area.toPlainText()
        if message:
            encrypted = self.encrypt_message(message)
            self.encrypted_area.setPlainText(encrypted)
            QMessageBox.information(self, 'Success', 'Message encrypted.')
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a message to encode.')

    def decode(self):
        encrypted_message = self.encrypted_area.toPlainText()
        if encrypted_message:
            decrypted = self.decrypt_message(encrypted_message)
            self.text_area.setPlainText(decrypted)
            QMessageBox.information(self, 'Success', 'Message decrypted.')
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter an encrypted message to decode.')

    def save_file(self):
        encrypted_message = self.encrypted_area.toPlainText()
        if encrypted_message:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Encrypted Message", "", "Text Files (*.txt);;All Files (*)", options=options)
            if file_name:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(encrypted_message)
                QMessageBox.information(self, 'Success', 'File saved successfully.')
        else:
            QMessageBox.warning(self, 'Warning', 'No message to save.')

    def load_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Encrypted File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                encrypted_message = file.read()
                self.encrypted_area.setPlainText(encrypted_message)
                QMessageBox.information(self, 'Success', 'File loaded successfully.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.resize(800, 400)
    ex.show()
    sys.exit(app.exec_())
