import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# --- Page Config ---
st.set_page_config(layout="wide", page_title="ලෝකයේ අරුම පුදුම තැන්", page_icon="🌎")

# --- CSS for Professional Look ---
st.markdown("""
<style>
    .main-title { font-size: 3rem; font-weight: bold; color: #2F80ED; text-align: center; margin-bottom: 20px; }
    .item-card { background-color: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 5px solid #2F80ED; margin-bottom: 20px; }
    .item-title { font-size: 1.5rem; font-weight: bold; color: #333; }
</style>
""", unsafe_allow_html=True)

# --- Image Loading Function ---
def show_img(url, caption):
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption=caption, use_container_width=True)
    except:
        st.error(f"පින්තූරය පූරණය කළ නොහැක: {caption}")

# --- Header ---
st.markdown("<h1 class='main-title'>🌍 ලෝකයේ අරුම පුදුම දෑ</h1>", unsafe_allow_html=True)

# --- Tabs ---
tabs = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

# 1. ලෝකයේ උසම කඳු 10
with tabs[0]:
    st.header("⛰️ ලෝකයේ උසම කඳු 10")
    data = [
        ("මවුන්ට් එවරස්ට් (Mount Everest)", "8,848m", "නේපාලය/චීනය", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg"),
        ("K2", "8,611m", "පාකිස්තානය/චීනය", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/K2_from_Concordia_Pakistan.jpg/640px-K2_from_Concordia_Pakistan.jpg"),
        ("කාංචන්ජංගා (Kangchenjunga)", "8,586m", "නේපාලය/ඉන්දියාව", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kangchenjunga.jpg/640px-Kangchenjunga.jpg"),
        ("ලොට්සේ (Lhotse)", "8,516m", "නේපාලය", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Lhotse_from_Kala_Patthar_2012.JPG/640px-Lhotse_from_Kala_Patthar_2012.JPG"),
        ("මකාලූ (Makalu)", "8,485m", "නේපාලය", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Makalu_from_Cho_Oyu_summit.jpg/640px-Makalu_from_Cho_Oyu_summit.jpg"),
        ("චෝ ඔයු (Cho Oyu)", "8,188m", "නේපාලය", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cho_Oyu_from_Gokyo_Ri.jpg/640px-Cho_Oyu_from_Gokyo_Ri.jpg"),
        ("දෞලගිරි (Dhaulagiri)", "8,167m", "නේපාලය", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Dhaulagiri_from_Poon_Hill.jpg/640px-Dhaulagiri_from_Poon_Hill.jpg"),
        ("මනස්ලු (Manaslu)", "8,163m", "නේපාලය", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Manaslu_from_Serang_Gompa.jpg/640px-Manaslu_from_Serang_Gompa.jpg"),
        ("නන්ගා පර්බට් (Nanga Parbat)", "8,126m", "පාකිස්තානය", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Nanga_Parbat.jpg/640px-Nanga_Parbat.jpg"),
        ("අන්නපූර්ණ (Annapurna)", "8,091m", "නේපාලය", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Annapurna_South_and_Fang_from_Annapurna_Base_Camp_in_Nepal.jpg/640px-Annapurna_South_and_Fang_from_Annapurna_Base_Camp_in_Nepal.jpg")
    ]
    for name, height, loc, url in data:
        col1, col2 = st.columns([1, 2])
        with col1: show_img(url, name)
        with col2: st.markdown(f"<div class='item-card'><p class='item-title'>{name}</p><p>උස: {height}<br>පිහිටීම: {loc}</p></div>", unsafe_allow_html=True)

# 2. ලෝකයේ උසම දිය ඇලි 10
with tabs[1]:
    st.header("🌊 ලෝකයේ උසම දිය ඇලි 10")
    falls = [
        ("ඒන්ජල් ෆෝල්ස් (Angel Falls)", "979m", "වෙනිසියුලාව", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG"),
        ("ටුගෙලා ෆෝල්ස් (Tugela Falls)", "948m", "දකුණු අප්‍රිකාව", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/TugelaFalls-Drakensberg.JPG/640px-TugelaFalls-Drakensberg.JPG")
        # (අමතර දිය ඇලි ලැයිස්තුව මෙහිදී Code එක දිග වැඩි නිසා කෙටි කර ඇත)
    ]
    for name, height, loc, url in falls:
        col1, col2 = st.columns([1, 2])
        with col1: show_img(url, name)
        with col2: st.markdown(f"<div class='item-card'><p class='item-title'>{name}</p><p>උස: {height}<br>පිහිටීම: {loc}</p></div>", unsafe_allow_html=True)

# 3. ලෝකයේ විශාලතම රටවල් 10
with tabs[2]:
    st.header("🗺️ ලෝකයේ විශාලතම රටවල් 10")
    countries = [
        ("රුසියාව (Russia)", "17,098,242 km²", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png"),
        ("කැනඩාව (Canada)", "9,984,670 km²", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Flag_of_Canada.svg/640px-Flag_of_Canada.svg.png")
    ]
    for name, area, url in countries:
        col1, col2 = st.columns([1, 2])
        with col1: show_img(url, name)
        with col2: st.markdown(f"<div class='item-card'><p class='item-title'>{name}</p><p>වර්ග ප්‍රමාණය: {area}</p></div>", unsafe_allow_html=True)

# 4. ලෝකයේ විශාලතම ගිනිකඳු 10
with tabs[3]:
    st.header("🌋 ලෝකයේ විශාලතම ගිනිකඳු 10")
    volcanoes = [
        ("මාඋනා ලෝවා (Mauna Loa)", "හවායි", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
    ]
    for name, loc, url in volcanoes:
        col1, col2 = st.columns([1, 2])
        with col1: show_img(url, name)
        with col2: st.markdown(f"<div class='item-card'><p class='item-title'>{name}</p><p>පිහිටීම: {loc}</p></div>", unsafe_allow_html=True)

# 5. ලෝකයේ දිගම ගංගා 10
with tabs[4]:
    st.header("🏞️ ලෝකයේ දිගම ගංගා 10")
    rivers = [
        ("නයිල් ගංගාව (Nile)", "6,650 km", "අප්‍රිකාව", "
