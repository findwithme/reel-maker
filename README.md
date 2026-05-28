# Reel Maker

AI-powered Instagram Reel Generator and Uploader built with Python.

## Features

* Generate reel scripts automatically
* Create captions with hashtags
* Generate videos from scripts
* Upload reels directly to Instagram
* Simple GUI interface using Tkinter

---

# Installation

## 1. Download the Project

Download the ZIP file from GitHub and extract it.

Or clone the repository:

```bash
git clone https://github.com/findwithme/reel-maker.git
```

---

# Install Python

## 2. Install Python

Make sure Python 3.10 or above is installed.

Download Python from:

https://www.python.org/downloads/

---

# Install Ollama

## 3. Install Ollama

Download and install Ollama from:

https://ollama.com/

After installation, open terminal or command prompt and run:

```bash
ollama run llama3
```

This will download and start the AI model required for the project.

Important:

* Keep Ollama running before starting the project.
* The project will not work if Ollama is closed.

---

# Install Requirements

## 4. Install Required Packages

Open terminal or command prompt inside the project folder and run:

```bash
pip install -r requirements.txt
```

---

# Instagram Login Setup

## 5. Add Instagram Account

Open the `users.json` file and add your Instagram username and password.

Example:

```json
{
    "username": "your_instagram_username",
    "password": "your_instagram_password"
}
```

---

# Run the Project

## 6. Start the Application

Run:

```bash
python main.py
```

---

# Project Structure

```text
reel-maker/
│
├── main.py
├── requirements.txt
├── users.json
├── modules/
├── output/
└── assets/
```

---

# Notes

* Make sure your internet connection is active.
* Keep Ollama running while using the project.
* Instagram may ask for login verification on first login.
* Keep your credentials secure.
* Do not share your `users.json` file publicly.

---

# Technologies Used

* Python
* Tkinter
* MoviePy
* Instagrapi
* Ollama AI

---

# Disclaimer

This project is for educational purposes only. Use responsibly and follow Instagram's terms of service.

---

# Author

Developed by FindWithMe
