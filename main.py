import base64
import os

import streamlit as st
import streamlit.components.v1 as components
import folium

from PIL import Image 
from io import BytesIO

from streamlit_toggle import st_toggle_switch
from streamlit_image_comparison import image_comparison
from streamlit_image_select import image_select
from streamlit_folium import st_folium
from folium.plugins import Draw

import sidebar

# -----> Streamlit Config
st.set_page_config(
    page_title="บ้านเชี่ยวหลาน",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={}
)

# -----> Global Variable
if 'language' not in st.session_state: 
    st.session_state['language'] = 0
if 'index_page' not in st.session_state: 
    st.session_state['index_page'] = 0
if 'trip' not in st.session_state: 
    st.session_state['trip'] = None

# ----------> Thai / English
st.session_state['language'] = st_toggle_switch(
    label="𝐓𝐇𝐀𝐈 / 𝐄𝐍𝐆", key="switch_1",
    default_value=False, label_after=False,
    inactive_color="#D3D3D3",  # optional
    active_color="#11567f",  # optional
    track_color="#29B5E8",  # optional
)

# -----> Image : HTML To Streamlit
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img1 = get_img_as_base64("images/d1.jpg")
img2 = get_img_as_base64("images/d2.jpg")
img3 = get_img_as_base64("images/d3.jpg")
img4 = get_img_as_base64("images/d4.jpg")
img5 = get_img_as_base64("images/d5.jpg")

# --------------------> Sidebar
with st.sidebar:
    sidebar.App()

