import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# පින්තූර පූරණය කරන සරල Function එකක්
def get_img(url):
    try:
        res = requests.get(url, timeout=10)
        return Image.open(BytesIO(res.content))
    except:
        return None

st.set_page_config(layout="wide", page_title="World Wonders")
st.title("🌍 ලෝකයේ අරුම පුදුම තැන්")

# Tab පහක් හදමු
t1, t2, t3, t4, t5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

# 1. කඳු
with t1:
    st.header("ලෝකයේ උසම කඳු")
    col1, col2 = st.columns([1, 2])
    with col1:
        img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg")
        if img: st.image(img)
    with col2:
        st.subheader("1. මවුන්ට් එවරස්ට් (8,848m)")
        st.write("නේපාලය සහ චීනය අතර පිහිටා ඇත.")

# 2. දිය ඇලි
with t2:
    st.header("ලෝකයේ උසම දිය ඇලි")
    col1, col2 = st.columns([1, 2])
    with col1:
        img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG")
        if img: st.image(img)
    with col2:
        st.subheader("1. ඒන්ජල් ෆෝල්ස් (979m)")
        st.write("වෙනිසියුලාවේ පිහිටා ඇත.")

# 3. රටවල්
with t3:
    st.header("විශාලතම රටවල්")
    col1, col2 = st.columns([1, 2])
    with col1:
        img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png")
        if img: st.image(img, width=300)
    with col2:
        st.subheader("1. රුසියාව (17,098,242 km²)")
        st.write("ලෝකයේ විශාලතම රටයි.")

# 4. ගිනිකඳු
with t4:
    st.header("විශාලතම ගිනිකඳු")
    col1, col2 = st.columns([1, 2])
    with col1:
        img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
        if img: st.image(img)
    with col2:
        st.subheader("1. මාඋනා ලෝවා")
        st.write("හවායි හි පිහිටා ඇත.")

# 5. ගංගා
with t5:
    st.header("ලෝකයේ දිගම ගංගා")
    col1, col2 = st.columns([1, 2])
    with col1:
        img = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Luxor_and_Nile.jpg/640px-Luxor_and_Nile.jpg")
        if img: st.image(img)
    with col2:
        st.subheader("1. නයිල් ගංගාව (6,650 km)")
        st.write("අප්‍රිකා මහද්වීපයේ පිහිටා ඇත.")
