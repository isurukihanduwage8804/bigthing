import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# පින්තූර පූරණය කරන ශ්‍රිතය (Function)
def load_img(url):
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None

# App සැකසුම්
st.set_page_config(layout="wide", page_title="ලෝකයේ අරුම පුදුම තැන්")

st.markdown("<h1 style='text-align: center; color: #2F80ED;'>🌍 ලෝකයේ අරුම පුදුම තැන්</h1>", unsafe_allow_html=True)

# Tabs මගින් වර්ගීකරණය
tab1, tab2, tab3, tab4, tab5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

# --- 1. කඳු ---
with tab1:
    st.header("⛰️ ලෝකයේ උසම කඳු 10")
    items = [
        ("මවුන්ට් එවරස්ට්", "8,848m", "නේපාලය/චීනය", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg"),
        ("K2", "8,611m", "පාකිස්තානය/චීනය", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/K2_from_Concordia_Pakistan.jpg/640px-K2_from_Concordia_Pakistan.jpg")
    ]
    for name, h, loc, url in items:
        col1, col2 = st.columns([1, 2])
        img = load_img(url)
        with col1:
            if img: st.image(img)
            else: st.warning("පින්තූරය පූරණය කළ නොහැක")
        with col2:
            st.subheader(name)
            st.write(f"උස: {h} | පිහිටීම: {loc}")
        st.divider()

# --- 2. දිය ඇලි ---
with tab2:
    st.header("🌊 ලෝකයේ උසම දිය ඇලි 10")
    falls = [
        ("ඒන්ජල් ෆෝල්ස්", "979m", "වෙනිසියුලාව", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG")
    ]
    for name, h, loc, url in falls:
        col1, col2 = st.columns([1, 2])
        img = load_img(url)
        with col1:
            if img: st.image(img)
        with col2:
            st.subheader(name)
            st.write(f"උස: {h} | පිහිටීම: {loc}")

# --- 3. රටවල් ---
with tab3:
    st.header("🗺️ ලෝකයේ විශාලතම රටවල් 10")
    countries = [
        ("රුසියාව", "17,098,242 km²", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png")
    ]
    for name, area, url in countries:
        col1, col2 = st.columns([1, 2])
        img = load_img(url)
        with col1:
            if img: st.image(img, width=300)
        with col2:
            st.subheader(name)
            st.write(f"වර්ග ප්‍රමාණය: {area}")

# --- 4. ගිනිකඳු ---
with tab4:
    st.header("🌋 ලෝකයේ විශාලතම ගිනිකඳු 10")
    volcanoes = [
        ("මාඋනා ලෝවා", "හවායි, ඇමරිකාව", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
    ]
    for name, loc, url in volcanoes:
        col1, col2 = st.columns([1, 2])
        img = load_img(url)
        with col1:
            if img: st.image(img)
        with col2:
            st.subheader(name)
            st.write(f"පිහිටීම: {loc}")

# --- 5. ගංගා ---
with tab5:
    st.header("🏞️ ලෝකයේ දිගම ගංගා 10")
    rivers = [
        ("නයිල් ගංගාව", "6,650 km", "අප්‍රිකාව", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Luxor_and_Nile.jpg/640px-Luxor_and_Nile.jpg")
    ]
    for name, d, loc, url in rivers:
        col1, col2 = st.columns([1, 2])
        img = load_img(url)
        with col1:
            if img: st.image(img)
        with col2:
            st.subheader(name)
            st.write(f"දිග: {d} | පිහිටීම: {loc}")
