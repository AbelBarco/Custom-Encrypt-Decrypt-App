
# 🔐 Custom Encrypt/Decrypt App

A desktop application built with **PyQt5** that allows users to **encrypt and decrypt messages** using a custom substitution system based on extensive character dictionaries.

---

## ✨ Features

* **Robust encryption:** Substitution system with ~100,000 characters per letter
* **Case sensitivity:** Uppercase and lowercase letters have **completely separate substitution tables**
* **Automatic decryption:** Recover original messages from encrypted text
* **Modern dark UI:** Intuitive and minimalist graphical interface
* **File management:** Save and load encrypted messages easily
* **Optional music player:** MP3 playback integration
* **High security:** Each character is replaced by a unique, long substitution string
* **Focused interface:** Clean design optimized for encryption/decryption tasks

---

## 📋 Requirements

* Python 3.7 or higher
* PyQt5
* Proper folder structure with character dictionaries

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/custom-encrypt-decrypt-app.git
cd custom-encrypt-decrypt-app
```

### 2. Install dependencies

```bash
pip install PyQt5
```

### 3. Required folder structure

```
project/
├── main.py
├── CTabecedario/          # Uppercase dictionary (~100k chars per letter)
│   ├── A.txt
│   ├── B.txt
│   └── ...
└── CLabecedario/          # Lowercase dictionary (~100k chars per letter)
    ├── a.txt
    ├── b.txt
    └── ...
```

### 4. Configure substitution dictionaries

Each `.txt` file must contain about **100,000 substitution characters**.

**Example**: `CTabecedario/A.txt`

```
@#$%^&*()[]{}|;:',.<>?/\~`!º«»ü+*÷×§¶†‡ˆ˜¡¿€£¥¢ƒ§¶†‡...
```

**Example**: `CLabecedario/a.txt`

```
♠♣♥♦©®™¤¢£€¥¦§¨ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅ...
```

> ⚠️ **Important:**
>
> * Each letter (A, B, C, etc.) in `CTabecedario` must have its own unique substitution sequence
> * Each lowercase equivalent (a, b, c, etc.) must have **completely different** sequences
> * No characters should overlap between uppercase and lowercase dictionaries

---

## 🖥️ Usage

### Run the application

```bash
python main.py
```

### Basic workflow

1. **Write a message:** Type your text in the upper text area
2. **Encrypt:** Click “Encode” to encrypt the message
3. **View result:** The encrypted message appears below
4. **Save:** Use “Save Encrypted Message” to store the result
5. **Load:** Use “Load Encrypted File” to reopen a saved message
6. **Decrypt:** Click “Decode” to recover the original text

---

## 🔒 How Encryption Works

### Encryption Process

1. The user enters a message
2. The app detects if characters are uppercase or lowercase
3. For each character:

   * It loads the corresponding file from `CTabecedario` or `CLabecedario`
   * Reads ~100,000 substitution characters
   * Replaces the character with the substitution string
4. The result is a much longer encrypted text
5. The encrypted message is displayed in the UI

### Decryption Process

1. The user pastes or loads an encrypted message
2. The app creates a reverse lookup dictionary (value → key)
3. It scans the message left-to-right
4. When a matching substitution string is found, it’s replaced with the original character
5. The original message is fully reconstructed

> ✅ Because every letter has a unique substitution set, decryption is **deterministic and unambiguous**.

---

## ⚠️ Security Considerations

* **File size:** Dictionaries will take up several MBs (~5.2 MB total for full set)
* **Performance:** Encryption/decryption remains instant, even for long texts
* **Confidentiality:** Keep substitution dictionaries **private**
* **Determinism:** Identical inputs always produce identical outputs (useful for integrity checking)

---

## 🧩 Main Class: `App`

### Core Methods

| Method                               | Description                                             |
| ------------------------------------ | ------------------------------------------------------- |
| `__init__()`                         | Initializes the app and loads substitution dictionaries |
| `initUI()`                           | Builds the graphical interface                          |
| `load_substitution_dict(folder)`     | Loads substitution files                                |
| `encrypt_message(message)`           | Encrypts text using dictionary mappings                 |
| `decrypt_message(encrypted_message)` | Decrypts text by reversing mappings                     |
| `encode()`                           | Handles encryption button click                         |
| `decode()`                           | Handles decryption button click                         |
| `save_file()`                        | Saves encrypted message to file                         |
| `load_file()`                        | Loads encrypted message from file                       |

---

## 💡 Example

```
Input: "Hola"

Dictionary:
H → [~100,000 chars for H]
o → [~100,000 chars for o]
l → [~100,000 chars for l]
a → [~100,000 chars for a]

Output: [~400,000-character encrypted string]
```

### Case-Sensitivity Example

```
Input: "Aa"

CTabecedario/A.txt: ©®™£¥€∆∑∏π...  
CLabecedario/a.txt: §¶†‡ˆ˜¡¿...  

Output: [200,000 completely unique characters]

Decryption: "Aa" ✅
```

> 🧠 Each case has an independent substitution table, making frequency analysis attacks practically impossible.

---

## 🎨 User Interface

* **Dark theme:** Gray background (#2A2A2A) with white text
* **Two text areas:** Input (top) and output (bottom)
* **Control panel:** Encode, Decode, Save, Load buttons
* **Animated GIF:** Decorative animation next to controls

---

## 🔧 Troubleshooting

| Issue                     | Solution                                                                         |
| ------------------------- | -------------------------------------------------------------------------------- |
| “No songs in CHMusica”    | Create the `CHMusica` folder in the project root                                 |
| “Dictionaries not loaded” | Ensure `CTabecedario` and `CLabecedario` exist with correctly named `.txt` files |
| Unrecognized characters   | Non-dictionary characters remain unchanged                                       |

---

## 🤝 Contributing

Contributions are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📄 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.

---

## ✍️ Author

**Abel Barco**

📧 Contact: [info@abelbarco.xyz](mailto:info@abelbarco.xyz)

---

> 🧩 *This project was developed for educational and demonstration purposes.*

---
