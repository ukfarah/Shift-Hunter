import streamlit as st
from game_functions import single_player_mode
from ui_functions import display_encrypted_message, display_input_field, display_start_button
from caesar_cipher.caesar import caesar
from PIL import Image
import os
import random

# === Paths
LOGO_PATH = os.path.join(os.path.dirname(__file__), "logo/LOGO.png")
ASCII_HELPER = os.path.join(os.path.dirname(__file__), "logo/table.jpg")

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

    try:
        st.image(Image.open(ASCII_HELPER), caption=" Table", use_column_width=True)
    except:
        st.caption(" Table (image not found)")

# === Header
st.markdown("<h1 style='text-align: center;'>🎮 Shift Hunter</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Crack the Cipher. Challenge Your Brain.</h3>", unsafe_allow_html=True)
st.markdown("---")

# === MIND SHIFT
if mode == "🧠 Mind Shift":
    st.subheader("🧠 Mind Shift")
    with st.expander("📜 How to Play"):
        st.markdown("""
        You're shown an encrypted word. Guess the Caesar cipher key (1–25) to decode it.

        #### 🔐 Example:
        - Original: `hello`
        - Key: `2`
        - Encrypted: `jgnnq`
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
        st.info(f"Length: {len(st.session_state.original_message)} letters | Category: {st.session_state.category}")
        guess = display_input_field()
        if guess:
            try:
                guess = int(guess)
                if guess == st.session_state.shift_key:
                    st.success("✅ Correct! You cracked the cipher!")
                    decoded = caesar(st.session_state.encrypted_message, guess, "decode")
                    st.info(f"🔓 Original message: `{decoded}`")
                    st.markdown("### 🔎 Letter Mappings & ASCII Shifts:")
                    for e, o in zip(st.session_state.encrypted_message, decoded):
                        st.markdown(f"`{e}` ({ord(e)}) → `{o}` ({ord(o)})")
                    st.session_state.solved = True
                else:
                    st.session_state.attempts += 1
                    hint = "🔼 Try a larger number!" if guess < st.session_state.shift_key else "🔽 Try a smaller number!"
                    st.warning(f"{hint} ❌ (Attempt {st.session_state.attempts}/3)")
                    if st.session_state.attempts >= 3:
                        st.error("🚫 Out of attempts!")
                        decoded = caesar(st.session_state.encrypted_message, st.session_state.shift_key, "decode")
                        st.info(f"📜 Original: `{decoded}`")
                        st.markdown("### 🔎 Letter Mappings & ASCII Shifts:")
                        for e, o in zip(st.session_state.encrypted_message, decoded):
                            st.markdown(f"`{e}` ({ord(e)}) → `{o}` ({ord(o)})")
                        st.session_state.solved = True
            except ValueError:
                st.warning("⚠️ Please enter a valid number.")

    if st.session_state.encrypted_message and st.session_state.solved:
        if st.button("🔄 Try Another Word"):
            for key in ["encrypted_message", "shift_key", "original_message", "category", "attempts", "solved"]:
                st.session_state[key] = None
            st.experimental_rerun()

# === SPIN & CRACK
elif mode == "🔓 Spin & Crack":
    st.subheader("🔓 Spin & Crack")
    with st.expander("📜 How to Play"):
        st.markdown("""
        <p><strong>🎯 Goal:</strong> Decode the hidden word by rotating each letter.</p>
        <ul>
            <li>Spin each dial forward or backward.</li>
            <li>Each dial shows its <strong>current letter</strong>, <strong>original letter</strong>, and <strong>shift key</strong>.</li>
            <li>The encrypted word above stays fixed. Only your guess below changes.</li>
            <li>You have <strong>5 attempts</strong> to guess the word.</li>
        </ul>
        """, unsafe_allow_html=True)

    if "dial_word" not in st.session_state:
        word_list = [
            ("hello", "greeting"), ("math", "school subject"), ("code", "tech term"),
            ("lion", "animal"), ("banana", "fruit"), ("planet", "space object"),
            ("river", "natural element"), ("oxygen", "science"), ("flute", "instrument"), ("teacher", "profession")
        ]
        word, category = random.choice(word_list)
        key = random.randint(1, 25)
        encoded = caesar(word, key, "encode")
        st.session_state.update({
            "dial_word": list(encoded),
            "dial_initial": list(encoded),
            "original_word": word,
            "category": category,
            "dial_attempts": 0,
            "dial_solved": False
        })

    # Fixed encoded word (stays constant)
    st.code(''.join(st.session_state.dial_initial), language="none")
    st.info(f"Length: {len(st.session_state.original_word)} letters | Category: {st.session_state.category}")

    cols = st.columns(len(st.session_state.dial_word))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_attempt = []

    for i, col in enumerate(cols):
        with col:
            original_letter = st.session_state.dial_initial[i]
            current_letter = st.session_state.dial_word[i]

            index_orig = alphabet.index(original_letter)
            index_curr = alphabet.index(current_letter)

            up = st.button("▲", key=f"up_{i}")
            down = st.button("▼", key=f"down_{i}")

            if up:
                index_curr = (index_curr + 1) % 26
                st.session_state.dial_word[i] = alphabet[index_curr]

            elif down:
                index_curr = (index_curr - 1) % 26
                st.session_state.dial_word[i] = alphabet[index_curr]

            current_letter = st.session_state.dial_word[i]
            index_curr = alphabet.index(current_letter)
            shift = (index_curr - index_orig) % 26
            shift_display = f"+{shift}" if shift <= 13 else f"-{26 - shift}"

            st.write(f"**{current_letter}**")
            st.caption(f"📌 Current: `{current_letter}`")
            st.caption(f"🔙 From: `{original_letter}`")
            st.caption(f"🔑 Shift: `{shift_display}`")

            decoded_attempt.append(current_letter)

    decoded_word = ''.join(decoded_attempt)
    st.code(decoded_word)

    col_reset, col_submit = st.columns([1, 3])
    with col_reset:
        if st.button("🔄RESET "):
            st.session_state.dial_word = list(st.session_state.dial_initial)
            st.experimental_rerun()

    with col_submit:
        if not st.session_state.dial_solved and st.button("✅Check"):
            if decoded_word == st.session_state.original_word:
                st.success("🎉 Correct!")
                st.markdown("### 🔎 Letter Mappings & ASCII Shifts:")
                for enc_char, orig_char in zip(decoded_word, st.session_state.original_word):
                    st.markdown(f"`{enc_char}` ({ord(enc_char)}) → `{orig_char}` ({ord(orig_char)})")
                st.session_state.dial_solved = True
            else:
                st.session_state.dial_attempts += 1
                if st.session_state.dial_attempts < 5:
                    st.error(f"❌ Nope! Try again! (Attempt {st.session_state.dial_attempts}/5)")
                else:
                    st.error("🚫 Out of attempts!")
                    st.info(f"📜 Answer was: `{st.session_state.original_word}`")
                    st.markdown("### 🔎 Letter Mappings & ASCII Shifts:")
                    for enc_char, orig_char in zip(decoded_word, st.session_state.original_word):
                        st.markdown(f"`{enc_char}` ({ord(enc_char)}) → `{orig_char}` ({ord(orig_char)})")
                    st.session_state.dial_solved = True

    if st.session_state.dial_solved:
        if st.button("🎲 Try Another Word"):
            for key in ["dial_word", "dial_initial", "original_word", "category", "dial_attempts", "dial_solved"]:
                st.session_state.pop(key, None)
            st.experimental_rerun()
