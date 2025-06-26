import streamlit as st

def display_encrypted_message(encrypted_message):
    st.markdown(f"<h3 style='color:#ff6f61;'>🔐 Encrypted Message: <code>{encrypted_message}</code></h3>", unsafe_allow_html=True)

def display_feedback(feedback):
    st.write(feedback)

def display_input_field():
    return st.text_input("Enter your guess for the shift key (1–25):")

def display_start_button():
    if st.button("🎲 Start New Game"):
        return True
    return False

def display_instructions():
    st.subheader("Instructions:")

    st.markdown("""
    ## 🎮 How the Game Works

    ### 🔸 Caesar Cipher Basics:

    A Caesar Cipher is a way to hide a message by **shifting** each letter **forward in the alphabet** by a number.

    For example:
    - A shift of `2` means:
        - `A` becomes `C`
        - `B` becomes `D`
        - `C` becomes `E`
    - This works using **modular arithmetic** — after `Z`, it wraps back to `A`.

    **Important:**  
    👉 The word “shift” here means changing letters, not pressing the **Shift key** on your keyboard.  
    ✅ When asked to enter a shift, just type a number (like `1`, `5`, etc.).

    ---

    ### 👨‍🏫 Step-by-Step Example:

    #### 👤 Player 1:
    - Enters the message: `hello`
    - Chooses a shift key: `2`

    #### 🔐 Game Encrypts It:
    It moves each letter forward in the alphabet:

    - `h` → `j`  
    - `e` → `g`  
    - `l` → `n`  
    - `l` → `n`  
    - `o` → `q`  

    ✅ So the encrypted message is: `jgnnq`

    ---

    #### 👤 Player 2 Sees:
    - Encrypted Message: `jgnnq`
    - (Hint: The word has 5 letters)

    #### 🧠 Player 2 Must:
    1. Guess the shift key:  
       👉 For example, try typing `2`

    2. Decode the message mentally or in writing.  
       👉 If their guess is correct, decoding `jgnnq` with shift `2` should give back `hello`.

    ---

    ### ✅ What You Should Do as a Player:

    - In 1 Player Mode:
      - Type a **number between 1 and 25** to guess the shift key.

    - In 2 Player Mode:
      - Player 1 enters a message and selects the shift.
      - Player 2 must guess the **number** and **write the original message**.

    🎯 You win if both are correct!
    """)
