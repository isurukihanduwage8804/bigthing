import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# --- පින්තූර Load කරන Function එක ---
def get_img(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers, timeout=10)
        return Image.open(BytesIO(res.content))
    except:
        return None

st.set_page_config(layout="wide", page_title="World Wonders")
st.title("🌍 ලෝකයේ අරුම පුදුම දෑ")

# Tab 5ක් හදමු
t1, t2, t3, t4, t5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

with t1:
    st.header("⛰️ ලෝකයේ උසම කඳු")
    img1 = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg")
    if img1: st.image(img1, caption="මවුන්ට් එවරස්ට්")
    st.write("උස: 8,848m | නේපාලය")

with t2:
    st.header("🌊 ලෝකයේ උසම දිය ඇලි")
    img2 = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG")
    if img2: st.image(img2, caption="ඒන්ජල් ෆෝල්ස්")
    st.write("උස: 979m | වෙනිසියුලාව")

with t3:
    st.header("🗺️ විශාලතම රටවල්")
    img3 = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png")
    if img3: st.image(img3, width=300)
    st.write("රුසියාව (17,098,242 km²)")

with t4:
    st.header("🌋 විශාලතම ගිනිකඳු")
    img4 = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
    if img4: st.image(img4, caption="මාඋනා ලෝවා")
    st.write("හවායි හි පිහිටා ඇත.")

with t5:
    st.header("🏞️ ලෝකයේ දිගම ගංගා")
    img5 = get_img("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Luxor_and_Nile.jpg/640px-Luxor_and_Nile.jpg")
    if img5: st.image
