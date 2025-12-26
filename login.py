import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import json
import hashlib
import base64
import secrets

PROJECT_DIR = os.path.dirname(__file__)
CREDENTIALS_PATH = os.path.join(PROJECT_DIR, "credentials.json")


def _hash_password(password: str, salt: bytes | None = None, iterations: int = 200_000):
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return base64.b64encode(dk).decode("ascii"), base64.b64encode(salt).decode("ascii"), iterations


def _load_credentials() -> dict:
    if not os.path.exists(CREDENTIALS_PATH):
        return {}
    try:
        with open(CREDENTIALS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_credentials(data: dict) -> None:
    tmp = CREDENTIALS_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    try:
        os.replace(tmp, CREDENTIALS_PATH)
    except Exception:
        os.remove(tmp)


def create_user(username: str, password: str) -> None:
    data = _load_credentials()
    if username in data:
        raise ValueError("User already exists")
    pwd_hash, salt_b64, iterations = _hash_password(password)
    data[username] = {"hash": pwd_hash, "salt": salt_b64, "iterations": iterations}
    _save_credentials(data)


def verify_user(username: str, password: str) -> bool:
    data = _load_credentials()
    user = data.get(username)
    if not user:
        return False
    try:
        salt = base64.b64decode(user["salt"])
        iterations = int(user.get("iterations", 200_000))
        expected_hash = user["hash"]
        pwd_hash, _, _ = _hash_password(password, salt=salt, iterations=iterations)
        return secrets.compare_digest(pwd_hash, expected_hash)
    except Exception:
        return False


def has_any_user() -> bool:
    return bool(_load_credentials())


def launch_app():
    python_exec = sys.executable
    app_path = os.path.join(PROJECT_DIR, "first-desktop.py")
    try:
        subprocess.Popen([python_exec, app_path], cwd=PROJECT_DIR)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch app: {e}")


def on_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if verify_user(username, password):
        launch_app()
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def open_register():
    def do_register():
        u = reg_user.get().strip()
        p = reg_pass.get().strip()
        p2 = reg_pass2.get().strip()
        if not u or not p:
            messagebox.showwarning("Register", "Username and password cannot be empty.")
            return
        if p != p2:
            messagebox.showwarning("Register", "Passwords do not match.")
            return
        try:
            create_user(u, p)
        except ValueError:
            messagebox.showerror("Register", "User already exists.")
            return
        messagebox.showinfo("Register", "User created successfully. You may now log in.")
        reg_win.destroy()

    reg_win = tk.Toplevel(root)
    reg_win.title("Register")
    reg_win.resizable(False, False)
    frm = tk.Frame(reg_win, padx=12, pady=12)
    frm.pack()

    tk.Label(frm, text="Username:").grid(row=0, column=0, sticky="w")
    reg_user = tk.Entry(frm)
    reg_user.grid(row=0, column=1, pady=4)

    tk.Label(frm, text="Password:").grid(row=1, column=0, sticky="w")
    reg_pass = tk.Entry(frm, show="*")
    reg_pass.grid(row=1, column=1, pady=4)

    tk.Label(frm, text="Confirm:").grid(row=2, column=0, sticky="w")
    reg_pass2 = tk.Entry(frm, show="*")
    reg_pass2.grid(row=2, column=1, pady=4)

    tk.Button(frm, text="Create", command=do_register, width=10).grid(row=3, column=0, columnspan=2, pady=8)


root = tk.Tk()
root.title("Login")
root.geometry("340x200")
root.resizable(False, False)

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(expand=True, fill=tk.BOTH)

username_label = tk.Label(frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1, pady=6)

password_label = tk.Label(frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, pady=6)

login_button = tk.Button(frame, text="Login", width=10, command=on_login)
login_button.grid(row=2, column=0, pady=12)

register_button = tk.Button(frame, text="Register", width=10, command=open_register)
register_button.grid(row=2, column=1, pady=12)

# Allow pressing Enter to submit
root.bind('<Return>', lambda event: on_login())

if __name__ == '__main__':
    if not has_any_user():
        messagebox.showinfo("No users", "No users found — please create an account using Register.")
    root.mainloop()
