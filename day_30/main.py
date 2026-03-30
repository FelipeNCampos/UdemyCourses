from pathlib import Path
from random import choice, randint, shuffle
from tkinter import Button, Canvas, END, Entry, Label, PhotoImage, Tk, messagebox
import json

try:
    import pyperclip
except ImportError:
    pyperclip = None


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"
LOGO_FILE = BASE_DIR / "logo.png"

window = None
website_entry = None
email_entry = None
password_entry = None


# ---------------------------- Data helpers ------------------------------- #
def searchFile():
    ensure_data_file()


def ensure_data_file(path=DATA_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("{}", encoding="utf-8")
        return

    try:
        with path.open("r", encoding="utf-8") as file:
            json.load(file)
    except (json.JSONDecodeError, OSError):
        path.write_text("{}", encoding="utf-8")


def load_data(path=DATA_FILE):
    ensure_data_file(path)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data, path=DATA_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def get_saved_credentials(website, path=DATA_FILE):
    website = (website or "").strip()
    if not website:
        return None

    data = load_data(path)
    return data.get(website)


def save_credentials(website, email, password, path=DATA_FILE):
    website = (website or "").strip()
    email = (email or "").strip()
    password = password or ""

    if not website or not password:
        raise ValueError("Website and password are required.")

    data = load_data(path)
    data[website] = {
        "email": email,
        "password": password,
    }
    save_data(data, path)
    return data[website]


# ---------------------------- Search ------------------------------- #
def search(website=None):
    if website is None and website_entry is not None:
        website = website_entry.get()

    website = (website or "").strip()
    if not website:
        if window is not None:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left website empty.")
        return None

    credentials = get_saved_credentials(website)
    if credentials is None:
        if window is not None:
            messagebox.showinfo(title="Error", message="Login not found.")
        return None

    if window is not None:
        messagebox.showinfo(
            title="Login",
            message=(
                f"Website = {website}\n"
                f"Email/Login = {credentials['email']}\n"
                f"Password = {credentials['password']}"
            ),
        )
    return credentials


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(target_entry=None, copy_to_clipboard=True):
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    entry = target_entry or password_entry
    if entry is not None:
        entry.delete(0, END)
        entry.insert(0, password)

    if copy_to_clipboard and pyperclip is not None:
        try:
            pyperclip.copy(password)
        except pyperclip.PyperclipException:
            pass

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(website=None, email=None, password=None):
    if website is None and website_entry is not None:
        website = website_entry.get()
    if email is None and email_entry is not None:
        email = email_entry.get()
    if password is None and password_entry is not None:
        password = password_entry.get()

    try:
        saved_credentials = save_credentials(website, email, password)
    except ValueError:
        if window is not None:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return None

    if website_entry is not None:
        website_entry.delete(0, END)
    if password_entry is not None:
        password_entry.delete(0, END)

    return saved_credentials


# ---------------------------- UI SETUP ------------------------------- #
def create_app():
    global window, website_entry, email_entry, password_entry

    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file=str(LOGO_FILE))
    canvas.create_image(100, 100, image=logo_img)
    canvas.image = logo_img
    canvas.grid(row=0, column=1)

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0)
    email_label = Label(text="Email/Username:")
    email_label.grid(row=2, column=0)
    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

    website_entry = Entry(width=35)
    website_entry.grid(row=1, column=1)
    website_entry.focus()

    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.insert(0, "angela@gmail.com")

    password_entry = Entry(width=21)
    password_entry.grid(row=3, column=1)

    generate_password_button = Button(text="Generate Password", command=generate_password)
    generate_password_button.grid(row=3, column=2)

    add_button = Button(text="Add", width=36, command=save)
    add_button.grid(row=4, column=1, columnspan=2)

    search_button = Button(text="Search", command=search)
    search_button.grid(row=1, column=2)

    return window


if __name__ == "__main__":
    create_app().mainloop()
