import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# --- Page Config ---
st.set_page_config(layout="wide", page_title="World Wonders")

def get_img(url):
    try:
        res = requests.get(url, timeout=15)
        return Image.open(BytesIO(res.content))
    except:
        return None

st.title("🌍 ලෝකයේ අරුම පුදුම තැන්")

# Tabs
t1, t2, t3, t4, t5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

with t1:
    st.header("⛰️ ලෝකයේ උසම කඳු")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg")
    if img: st.image(img, caption="1. මවුන්ට් එවරස්ට් (8,848m)")
    st.write("නේපාලය සහ චීනය අතර පිහිටා ඇත.")

with t2:
    st.header("🌊 ලෝකයේ උසම දිය ඇලි")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG")
    if img: st.image(img, caption="1. ඒන්ජල් ෆෝල්ස් (979m)")
    st.write("වෙනිසියුලාවේ පිහිටා ඇත.")

with t3:
    st.header("🗺️ විශාලතම රටවල්")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png")
    if img: st.image(img, width=400, caption="1. රුසියාව")
    st.write("වර්ග ප්‍රමාණය: 17,098,242 km²")

with t4:
    st.header("🌋 විශාලතම ගිනිකඳු")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
    if img: st.image(img, caption="1. මාඋනා ලෝවා")
    st.write("හවායි හි පිහිටා ඇත.")

with t5:
    st.header("🏞️ ලෝකයේ දිගම ගංගා")
    img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Luxor_and_Nile.jpg/640px-Luxor_and_Nile.jpg")
    if img: st.image(img, caption="1. නයිල් ගංගාව")
    st.write("දිග: 6,650 km")
