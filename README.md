# 🎮 Shift Hunter: Crack the Cipher, Challenge Your Brain

Welcome to **Shift Hunter**, a web-based puzzle game where your mission is to crack secret codes! This project is built using **Python** and **Streamlit**, combining classic cryptography with modern web interfaces for an engaging and educational experience.

---

## 📌 Project Overview

Shift Hunter is an interactive word puzzle game designed around the **Caesar Cipher**, one of the simplest and most widely known encryption techniques.

The primary objective of the game is to **decode encrypted messages (cipher texts)** by identifying the correct shift value used during the encryption process.

Whether you are a student learning cryptography, a puzzle enthusiast, or just someone looking for a quick brain teaser—**Shift Hunter** is the perfect game for you!

---

## 🎯 Gameplay Description

In **Mind Shift Mode**, the game presents the player with:

- An **encrypted word or phrase** (Cipher Text)
- **Category hints** (such as "Animal", "Fruit", etc.)
- **Length of the original word**

Your goal is to analyze the hint and decipher the correct word by mentally reversing the Caesar shift.

### 🧪 Example:

- **Encrypted Message:** `tqwv`
- **Category:** Animal
- **Length:** 4 letters

Your task: Crack the shift and figure out the original word! (Spoiler: It’s **“pony”**, if using a backward shift of 2.)

---

## 🏗️ Project Structure

The project follows a modular structure for clarity and scalability:

ShiftHunterProject/
├── app/
├── caesar_cipher/
├── requirements.txt
└── run.txt


---

## 🛠️ Technologies Used

- **Python 3.x** – Core programming language
- **Streamlit** – Rapid web application framework
- **Caesar Cipher Algorithm** – For message encryption/decryption
- **HTML/CSS (via Streamlit rendering)** – UI/UX presentation

---

## ✅ Features

- 🎮 **Interactive Gameplay:** Real-time web interface using Streamlit
- 🔐 **Custom Cipher Engine:** Fully implemented Caesar cipher logic
- 🧠 **Brain Training:** Encourages logical thinking and cryptanalysis skills
- 📱 **Responsive UI:** Runs directly in your browser
- 📚 **Educational Tool:** Great for teaching basic cryptography concepts
- 🏗️ **Modular Codebase:** Organized for easy maintenance and future updates


---

## 📸 Screenshot

![WhatsApp Image 2025-06-22 at 14 59 04_45dcce8b](https://github.com/user-attachments/assets/39fa84f0-5d28-4e11-bace-c3f7f21ccada) <!-- Replace with actual path when uploading -->

---

## 💻 Installation & Local Setup

Follow these simple steps to run Shift Hunter locally:

1. **Clone the Repository:**

```bash
git clone https://github.com/yourusername/ShiftHunter.git
cd ShiftHunterProject

```

2. **(Optional but Recommended) Create a Virtual Environment**

It is recommended to create a Python virtual environment to avoid dependency conflicts with other projects.

```bash
python -m venv venv

```

3. **Install Required Dependencies**

```bash

pip install -r requirements.txt

```

4. **Run the Streamlit App**

 ```bash

streamlit run app/Shift_Hunter.py

```

5. **Open the Application in Your Browser**

