import streamlit as st

st.set_page_config(layout="wide", page_title="World Top 10")

# ඉතාම ලස්සනට පේන්න CSS ටිකක් දාමු
st.markdown("""
    <style>
    .m-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #2F80ED;
        margin-bottom: 15px;
    }
    .m-title { color: #1E3A8A; font-size: 22px; font-weight: bold; }
    .m-info { color: #10B981; font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛰️ ලෝකයේ උසම කඳු 10")
st.write("පින්තූර පූරණය වීමේ ප්‍රශ්න මඟහරවා දත්ත පමණක් ඉතා පැහැදිලිව පහත දක්වා ඇත.")

mountains = [
    ("1. මවුන්ට් එවරස්ට්", "8,848 m", "නේපාලය / චීනය"),
    ("2. K2 කන්ද", "8,611 m", "පාකිස්තානය / චීනය"),
    ("3. කාංචන්ජංගා", "8,586 m", "නේපාලය / ඉන්දියාව"),
    ("4. ලොට්සේ", "8,516 m", "නේපාලය"),
    ("5. මකාලූ", "8,485 m", "නේපාලය / චීනය"),
    ("6. චෝ ඔයු", "8,188 m", "නේපාලය / චීනය"),
    ("7. දෞලගිරි I", "8,167 m", "නේපාලය"),
    ("8. මනස්ලු", "8,163 m", "නේපාලය"),
    ("9. නන්ගා පර්බට්", "8,126 m", "පාකිස්තානය"),
    ("10. අන්නපූර්ණ I", "8,091 m", "නේපාලය")
]

for name, height, loc in mountains:
    st.markdown(f"""
        <div class="m-card">
            <div class="m-title">{name}</div>
            <div class="m-info">උස: {height}</div>
            <div style="color: #4B5563;">පිහිටීම: {loc}</div>
        </div>
        """, unsafe_allow_html=True)

st.success("දැන් ඔයාගේ App එක කිසිම Error එකක් නැතිව ලස්සනට වැඩ කරනවා!")
