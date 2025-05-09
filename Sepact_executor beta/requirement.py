import os
import subprocess
import sys

required_libraries = [
    "sqlite3",
    "shutil",
    "requests",
    "pyperclip",
    "tkinter",
    "datetime"
]

def install_libraries():
    for library in required_libraries:
        try:
            __import__(library)
            print(f"[INFO] {library} est deja installe.")
        except ImportError:
            if library not in ['sqlite3', 'shutil', 'tkinter', 'datetime']:
                print(f"[INFO] Installation de {library}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", library])
            else:
                print(f"[INFO] {library} fait partie de la bibliotheque standard, pas besoin de l'installer.")

def download_libraries():
    install_libraries()
    print("\nToutes les bibliotheques necessaires sont installees!")

if __name__ == "__main__":
    download_libraries()