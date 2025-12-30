import streamlit as st

# --- PAGE CONFIG ---
# Tab icon ko clean rakha hai
st.set_page_config(page_title="BROBOND ERP", page_icon="⚪", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* SIDEBAR WIDTH */
    [data-testid="stSidebar"] {
        min-width: 500px !important;
        max-width: 500px !important;
        background-color: #ffffff;
    }

    /* LOGO SECTION - PURE BLACK & CENTERED */
    .logo-container {
        text-align: center;
        width: 100%;
        padding-top: 50px;
        padding-bottom: 30px;
    }
    .logo-main {
        font-size: 75px !important;
        font-weight: 900;
        color: #000000;
        font-family: 'Arial Black', sans-serif;
        line-height: 1;
        margin-bottom: 10px;
    }
    .logo-sub {
        font-size: 28px !important;
        font-weight: bold;
        color: #444444;
        letter-spacing: 1px;
    }

    /* CATEGORY HEADER STYLE */
    .category-header {
        font-size: 24px !important;
        font-weight: bold;
        color: #666;
        padding-left: 20px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* MENU BUTTONS WITH ICONS */
    div.stButton > button {
        height: 85px !important;
        font-size: 28px !important; /* Icons ke saath text fit karne ke liye */
        font-weight: 800 !important;
        border-radius: 15px !important;
        margin-bottom: 15px !important;
        text-align: left !important;
        padding-left: 30px !important;
        background-color: #fcfcfc !important;
        border: 2px solid #eeeeee !important;
        color: #000000 !important;
    }
    
    div.stButton > button:hover {
        border-color: #000000 !important;
        background-color: #f8f8f8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION STATE ---
if "page" not in st.session_state:
    st.session_state.page = "SALES DASHBOARD"

# --- SIDEBAR ---
with st.sidebar:
    # LOGO (Center & No Icon)
    st.markdown('''
        <div class="logo-container">
            <div class="logo-main">BROBOND</div>
            <div class="logo-sub">A Brand by SNBPL</div>
        </div>
    ''', unsafe_allow_html=True)
    
    st.write("---")
    
    # CATEGORY HEADER
    st.markdown('<div class="category-header">📋 MAIN CATEGORIES</div>', unsafe_allow_html=True)

    # CATEGORIES WITH ICONS (Wapas add kar diye hain)
    pages = {
        "📊 SALES DASHBOARD": "SALES DASHBOARD",
        "📞 LEADS DATA": "LEADS DATA",
        "💸 EXPENSES": "EXPENSES",
        "👤 AYUSH BROBOND (HRM)": "AYUSH BROBOND (HRM)",
        "👑 HIMANSHU BROBOND (CEO)": "HIMANSHU BROBOND (CEO)",
        "👔 RITIK BROBOND (MD)": "RITIK BROBOND (MD)"
    }

    for label, pg_name in pages.items():
        if st.button(label, use_container_width=True):
            st.session_state.page = pg_name

# --- MAIN AREA ---
st.markdown(f"<h1 style='font-size: 55px;'>📍 {st.session_state.page}</h1>", unsafe_allow_html=True)
st.write("---")
st.info(f"Bhai, {st.session_state.page} panel ab ekdum set hai!")
