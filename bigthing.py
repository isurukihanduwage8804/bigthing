import streamlit as st

# Page Configuration
st.set_page_config(layout="wide", page_title="World Wonders")

st.markdown("<h1 style='text-align: center; color: #2F80ED;'>🌍 ලෝකයේ අරුම පුදුම තැන්</h1>", unsafe_allow_html=True)

# Tabs
t1, t2, t3, t4, t5 = st.tabs(["⛰️ කඳු", "🌊 දිය ඇලි", "🗺️ රටවල්", "🌋 ගිනිකඳු", "🏞️ ගංගා"])

# 1. කඳු
with t1:
    st.header("⛰️ ලෝකයේ උසම කඳු")
    # Wikipedia වෙනුවට Unsplash ලින්ක් භාවිතා කර ඇත
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800", caption="මවුන්ට් එවරස්ට් (Mount Everest)")
    st.write("උස: 8,848m | නේපාලය")

# 2. දිය ඇලි
with t2:
    st.header("🌊 ලෝකයේ උසම දිය ඇලි")
    st.image("https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=800", caption="ඒන්ජල් ෆෝල්ස් (Angel Falls)")
    st.write("උස: 979m | වෙනිසියුලාව")

# 3. රටවල්
with t3:
    st.header("🗺️ විශාලතම රටවල්")
    st.image("https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?w=800", caption="ලෝක සිතියම - රුසියාව")
    st.write("රුසියාව (17,098,242 km²)")

# 4. ගිනිකඳු
with t4:
    st.header("🌋 විශාලතම ගිනිකඳු")
    st.image("https://images.unsplash.com/photo-1518495973542-4542c06a5843?w=800", caption="ගිනිකන්දක් (Volcano)")
    st.write("මාඋනා ලෝවා - හවායි")

# 5. ගංගා
with t5:
    st.header("🏞️ ලෝකයේ දිගම ගංගා")
    st.image("https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800", caption="ගංගාවක් (River)")
    st.write("නයිල් ගංගාව - දිග: 6,650 km")
