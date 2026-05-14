import streamlit as st
from deep_translator import GoogleTranslator
from typing import Dict

# ---------------- CONFIG ----------------
st.set_page_config(page_title="LingoSphere", layout="wide")


# ---------------- LOAD LANGUAGES ----------------
raw_languages = GoogleTranslator().get_supported_languages(as_dict=True)

if isinstance(raw_languages, dict):
    languages: Dict[str, str] = raw_languages
else:
    languages = {lang: lang for lang in raw_languages}

language_names = sorted(languages.keys())

# ---------------- STATE ----------------
translated = None  # ✅ FIX: prevents NameError

# ---------------- FULL ORANGE UI ----------------
st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: linear-gradient(180deg, #ff9a2f, #ff7a00) !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stSidebar"] {
    background: transparent !important;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #7a2e00;
    text-shadow:
        0px 0px 30px rgba(255,255,255,1),
        0px 0px 60px rgba(255,200,100,0.9);
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    color: #5c2500;
    margin-bottom: 25px;
}

/* FLAGS (SINGLE LINE) */
.flag-row {
    display: flex;
    justify-content: center;
    flex-wrap: nowrap;
    gap: 18px;
    margin-bottom: 20px;
    overflow-x: auto;
    padding-bottom: 10px;
}

.flag {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    padding: 5px;
    background: linear-gradient(145deg, rgba(255,255,255,0.7), rgba(255,255,255,0.2));
    backdrop-filter: blur(6px);
    border: 2px solid rgba(255,255,255,0.9);
    box-shadow:
        inset 0 2px 6px rgba(255,255,255,0.8),
        0 0 10px rgba(255,255,255,0.6),
        0 4px 12px rgba(0,0,0,0.2);
}

.flag img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
}

/* CHAT */
.chat-line {
    white-space: nowrap;
    overflow: hidden;
    width: 100%;
    margin-bottom: 25px;
}

.chat-track {
    display: inline-block;
    animation: scroll 18s linear infinite;
}

.chat {
    display: inline-block;
    background: rgba(255,255,255,0.6);
    padding: 8px 14px;
    border-radius: 20px;
    margin: 0 10px;
}

@keyframes scroll {
    from { transform: translateX(100%); }
    to { transform: translateX(-100%); }
}

/* INPUT */
.stTextArea textarea {
    border-radius: 12px;
}

/* BUTTON */
div.stButton > button {
    display: block;
    margin: 0 auto;
    width: 220px;
    height: 50px;
    border-radius: 12px;
    background-color: #7a2e00;
    color: white;
    font-weight: 600;
    font-size: 16px;
}

/* RESULT */
.result-title {
    color: white;
    font-size: 26px;
    font-weight: 600;
    margin-top: 30px;
}

.result-box {
    background: white;
    color: black;
    padding: 18px;
    border-radius: 12px;
    margin-top: 10px;
    font-size: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}


                       
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title"> LingoSphere</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Where languages meet clarity</div>', unsafe_allow_html=True)

# ---------------- FLAGS ----------------
st.markdown("""
<div class="flag-row">
<img class="flag" src="https://flagcdn.com/w80/us.png">
<img class="flag" src="https://flagcdn.com/w80/in.png">
<img class="flag" src="https://flagcdn.com/w80/fr.png">
<img class="flag" src="https://flagcdn.com/w80/es.png">
<img class="flag" src="https://flagcdn.com/w80/jp.png">
<img class="flag" src="https://flagcdn.com/w80/de.png">
<img class="flag" src="https://flagcdn.com/w80/br.png">
<img class="flag" src="https://flagcdn.com/w80/kr.png">
<img class="flag" src="https://flagcdn.com/w80/ru.png">
<img class="flag" src="https://flagcdn.com/w80/it.png">
<img class="flag" src="https://flagcdn.com/w80/cn.png">
<img class="flag" src="https://flagcdn.com/w80/tr.png">
<img class="flag" src="https://flagcdn.com/w80/pt.png">
<img class="flag" src="https://flagcdn.com/w80/sa.png">
<img class="flag" src="https://flagcdn.com/w80/eg.png">
<img class="flag" src="https://flagcdn.com/w80/nl.png">
<img class="flag" src="https://flagcdn.com/w80/se.png">
<img class="flag" src="https://flagcdn.com/w80/no.png">
</div>
""", unsafe_allow_html=True)

# ---------------- CHAT ----------------
st.markdown("""
<div class="chat-line">
<div class="chat-track">
<span class="chat">👋 Hello!</span>
<span class="chat">FR Bonjour!</span>
<span class="chat">ES ¡Hola!</span>
<span class="chat">JP こんにちは！</span>
<span class="chat">DE Hallo!</span>
<span class="chat">CN 你好！</span>
<span class="chat">IN नमस्ते!</span>
<span class="chat">AR مرحبا!</span>
<span class="chat">PT Olá!</span>
<span class="chat">RU Привет!</span>
<span class="chat">IT Ciao!</span>
<span class="chat">KR 안녕하세요!</span>
<span class="chat">TR Merhaba!</span>
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", language_names)

with col2:
    target_lang = st.selectbox("Target Language", language_names)

text = st.text_area("Enter text")

# ---------------- BUTTON ----------------
clicked = st.button("TRANSLATE")

# ---------------- TRANSLATION ----------------
if clicked:
    if not text.strip():
        st.warning("Enter text")
    elif source_lang == target_lang:
        st.warning("Languages cannot be same")
    else:
        source_code = languages[source_lang]
        target_code = languages[target_lang]

        translated = GoogleTranslator(
            source=source_code,
            target=target_code
        ).translate(text)

# ---------------- OUTPUT ----------------
if translated:
    st.markdown(
        '<div class="result-title">Translated Text</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="result-box">{translated}</div>',
        unsafe_allow_html=True
    )

    
   
    