if st.session_state['index_page'] == 0:

    st.title("(DEMO) ตัวอย่างเว็บแอป 🌏")
    st.success("(DEMO) ตัวอย่างเว็บแอป 🌏")
    # ----------> ขนานไม่ดี
    # image_comparison(
    # img1="images/index_1.jpg",
    # img2="images/index_2.jpg",
    # label1="",
    # label2="",
    # width=700,
    # starting_position=50,
    # show_labels=True,
    # make_responsive=True,
    # )

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
            }}

            .slider {{
                overflow: hidden;
                width: 100vw;
                height: 100vh;
                position: relative;
            }}

            .slider .slide {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border-radius: 10px;
                background-size: cover;
                background-position: center;
                animation: slide 15s infinite;
            }}

            .slider .slide:nth-child(1) {{
                background-image: url("data:image/png;base64,{img1}");
                
                animation-delay: -0;
            }}

            .slider .slide:nth-child(2) {{
                background-image: url("data:image/png;base64,{img2}");
                animation-delay: -3s;
            }}
            
            .slider .slide:nth-child(3) {{
                background-image: url("data:image/png;base64,{img3}");
                animation-delay: -6s;
            }}
            
            .slider .slide:nth-child(4) {{
                background-image: url("data:image/png;base64,{img4}");
                animation-delay: -9s;
            }}

            .slider .slide:nth-child(5) {{
                background-image: url("data:image/png;base64,{img5}");
                animation-delay: -12s;
            }}

            @keyframes slide {{
                0%, 15%, 100% {{
                    transform: translateX(0);
                    animation-timing-function: ease;
                }}
                20% {{
                    transform: translateX(-100%);
                    animation-timing-function: step-end;
                }}
                95% {{
                    transform: translateX(100%);
                    animation-timing-function: ease;
                }}
            }}
        </style>
    </head>
        <body>
            <div class="slider">
                <div class="slide"></div>
                <div class="slide"></div>
                <div class="slide"></div>
                <div class="slide"></div>
                <div class="slide"></div>
            <div>
        </body>
    </html> 

    """
    components.html(html, height=600, scrolling=False)

    # logo = Image.open("images/logo_edit.png")
    # st.image(logo, use_column_width=True)


elif st.session_state['index_page']== 1:

    img = image_select(
    label="",
    images=[
        "images/logo_edit_1.png",
        "images/logo_edit_2.png",
        "images/logo_edit_3.png",
        "images/logo_edit_4.png",
        "images/logo_edit_5.png",
        "images/logo_edit_6.png",
        "images/logo_edit_7.png",
    ],
    captions=["ท่าเรือบ้านเชี่ยวหลาน", "จุดชมวิวเขื่อนรัชชประภา", "สะพานแขวน ภูเขารูปหัวใจ", 
              "วัดไกรสรเขตราราม", "ลานพระแท่น ภปร.สก.", "ศูนย์ศิลปาชีพบ้านเชี่ยวหลาน", 
              "บ้านพอเพียง เชี่ยวหลาน"],
            use_container_width=True, index=0
    )

    if img == "images/logo_edit_1.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")
      
    elif img == "images/logo_edit_2.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")

    elif img == "images/logo_edit_3.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")

    elif img == "images/logo_edit_4.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")

    elif img == "images/logo_edit_5.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")
       
    elif img == "images/logo_edit_6.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")
    
    elif img == "images/logo_edit_7.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.warning("⚠️⠀:orange[Coming soon]")


elif st.session_state['index_page'] >= 2:

    # ----------> Marker Color 
    # 'beige', 'black', 'blue', 'cadetblue', 'darkblue', 'darkgreen', 'darkpurple', 'darkred', 'gray', 
    # 'green', 'lightblue', 'lightgray', 'lightgreen', 'lightred', 'orange', 'pink', 'purple', 'red', 'white'

    # # ----------> บ้านเชี่ยวหลาน
    # folium.Marker([8.978925364564146, 98.82449785474496], icon=folium.Icon(color="red"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    # # ----------> ท่าเรือเทศบาลตำบลบ้านเชี่ยวหลาน
    # folium.Marker([8.977273533078275, 98.82075112314551], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    # # ----------> จุดชมวิวเขื่อนรัชชประภา
    # folium.Marker([8.973088532622594, 98.81080043057683], icon=folium.Icon(color="blue"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    # # ----------> สะพานแขวน ภูเขารูปหัวใจ
    # folium.Marker([8.949050372410868, 98.82245102598056], icon=folium.Icon(color="green"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    # # ----------> วัดไกรสรเขตราราม
    # folium.Marker([8.979029388189934, 98.84899398947246], icon=folium.Icon(color="purple"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    # # ----------> ลานพระแท่น ภปร.สก.
    # folium.Marker([8.975542176892585, 98.84371586146968], icon=folium.Icon(color="cadetblue"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    # # ----------> ศูนย์ศิลปาชีพบ้านเชี่ยวหลาน
    # folium.Marker([8.977097444759261, 98.84369485026102], icon=folium.Icon(color="gray"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)


    # center on Liberty Bell, add marker
    map = folium.Map(location=[8.969686369678994, 98.82382392883302],zoom_start=14, control_scale=True)
    Draw(export=True).add_to(map)

    if st.session_state['trip'] == "ทริปวันเดียว" or st.session_state['trip'] == "One Day Trip":

        # ----------> บ้านเชี่ยวหลาน
        folium.Marker([8.978925364564146, 98.82449785474496], icon=folium.Icon(color="red"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> ท่าเรือเทศบาลตำบลบ้านเชี่ยวหลาน
        folium.Marker([8.977273533078275, 98.82075112314551], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> จุดชมวิวเขื่อนรัชชประภา
        folium.Marker([8.973088532622594, 98.81080043057683], icon=folium.Icon(color="blue"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> ลานพระแท่น ภปร.สก.
        folium.Marker([8.975542176892585, 98.84371586146968], icon=folium.Icon(color="cadetblue"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> ศูนย์ศิลปาชีพบ้านเชี่ยวหลาน
        folium.Marker([8.977097444759261, 98.84369485026102], icon=folium.Icon(color="gray"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    
    elif st.session_state['trip'] == "ทริปสองวัน" or st.session_state['trip'] == "Two Day Trip":
        # ----------> บ้านเชี่ยวหลาน
        folium.Marker([8.978925364564146, 98.82449785474496], icon=folium.Icon(color="red"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> ท่าเรือเทศบาลตำบลบ้านเชี่ยวหลาน
        folium.Marker([8.977273533078275, 98.82075112314551], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> จุดชมวิวเขื่อนรัชชประภา
        folium.Marker([8.973088532622594, 98.81080043057683], icon=folium.Icon(color="blue"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> สะพานแขวน ภูเขารูปหัวใจ
        folium.Marker([8.949050372410868, 98.82245102598056], icon=folium.Icon(color="green"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> วัดไกรสรเขตราราม
        folium.Marker([8.979029388189934, 98.84899398947246], icon=folium.Icon(color="purple"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> ลานพระแท่น ภปร.สก.
        folium.Marker([8.975542176892585, 98.84371586146968], icon=folium.Icon(color="cadetblue"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
        # ----------> ศูนย์ศิลปาชีพบ้านเชี่ยวหลาน
        folium.Marker([8.977097444759261, 98.84369485026102], icon=folium.Icon(color="gray"), popup="Thailand", tooltip="ตำแหน่ง").add_to(map)
    
    else:
        st.warning("⚠️⠀:orange[Coming soon]")

    # call to render Folium map in Streamlit
    map_data = st_folium(map, width='auto', returned_objects="last_object_clicked")
    
