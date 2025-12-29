import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# --- App එකේ මූලික සැකසුම් ---
st.set_page_config(layout="wide", page_title="ලෝකයේ අරුම පුදුම තැන්", page_icon="🌎")

# --- CSS Styling ---
st.markdown("""
<style>
.main-header {
    font-size: 3.5em;
    font-weight: bold;
    color: #2F80ED;
    text-align: center;
    margin-bottom: 0.5em;
    text-shadow: 2px 2px 4px #aaa;
}
.sub-header {
    font-size: 2.2em;
    font-weight: bold;
    color: #4F4F4F;
    margin-top: 1.5em;
    margin-bottom: 1em;
    border-bottom: 2px solid #E0E0E0;
    padding-bottom: 0.5em;
}
.item-title {
    font-size: 1.5em;
    font-weight: bold;
    color: #333;
    margin-top: 1em;
    margin-bottom: 0.5em;
}
.item-description {
    font-size: 1.1em;
    color: #555;
    line-height: 1.6;
}
.stImage {
    border-radius: 10px;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
}
.stExpander > div > p {
    font-size: 1.1em;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# --- පින්තූර Load කරන Function එක (URL වලින්) ---
def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # HTTP errors සඳහා
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        st.error(f"පින්තූරය Load කිරීමේදී දෝෂයක්: {e}. කරුණාකර URL එක පරීක්ෂා කරන්න.")
        return None
    except Exception as e:
        st.error(f"පින්තූරය සැකසීමේදී දෝෂයක්: {e}")
        return None

# --- මාතෘකාව ---
st.markdown("<p class='main-header'>ලෝකයේ අරුම පුදුම තැන්</p>", unsafe_allow_html=True)
st.write("🌍 ලෝකයේ උසම කඳු, දිය ඇලි, විශාලතම රටවල්, විශාලතම ගිනි කඳු සහ දිගම ගංගා ගැන දැනගන්න!")

# --- 1. ලෝකයේ උසම කඳු 10 ---
st.markdown("<p class='sub-header'>⛰️ ලෝකයේ උසම කඳු 10</p>", unsafe_allow_html=True)

mountains = [
    {"name": "මවුන්ට් එවරස්ට් (Mount Everest)", "height": "8,848.86 m", "location": "නේපාලය/චීනය", "desc": "ලෝකයේ උසම කඳු මුදුන වන මවුන්ට් එවරස්ට් හිමාල කඳුකරයේ පිහිටා ඇත. කඳු නගින්නන්ගේ සිහිනය වන මෙය අතිශය අභියෝගාත්මක ගමනාන්තයකි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Mount_Everest_from_Kala_Patthar_-_October_2015.jpg/1280px-Mount_Everest_from_Kala_Patthar_-_October_2015.jpg"},
    {"name": "කේ2 (K2 / Mount Godwin Austen)", "height": "8,611 m", "location": "පාකිස්තානය/චීනය", "desc": "ලෝකයේ දෙවන උසම කන්ද වන K2, Karakoram කඳුකරයේ පිහිටා ඇත. මෙය එවරස්ට් වලට වඩා අභියෝගාත්මක යැයි සැලකේ.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/K2_from_Concordia_Pakistan.jpg/1280px-K2_from_Concordia_Pakistan.jpg"},
    {"name": "කාංචන්ජංගා (Kangchenjunga)", "height": "8,586 m", "location": "නේපාලය/ඉන්දියාව", "desc": "ලෝකයේ තුන්වන උසම කන්ද වන කාංචන්ජංගා යන්නෙහි තේරුම 'මහා හිම වල නිධානයන් පහ' යන්නයි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Kangchenjunga.jpg/1280px-Kangchenjunga.jpg"},
    {"name": "ලොට්සේ (Lhotse)", "height": "8,516 m", "location": "නේපාලය/චීනය", "desc": "එවරස්ට් කන්දට ඉතා ආසන්නව පිහිටා ඇති ලොට්සේ, ලෝකයේ සිව්වන උසම කන්දයි. එහි දකුණු මුහුණත ලෝකයේ වඩාත්ම අභියෝගාත්මක කඳු නැගීමේ බිත්ති වලින් එකක් ලෙස සැලකේ.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Lhotse_from_Kala_Patthar_2012.JPG/1280px-Lhotse_from_Kala_Patthar_2012.JPG"},
    {"name": "මකාලූ (Makalu)", "height": "8,485 m", "location": "නේපාලය/චීනය", "desc": "තනිව පිහිටි දැවැන්ත පිරමිඩයක් වැනි හැඩයක් ඇති මකාලූ කන්ද ලෝකයේ පස්වන උසම කන්දයි. එහි බෑවුම් සහිත කඳු බෑවුම් කඳු නගින්නන් හට අභියෝගාත්මක වේ.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Makalu_from_Cho_Oyu_summit.jpg/1280px-Makalu_from_Cho_Patthar_summit.jpg"},
    {"name": "චෝ ඔයු (Cho Oyu)", "height": "8,201 m", "location": "නේපාලය/චීනය", "desc": "චෝ ඔයු යන්නෙහි තේරුම 'පිරිසිදු ටර්කොයිස් දෙවඟන' යන්නයි. එය ලෝකයේ හයවන උසම කන්ද වන අතර සාපේක්ෂව පහසු කඳු නැගීමේ මාර්ගයක් ඇත.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Cho_Oyu_from_Gokyo_Ri.jpg/1280px-Cho_Oyu_from_Gokyo_Ri.jpg"},
    {"name": "දෞලගිරි (Dhaulagiri)", "height": "8,167 m", "location": "නේපාලය", "desc": "දෞලගිරි යන්නෙහි තේරුම 'සුදු කන්ද' යන්නයි. එය ලෝකයේ හත්වන උසම කන්ද වන අතර, එහි බටහිර මුහුණතේ ඇති අතිවිශාල බෑවුම ප්‍රසිද්ධය.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Dhaulagiri_from_Poon_Hill.jpg/1280px-Dhaulagiri_from_Poon_Hill.jpg"},
    {"name": "මනස්ලු (Manaslu)", "height": "8,163 m", "location": "නේපාලය", "desc": "මනස්ලු යන්නෙහි තේරුම 'ආත්මයේ කන්ද' යන්නයි. එය ලෝකයේ අටවන උසම කන්ද වන අතර, එහි කඳු මුදුනට නගින පළමු පුද්ගලයා ජපන් ජාතිකයෙකි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Manaslu_from_Serang_Gompa.jpg/1280px-Manaslu_from_Serang_Gompa.jpg"},
    {"name": "නන්ගා පර්බට් (Nanga Parbat)", "height": "8,126 m", "location": "පාකිස්තානය", "desc": "නන්ගා පර්බට් යන්නෙහි තේරුම 'නිරුවත් කන්ද' යන්නයි. එය ලෝකයේ නවවන උසම කන්ද වන අතර, කඳු නගින්නන්ට ඉතා භයානක කන්දක් ලෙස සැලකේ.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Nanga_Parbat.jpg/1280px-Nanga_Parbat.jpg"},
    {"name": "අන්නපූර්ණ I (Annapurna I)", "height": "8,091 m", "location": "නේපාලය", "desc": "අන්නපූර්ණ I යනු ලෝකයේ දසවන උසම කන්දයි. එය ඉතා භයානක කඳු මුදුනක් ලෙස සැලකෙන අතර, සාර්ථකත්වයේ අනුපාතය අඩුය.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Annapurna_South_and_Fang_from_Annapurna_Base_Camp_in_Nepal.jpg/1280px-Annapurna_South_and_Fang_from_Annapurna_Base_Camp_in_Nepal.jpg"},
]

for mountain in mountains:
    st.markdown(f"<p class='item-title'>{mountain['name']} ({mountain['height']})</p>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        img = load_image_from_url(mountain["img_url"])
        if img:
            st.image(img, caption=mountain["name"], use_column_width=True)
    with col2:
        st.markdown(f"<p class='item-description'><b>පිහිටීම:</b> {mountain['location']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='item-description'>{mountain['desc']}</p>", unsafe_allow_html=True)
    st.markdown("---")

# --- 2. ලෝකයේ උසම දිය ඇලි 10 ---
st.markdown("<p class='sub-header'>🌊 ලෝකයේ උසම දිය ඇලි 10</p>", unsafe_allow_html=True)

waterfalls = [
    {"name": "ඒන්ජල් ෆෝල්ස් (Angel Falls)", "height": "979 m", "location": "වෙනිසියුලාව", "desc": "ලෝකයේ උසම දිය ඇල්ල වන ඒන්ජල් ෆෝල්ස්, කැනයිමා ජාතික වනෝද්‍යානයේ පිහිටා ඇත. එහි ජලය කෙලින්ම වැටෙන උස මීටර් 807 කි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Salto_Angel-Canaima-Venezuela08.JPG/1280px-Salto_Angel-Canaima-Venezuela08.JPG"},
    {"name": "ටුගෙලා ෆෝල්ස් (Tugela Falls)", "height": "948 m", "location": "දකුණු අප්‍රිකාව", "desc": "දකුණු අප්‍රිකාවේ ඩ්‍රැකන්ස්බර්ග් කඳුකරයේ පිහිටා ඇති ටුගෙලා ෆෝල්ස් ලෝකයේ දෙවන උසම දිය ඇල්ලයි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/TugelaFalls-Drakensberg.JPG/1280px-TugelaFalls-Drakensberg.JPG"},
    {"name": "ඔක්තොම්බ් ෆෝල්ස් (Oktombe Falls)", "height": "900 m (ආසන්න වශයෙන්)", "location": "පේරු", "desc": "පේරු හි පිහිටා ඇති මෙය ලෝකයේ තුන්වන උසම දිය ඇල්ල ලෙස සැලකේ, නමුත් නිල මිනුම් තවමත් විවාදාත්මකය.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Yumbilla_Waterfalls_view_from_Catarata_La_Ocha.jpg/1280px-Yumbilla_Waterfalls_view_from_Catarata_La_Ocha.jpg"},
    {"name": "ඔයුමෙස්ට් ෆෝල්ස් (Ouyemest Falls)", "height": "820 m", "location": "ග්‍රීන්ලන්තය", "desc": "ග්‍රීන්ලන්තයේ පිහිටා ඇති මෙම දිය ඇල්ල අයිස් දියවීමෙන් නිර්මාණය වන අතර කාලගුණික තත්ත්වයන් අනුව වෙනස් වේ.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Tiniteqilaaq_view.jpg/1280px-Tiniteqilaaq_view.jpg"}, # Generic Greenland image
    {"name": "යේලොසෙමයිට් ෆෝල්ස් (Yosemite Falls)", "height": "739 m", "location": "ඇමරිකා එක්සත් ජනපදය", "desc": "කැලිෆෝනියාවේ යේලොසෙමයිට් ජාතික වනෝද්‍යානයේ පිහිටා ඇති මෙය උතුරු ඇමරිකාවේ උසම දිය ඇල්ලයි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Yosemite_Falls_from_Cooks_Meadow.jpg/1280px-Yosemite_Falls_from_Cooks_Meadow.jpg"},
    {"name": "මුටරාසි ෆෝල්ස් (Mutarazi Falls)", "height": "772 m", "location": "සිම්බාබ්වේ", "desc": "නැගෙනහිර සිම්බාබ්වේ හි පිහිටා ඇති මුටරාසි ෆෝල්ස්, සිම්බාබ්වේ හි උසම දිය ඇල්ලයි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Mutarazi_Falls.JPG/1280px-Mutarazi_Falls.JPG"},
    {"name": "බ්‍රවුන් ෆෝල්ස් (Browne Falls)", "height": "836 m", "location": "නවසීලන්තය", "desc": "නවසීලන්තයේ ෆියෝර්ඩ්ලන්ඩ් ජාතික වනෝද්‍යානයේ පිහිටා ඇති බ්‍රවුන් ෆෝල්ස් ලෝකයේ උසම දිය ඇලි වලින් එකකි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Browne_Falls_South_Island_New_Zealand.jpg/1280px-Browne_Falls_South_Island_New_Zealand.jpg"},
    {"name": "මොනාරේ ෆෝල්ස් (Monarere Falls)", "height": "780 m", "location": "නවසීලන්තය", "desc": "නවසීලන්තයේ පිහිටි තවත් උස දිය ඇල්ලක් වන මෙය, කඳුකර ප්‍රදේශයක පිහිටා ඇත.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Milford_Sound%2C_Fiordland%2C_New_Zealand.jpg/1280px-Milford_Sound%2C_Fiordland%2C_New_Zealand.jpg"}, # Generic New Zealand waterfall image
    {"name": "රිබන් ෆෝල්ස් (Ribbon Falls)", "height": "491 m", "location": "ඇමරිකා එක්සත් ජනපදය", "desc": "කැලිෆෝනියාවේ යේලොසෙමයිට් නිම්නයේ පිහිටා ඇති රිබන් ෆෝල්ස්, යේලොසෙමයිට් ෆෝල්ස් වලට නුදුරින් පිහිටා ඇත.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Ribbon_Fall_Yosemite_Valley.jpg/1280px-Ribbon_Fall_Yosemite_Valley.jpg"},
    {"name": "විනුෆොසන් (Vinnufossen)", "height": "860 m", "location": "නෝර්වේ", "desc": "නෝර්වේ හි පිහිටා ඇති විනුෆොසන්, යුරෝපයේ උසම දිය ඇල්ල වන අතර ලෝකයේ හයවන උසම දිය ඇල්ලයි.", "img_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Vinnufossen.jpg/1280px-Vinnufossen.jpg"},
]

for waterfall in waterfalls:
    st.markdown(f"<p class='item-title'>{waterfall['name']} ({waterfall['height']})</p>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        img = load_image_from_url(waterfall["img_url"])
        if img:
            st.
