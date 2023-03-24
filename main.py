import io
import os
import base64

import streamlit as st
import streamlit.components.v1 as components

from PIL import Image
from io import BytesIO

from streamlit_toggle import st_toggle_switch
from streamlit_image_comparison import image_comparison
from streamlit_image_select import image_select

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

st.image('images\logo_edit.png', use_column_width=True)
# -----> Image : HTML To Streamlit
def get_img_as_base64(file):
    st.write(file)
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# img1 = get_img_as_base64("images\d2.jpg")
# img2 = get_img_as_base64("images\d2.jpg")
# img3 = get_img_as_base64("images\d3.jpg")
# img4 = get_img_as_base64("images\d4.jpg")
# img5 = get_img_as_base64("images\d5.jpg")

# --------------------> Sidebar
with st.sidebar:
    sidebar.App()

if st.session_state['index_page'] == 0:

    st.success("Test")
    
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

#     html = f"""
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <style>
#             body {{
#                 margin: 0;
#             }}

#             .slider {{
#                 overflow: hidden;
#                 width: 100vw;
#                 height: 100vh;
#                 position: relative;
#             }}

#             .slider .slide {{
#                 position: absolute;
#                 top: 0;
#                 left: 0;
#                 width: 100%;
#                 height: 100%;
#                 background-size: cover;
#                 background-position: center;
#                 animation: slide 15s infinite;
#             }}

#             .slider .slide:nth-child(1) {{
#                 background-image: url("data:image/png;base64,{img1}");
#                 animation-delay: -0;
#             }}

#             .slider .slide:nth-child(2) {{
#                 background-image: url("data:image/png;base64,{img2}");
#                 animation-delay: -3s;
#             }}
            
#             .slider .slide:nth-child(3) {{
#                 background-image: url("data:image/png;base64,{img3}");
#                 animation-delay: -6s;
#             }}
            
#             .slider .slide:nth-child(4) {{
#                 background-image: url("data:image/png;base64,{img4}");
#                 animation-delay: -9s;
#             }}

#             .slider .slide:nth-child(5) {{
#                 background-image: url("data:image/png;base64,{img5}");
#                 animation-delay: -12s;
#             }}

#             @keyframes slide {{
#                 0%, 15%, 100% {{
#                     transform: translateX(0);
#                     animation-timing-function: ease;
#                 }}
#                 20% {{
#                     transform: translateX(-100%);
#                     animation-timing-function: step-end;
#                 }}
#                 95% {{
#                     transform: translateX(100%);
#                     animation-timing-function: ease;
#                 }}
#             }}
#         </style>
#     </head>
#         <body>
#             <div class="slider">
#                 <div class="slide"></div>
#                 <div class="slide"></div>
#                 <div class="slide"></div>
#                 <div class="slide"></div>
#                 <div class="slide"></div>
#             <div>
#         </body>
#     </html> 

#     """

#     components.html(html, height=800, scrolling=False)


elif st.session_state['index_page'] == 1:
    
    st.info("แนะนำแหล่งท่องเที่ยวบ้านเชี่ยวหลาน")
    
    img = image_select(
    label="",
    images=[
        "images/logo_edit.png",
        "images/logo_edit.png",
        "images/logo_edit.png",
        "images/logo_edit.png",
        "images/logo_edit.png",
        "images/logo_edit.png",
        "images/logo_edit.png",
    ],
    captions=["1", "2", "3", "4", "5", "6", "7"]
    )

elif st.session_state['index_page'] == 2:

    st.warning("⚠️⠀:orange[Coming soon]")
