"""
Minionese Translator -- Streamlit Web App
-------------------------------------------
A Minion-themed interactive UI wrapped around the same translator engine
used by the CLI (dictionary.py, phonetics.py, translator.py).

Run with:
    streamlit run app.py
"""

import streamlit as st

from dictionary import DICTIONARY
from translator import to_english, to_minionese

st.set_page_config(
    page_title="Minionese Translator",
    page_icon="🍌",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Minion-themed styling: goggle-grey, denim-blue overalls, banana-yellow
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --minion-yellow: #FFD43B;
        --minion-yellow-dark: #F5B700;
        --overalls-blue: #2E5FA3;
        --overalls-blue-dark: #1E3F73;
        --goggle-grey: #B8B8B8;
        --goggle-dark: #4a4a4a;
    }

    .stApp {
        background: linear-gradient(180deg, var(--minion-yellow) 0%, #FFE470 55%, var(--minion-yellow) 100%);
    }

    /* Title banner styled like Minion overalls stitching */
    .minion-header {
        background: var(--overalls-blue);
        border-radius: 14px;
        padding: 1.1rem 1.4rem;
        margin-bottom: 1.2rem;
        border: 4px dashed var(--minion-yellow-dark);
        text-align: center;
        box-shadow: 0 4px 0 var(--overalls-blue-dark);
    }
    .minion-header h1 {
        color: var(--minion-yellow);
        font-size: 2.1rem;
        margin: 0;
        letter-spacing: 1px;
        text-shadow: 2px 2px 0 var(--overalls-blue-dark);
    }
    .minion-header p {
        color: #eaeaea;
        margin: 0.3rem 0 0 0;
        font-size: 0.95rem;
    }

    /* Goggle-style divider */
    .goggle-divider {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin: 0.8rem 0 1.2rem 0;
    }
    .goggle-divider .lens {
        width: 34px;
        height: 34px;
        background: var(--goggle-grey);
        border: 4px solid var(--goggle-dark);
        border-radius: 50%;
    }
    .goggle-divider .bridge {
        width: 40px;
        height: 6px;
        background: var(--goggle-dark);
        border-radius: 3px;
    }

    /* Output card */
    .translation-output {
        background: white;
        border: 3px solid var(--overalls-blue);
        border-radius: 12px;
        padding: 1.1rem;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--overalls-blue-dark);
        min-height: 60px;
        box-shadow: 0 3px 0 var(--overalls-blue);
    }

    /* Buttons */
    .stButton > button {
        background: var(--overalls-blue);
        color: var(--minion-yellow);
        border: none;
        border-radius: 8px;
        font-weight: 700;
        box-shadow: 0 3px 0 var(--overalls-blue-dark);
    }
    .stButton > button:hover {
        background: var(--overalls-blue-dark);
        color: white;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        font-weight: 700;
        color: var(--overalls-blue-dark);
    }

    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="minion-header">
        <h1>🍌 Minionese Translator 🍌</h1>
        <p>Bello! Type English, get Minionese. Bee-do-bee-do!</p>
    </div>
    <div class="goggle-divider">
        <div class="lens"></div><div class="bridge"></div><div class="lens"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_translate, tab_reverse, tab_wordbank, tab_about = st.tabs(
    ["🍌 Translate", "🔄 Reverse", "📖 Word Bank", "ℹ️ About"]
)

# ---------------------------------------------------------------------------
# Translate tab
# ---------------------------------------------------------------------------
with tab_translate:
    st.subheader("English ➜ Minionese")
    english_input = st.text_area(
        "Type your English text:",
        placeholder="e.g. Hello my friend, let's go eat cake!",
        height=120,
    )
    if st.button("Translate! 🍌", key="translate_btn"):
        if english_input.strip():
            result = to_minionese(english_input)
            st.markdown(f'<div class="translation-output">{result}</div>', unsafe_allow_html=True)
            st.balloons()
        else:
            st.warning("Type something first, bello!")

# ---------------------------------------------------------------------------
# Reverse tab
# ---------------------------------------------------------------------------
with tab_reverse:
    st.subheader("Minionese ➜ English")
    st.caption("Works for dictionary words (e.g. bello, poopaye, tank yu). Phonetic-fallback words can't be reversed.")
    minionese_input = st.text_area(
        "Type your Minionese text:",
        placeholder="e.g. Bello bapple, tank yu!",
        height=120,
    )
    if st.button("Translate back! 🔄", key="reverse_btn"):
        if minionese_input.strip():
            result = to_english(minionese_input)
            st.markdown(f'<div class="translation-output">{result}</div>', unsafe_allow_html=True)
        else:
            st.warning("Type something first, bello!")

# ---------------------------------------------------------------------------
# Word Bank tab
# ---------------------------------------------------------------------------
with tab_wordbank:
    st.subheader("📖 Word Bank")
    search = st.text_input("Search a word:", placeholder="e.g. love, banana, hero...")

    entries = sorted(DICTIONARY.items())
    if search:
        s = search.lower()
        entries = [(k, v) for k, v in entries if s in k.lower() or s in v[0].lower()]

    st.caption(f"{len(entries)} word(s)")

    for english, (minionese, note) in entries:
        col1, col2, col3 = st.columns([2, 2, 3])
        col1.markdown(f"**{english}**")
        col2.markdown(f"🍌 *{minionese}*")
        col3.caption(note)

# ---------------------------------------------------------------------------
# About tab
# ---------------------------------------------------------------------------
with tab_about:
    st.subheader("ℹ️ About this project and its Creator")
    st.markdown(
        """
        Tiisoto plojectoo iisito maadeatto fooleeno funzo

        **How it works:**
        Nobody wants to know the secret Chikkka 🍌

        **Creator:** [A Minion]
        """
    )
    st.markdown("🍌 *Poopaye!* 🍌")