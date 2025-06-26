import streamlit as st
from game_functions import single_player_mode
from ui_functions import display_encrypted_message, display_input_field, display_start_button
from caesar_cipher.caesar import caesar
from PIL import Image
import os
import random

LOGO_PATH = os.path.join(os.path.dirname(__file__), "logo", "LOGO.png")
ASCII_IMAGE = os.path.join(os.path.dirname(__file__), "logo", "table1.jpg")

st.set_page_config(page_title="Shift Hunter", page_icon="🕹️", layout="centered")

# === Theme
st.markdown("""
<style>
body {
    background-color: #2C1C29;
    color: #FCECC9;
    font-family: 'Comic Sans MS', cursive;
}
h1, h2, h3 {
    color: #FFA94D;
}
.stButton>button {
    background-color: #FFA94D;
    color: #2C1C29;
    font-weight: bold;
    font-size: 18px;
    border-radius: 12px;
    padding: 10px 20px;
}
.stButton>button:hover {
    background-color: #FF7F50;
}
.stTextInput>div>input {
    background-color: #3D2C3E !important;
    color: #FCECC9 !important;
    border: 2px solid #FFA94D;
}
section[data-testid="stSidebar"] {
    background-color: #2C1C29;
    border-right: 2px solid #FFA94D;
    color: #FCECC9;
}
</style>
""", unsafe_allow_html=True)

# === Sidebar
with st.sidebar:
    try:
        st.image(Image.open(LOGO_PATH), width=230, caption="🔐 Shift Hunter")
    except:
        st.warning("⚠️ Logo not found")
    mode = st.radio("🎮 Choose Game Mode", ["🧠 Mind Shift", "🔓 Spin & Crack"], key="game_mode")
    if st.checkbox("🧮 Show Caesar ASCII Table"):
        try:
            st.image(ASCII_IMAGE, use_column_width=True)
        except Exception as e:
            st.error(f"Image load error: {e}")

# === Title
st.markdown("<h1 style='text-align: center;'>🎮 Shift Hunter</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Crack the Cipher. Challenge Your Brain.</h3>", unsafe_allow_html=True)
st.markdown("---")

# === GAME 1: Mind Shift
if mode == "🧠 Mind Shift":
    st.subheader("🧠 Mind Shift")
    with st.expander("📜 How to Play"):
        st.markdown("""
        You're shown an encrypted word. Guess the Caesar cipher key (1–25) to decode it.
        Example: hello (shift 2) → jgnnq
        """)

    if "encrypted_message" not in st.session_state:
        st.session_state.update({
            "encrypted_message": None,
            "shift_key": None,
            "original_message": None,
            "category": None,
            "attempts": 0,
            "solved": False
        })

    if display_start_button():
        encrypted_message, shift_key, original_message, category = single_player_mode()
        st.session_state.update({
            "encrypted_message": encrypted_message,
            "shift_key": shift_key,
            "original_message": original_message,
            "category": category,
            "attempts": 0,
            "solved": False
        })

    if st.session_state.encrypted_message and not st.session_state.solved:
        display_encrypted_message(st.session_state.encrypted_message)
        st.info(f"Length: {len(st.session_state.original_message)} | Category: {st.session_state.category}")
        guess = display_input_field()
        if guess:
            try:
                guess = int(guess)
                if guess == st.session_state.shift_key:
                    st.success("✅ Correct! You cracked it!")
                    decoded = caesar(st.session_state.encrypted_message, guess, "decode")
                    st.info(f"🔓 Original: `{decoded}`")
                    st.session_state.solved = True
                else:
                    st.session_state.attempts += 1
                    st.warning(f"❌ Incorrect. Attempt {st.session_state.attempts}/3")
                    if st.session_state.attempts >= 3:
                        decoded = caesar(st.session_state.encrypted_message, st.session_state.shift_key, "decode")
                        st.error("🚫 Out of attempts!")
                        st.info(f"🔑 Key: {st.session_state.shift_key}, Word: `{decoded}`")
                        st.session_state.solved = True
            except ValueError:
                st.warning("⚠️ Enter a valid number.")

    if st.session_state.encrypted_message and st.session_state.solved:
        if st.button("🔄 Try Another Word"):
            for k in ["encrypted_message", "shift_key", "original_message", "category", "attempts", "solved"]:
                st.session_state.pop(k, None)
            st.experimental_rerun()

# === GAME 2: Spin & Crack
elif mode == "🔓 Spin & Crack":
    st.subheader("🔓 Spin & Crack")
    with st.expander("📜 How to Play"):
        st.markdown("""
        Rotate letters using 🔼 or 🔽 to find the original word. You get 5 attempts.
        """)

    if "dial_word" not in st.session_state:
        words = [("hello", "greeting"), ("math", "school subject"), ("banana", "fruit")]
        word, category = random.choice(words)
        key = random.randint(1, 25)
        encoded = caesar(word, key, "encode")
        st.session_state.update({
            "dial_word": list(encoded),
            "original_word": word,
            "category": category,
            "dial_attempts": 0,
            "dial_solved": False
        })

    st.markdown(f"### Encrypted Word: `{''.join(st.session_state.dial_word)}`")
    st.info(f"Length: {len(st.session_state.original_word)} | Category: {st.session_state.category}")
    cols = st.columns(len(st.session_state.dial_word))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_attempt = []

    for i, col in enumerate(cols):
        with col:
            idx = alphabet.index(st.session_state.dial_word[i])
            up = st.button("🔼", key=f"up_{i}")
            down = st.button("🔽", key=f"down_{i}")
            if up:
                idx = (idx + 1) % 26
                st.session_state.dial_word[i] = alphabet[idx]
            elif down:
                idx = (idx - 1) % 26
                st.session_state.dial_word[i] = alphabet[idx]
            st.write(f"**{st.session_state.dial_word[i]}**")
            decoded_attempt.append(st.session_state.dial_word[i])

    decoded_word = ''.join(decoded_attempt)
    st.code(decoded_word)

    if not st.session_state.dial_solved and st.button("✅ Submit Guess"):
        if decoded_word == st.session_state.original_word:
            st.success("🎉 Correct!")
            st.session_state.dial_solved = True
        else:
            st.session_state.dial_attempts += 1
            if st.session_state.dial_attempts < 5:
                st.warning(f"❌ Wrong. Attempt {st.session_state.dial_attempts}/5")
            else:
                st.error("🚫 Out of attempts!")
                st.info(f"The correct word was: `{st.session_state.original_word}`")
                st.session_state.dial_solved = True

    if st.button("🔄 Reset Word"):
        for key in ["dial_word", "original_word", "category", "dial_attempts", "dial_solved"]:
            st.session_state.pop(key, None)
        st.experimental_rerun()