import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# --- Page Setup ---
st.set_page_config(layout="wide", page_title="World Top 10")

# පින්තූර Load කරන Function එක
def get_img(url):
    try:
        res = requests.get(url, timeout=10)
        return Image.open(BytesIO(res.content))
    except:
        return None

st.title("🌍 ලෝකයේ අරුම පුදුම තැන් 10")

# Tab පහක් හදමු
t1, t2, t3, t4, t5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

# 1. ලෝකයේ උසම කඳු 10
with t1:
    st.header("⛰️ ලෝකයේ උසම කඳු 10")
    mountains = [
        ("මවුන්ට් එවරස්ට්", "8,848m", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg"),
        ("K2", "8,611m", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/K2_from_Concordia_Pakistan.jpg/640px-K2_from_Concordia_Pakistan.jpg"),
        ("කාංචන්ජංගා", "8,586m", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kangchenjunga.jpg/640px-Kangchenjunga.jpg"),
        ("ලොට්සේ", "8,516m", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Lhotse_from_Kala_Patthar_2012.JPG/640px-Lhotse_from_Kala_Patthar_2012.JPG"),
        ("මකාලූ", "8,485m", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Makalu_from_Cho_Oyu_summit.jpg/640px-Makalu_from_Cho_Oyu_summit.jpg"),
        ("චෝ ඔයු", "8,188m", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cho_Oyu_from_Gokyo_Ri.jpg/640px-Cho_Oyu_from_Gokyo_Ri.jpg"),
        ("දෞලගිරි", "8,167m", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Dhaulagiri_from_Poon_Hill.jpg/640px-Dhaulagiri_from_Poon_Hill.jpg"),
        ("මනස්ලු", "8,163m", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Manaslu_from_Serang_Gompa.jpg/640px-Manaslu_from_Serang_Gompa.jpg"),
        ("නන්ගා පර්බට්", "8,126m", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Nanga_Parbat.jpg/640px-Nanga_Parbat.jpg"),
        ("අන්නපූර්ණ", "8,091m", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Annapurna_South_and_Fang_from_Annapurna_Base_Camp_in_Nepal.jpg/640px-Annapurna_South_and_Fang_from_Annapurna_Base_Camp_in_Nepal.jpg")
    ]
    for name, h, url in mountains:
        col1, col2 = st.columns([1, 2])
        with col1:
            img = get_img(url)
            if img: st.image(img)
        with col2:
            st.subheader(name)
            st.write(f"උස: {h}")
        st.divider()

# 2. ලෝකයේ උසම දිය ඇලි 10
with t2:
    st.header("🌊 ලෝකයේ උසම දිය ඇලි 10")
    falls = [
        ("ඒන්ජල් ෆෝල්ස්", "979m", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG"),
        ("ටුගෙලා ෆෝල්ස්", "948m", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/TugelaFalls-Drakensberg.JPG/640px-TugelaFalls-Drakensberg.JPG")
    ]
    for name, h, url in falls:
        img = get_img(url)
        if img: st.image(img, caption=f"{name} ({h})", width=500)
        st.divider()

# 3. ලෝකයේ විශාලතම රටවල් 10
with t3:
    st.header("🗺️ විශාලතම රටවල් 10")
    st.write("1. රුසියාව | 2. කැනඩාව | 3. චීනය | 4. ඇමරිකාව | 5. බ්‍රසීලය")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png")
    if img: st.image(img, width=400, caption="රුසියාව")

# 4. ලෝකයේ විශාලතම ගිනිකඳු 10
with t4:
    st.header("🌋 විශාලතම ගිනිකඳු 10")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
    if img: st.image(img, caption="1. මාඋනා ලෝවා")

# 5. ලෝකයේ දිගම ගංගා 10
with t5:
    st.header("🏞️ ලෝකයේ දිගම ගංගා 10")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Luxor_and_Nile.jpg/640px-Luxor_and_Nile.jpg")
    if img: st.image(img, caption="1. නයිල් ගංගාව")
