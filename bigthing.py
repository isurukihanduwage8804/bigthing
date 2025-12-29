import streamlit as st

# App එකේ මූලික සැකසුම්
st.set_page_config(layout="wide", page_title="ලෝකයේ අරුම පුදුම තැන්", page_icon="🌎")

st.markdown("<h1 style='text-align: center; color: #2F80ED;'>ලෝකයේ අරුම පුදුම තැන්</h1>", unsafe_allow_html=True)

# Tabs විදියට කරමු එතකොට වඩාත් පිරිසිදුයි
tab1, tab2, tab3, tab4, tab5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

# --- 1. කඳු ---
with tab1:
    st.header("ලෝකයේ උසම කඳු 10")
    mountains = [
        {"n": "මවුන්ට් එවරස්ට්", "h": "8,848m", "u": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/640px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg"},
        {"n": "K2", "h": "8,611m", "u": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/K2_from_Concordia_Pakistan.jpg/640px-K2_from_Concordia_Pakistan.jpg"}
    ]
    for m in mountains:
        col1, col2 = st.columns([1, 2])
        with col1: st.image(m['u'])
        with col2: st.subheader(f"{m['n']} ({m['h']})")
        st.divider()

# --- 2. දිය ඇලි ---
with tab2:
    st.header("ලෝකයේ උසම දිය ඇලි 10")
    st.subheader("1. ඒන්ජල් ෆෝල්ස් (979m) - වෙනිසියුලාව")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/640px-Salto_Angel-Canaima-Venezuela08.JPG")
    st.divider()

# --- 3. රටවල් ---
with tab3:
    st.header("විශාලතම රටවල් 10")
    st.subheader("1. රුසියාව (17,098,242 km²)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Flag_of_Russia.svg/640px-Flag_of_Russia.svg.png", width=400)
    st.divider()

# --- 4. ගිනිකඳු ---
with tab4:
    st.header("විශාලතම ගිනිකඳු 10")
    st.subheader("1. මාඋනා ලෝවා (හවායි)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Mauna_Loa_summit_caldera.jpg/640px-Mauna_Loa_summit_caldera.jpg")
    st.divider()

# --- 5. ගංගා ---
with tab5:
    st.header("ලෝකයේ දිගම ගංගා 10")
    st.subheader("1. නයිල් ගංගාව (6,650 km)")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Luxor_and_Nile.jpg/640px-Luxor_and_Nile.jpg")
    st.divider()
