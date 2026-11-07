# Supermarket Simulator — Universal Save Editor

<p align="center">
  <b>A lightweight, cross-platform utility to edit Money, Store Level, and Store Points for Supermarket Simulator.</b>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-supported-versions">Supported Versions</a> •
  <a href="#-where-to-find-your-saves">Save Locations</a> •
  <a href="#-how-to-compile-from-source">Compilation Guide</a> •
  <a href="#-license">License</a>
</p>

---

## 🚀 Features

* **Universal Platform Detection:** Automatically recognizes and adapts to **Steam (`.es3`)** and **Xbox / PC Game Pass** save files.
* **Smart Byte Compensation:** For Xbox binary containers, it performs surgical byte adjustments to prevent structural corruption. For Steam, it performs clean, direct text replacement.
* **Auto-Reading:** Instantly loads and displays your current *Money*, *Store Level*, and *Store Points* upon opening a file.
* **Automatic Secure Backup:** Generates a timestamped backup (`.backup`) in your `Documents\Supermarket Simulator Backups` folder before modifying anything.
* **Modern Desktop Interface:** Built with native, lightweight GUI frameworks (available in Python/Tkinter or C++ Win32).

---

## 🎮 Supported Versions

| Platform | File Extension / Type | Editing Method |
| :--- | :--- | :--- |
| **Steam** | `.es3` (Plain Text / JSON) | Direct replacement |
| **Xbox / PC Game Pass** | Binary / Serialized Container | Surgical byte-size compensation |

---

## 📂 Where to Find Your Saves

Depending on your game version, your save files are located in these directories:

* **Steam:**
  1. Press `Win + R`, type `%appdata%` and hit Enter.
  2. Navigate back to **`LocalLow`** (or go directly to: `C:\Users\<YourUsername>\AppData\LocalLow\NK Games\Supermarket Simulator`).
  3. Look for files ending in **`.es3`**.

* **Xbox / PC Game Pass (Microsoft Store):**
  1. Press `Win + R`, type `%localappdata%` and hit Enter.
  2. Go to `Packages` and find the game's folder (starts with `NKGames.SupermarketSimulator...`).
  3. Navigate into `SystemAppData\wgs\000900000A390B88_000000000000000000000000657D9E7E` to find the binary save files.

---

## 🛠️ How to Compile from Source

### 1. Prerequisites
Make sure you have **Python 3.x** installed on your system along with its standard modules (`tkinter`, `pathlib`, `shutil`, `re`, `datetime`).

### 2. Install PyInstaller
Open your command prompt or PowerShell and install PyInstaller:
```bash
pip install pyinstaller
```
### 3 . Compile program
```bash
pyinstaller --onefile --windowed SaveEditor.py
