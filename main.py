import sys
import os
import subprocess

PROJECT_DIR = os.path.dirname(__file__)
APP_FILE = os.path.join(PROJECT_DIR, "first-desktop.py")

if __name__ == '__main__':
    if not os.path.exists(APP_FILE):
        print("Error: first-desktop.py not found in project root.")
        sys.exit(1)
    # Launch the GUI app using the same Python interpreter
    subprocess.run([sys.executable, APP_FILE], cwd=PROJECT_DIR)
