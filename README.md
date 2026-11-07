Supermarket Simulator — Universal Save Editor (Python Version)
Description / Descrição
A lightweight desktop tool built in Python with a graphical interface (Tkinter) designed to easily and safely edit your save files for Supermarket Simulator. It features automatic platform detection, supporting both Steam (.es3) and Xbox / PC Game Pass (Binary) versions, allowing you to modify your Money, Store Level, and Store Points without risking data corruption.

Prerequisites & Dependencies / Pré-requisitos e Dependências
To run or compile this script from the source code, you will need:

Python 3.x installed on your system.

The standard libraries used are tkinter, re, shutil, datetime, and pathlib (which come built-in with Python).

PyInstaller (only required if you want to compile the script into a standalone .exe).

How to Compile into an Executable (.exe) / Como Compilar para Executável
To compile the script into a clean Windows application while avoiding false-positive antivirus flags (by avoiding the --onefile temporary unpacking method), follow these steps:

Open your terminal (Command Prompt or PowerShell) and install PyInstaller:

Bash
pip install pyinstaller
Navigate to the folder where your SaveEditor.py script is saved:

Bash
cd path/to/your/script-folder
Compile the script using the --windowed flag (which hides the black command prompt window when the app opens):

Bash
pyinstaller --windowed SaveEditor.py
Once the process is finished, a new folder named dist will be created in your directory. Inside dist\SaveEditor\, you will find your clean, ready-to-use SaveEditor.exe along with its required runtime files.

Where to Find Your Save Files / Onde Encontrar Seus Saves
Steam:

Press Win + R, type %appdata%, go back one folder to LocalLow, and navigate to: NK Games\Supermarket Simulator (files end with .es3).

Xbox / PC Game Pass (Microsoft Store):

Press Win + R, type %localappdata%, go to Packages, look for the game's package folder, and navigate to LocalCache\Local\ where the binary save containers are stored.

How to Use / Como Usar
Run SaveEditor.exe.

Click "Open Save" and select your save file (the tool automatically detects if it's Steam or Xbox).

Type your desired values into the Money, Store Level, and Store Points boxes.

Click "Save Edited File".

Note: A secure timestamped backup (.backup) will automatically be saved in your Documents\Supermarket Simulator Backups folder before any modifications are applied.

Main Features / Principais Recursos
Universal Detection: Automatically recognizes Steam (.es3) and Xbox save structures.

Smart Byte Compensation: Adjusts internal structure spaces for Xbox binary saves to prevent corruption, and performs clean direct writing for Steam saves.

Auto-Reading: Instantly loads your current stats upon opening a file.

Automatic Secure Backup: Protects your progress by storing a backup copy in your Documents folder.

Shout Outs / Agradecimentos
Special thanks to the Supermarket Simulator modding community for their continuous feedback and support!
