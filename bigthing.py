import streamlit as st

st.set_page_config(page_title="World Wonders", layout="wide")

st.title("🌍 ලෝකයේ අරුම පුදුම තැන්")

# Sidebar එකක් දාමු එවිට ඔයාට වෙනස් දේවල් තෝරන්න ලේසියි
option = st.sidebar.selectbox(
    'ඔබට නැරඹීමට අවශ්‍ය කුමක්ද?',
    ('කඳු (Mountains)', 'දිය ඇලි (Waterfalls)', 'රටවල් (Countries)')
)

if option == 'කඳු (Mountains)':
    st.header("⛰️ මවුන්ට් එවරස්ට්")
    # ඉතාමත් කෙටි ලින්ක් එකක්
    st.image("https://tinyurl.com/everest-pic", width=700)
    st.write("ලෝකයේ උසම කන්දයි (8,848m).")

elif option == 'දිය ඇලි (Waterfalls)':
    st.header("🌊 ඒන්ජල් ෆෝල්ස්")
    st.image("https://tinyurl.com/angel-fall", width=700)
    st.write("ලෝකයේ උසම දිය ඇල්ලයි (979m).")

elif option == 'රටවල් (Countries)':
    st.header("🗺️ රුසියාව")
    st.image("https://tinyurl.com/russia-flag-pic", width=400)
    st.write("ලෝකයේ විශාලතම රටයි.")
