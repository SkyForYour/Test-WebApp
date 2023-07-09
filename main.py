import base64
import os

import streamlit as st
import streamlit.components.v1 as components

import folium.plugins as plugins
import folium

import gpxpy
import gpxpy.gpx

from PIL import Image 
from io import BytesIO

from streamlit_image_select import image_select
from streamlit_folium import st_folium

import sidebar

st.set_page_config(
    page_title="บ้านเชี่ยวหลาน",
    page_icon="🏞️",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={}
)

if 'index_page' not in st.session_state: 
    st.session_state['index_page'] = 0
if 'trip' not in st.session_state: 
    st.session_state['trip'] = None

# -----> Image : HTML To Streamlit
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# -----> GPX Line
def GPX(file):
    gpx_file = open(f'{file}', 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    # ave_lat = sum(p[0] for p in points)/len(points)
    # ave_lon = sum(p[1] for p in points)/len(points)
    return points

img1 = get_img_as_base64("images/into/I1.JPG")
img2 = get_img_as_base64("images/into/I2.jpg")
img3 = get_img_as_base64("images/into/I3.JPG")
img4 = get_img_as_base64("images/into/I4.jgp")
img5 = get_img_as_base64("images/into/I5.jgp")

# img1 = get_img_as_base64("images/into/I1.jpg")
# img2 = get_img_as_base64("images/into/I2.jpg")
# img3 = get_img_as_base64("images/into/I3.JPG")
# img4 = get_img_as_base64("images/into/I4.jpg")
# img5 = get_img_as_base64("images/into/I5.jpg")
# img6 = get_img_as_base64("images/into/I6.JPG")
# img7 = get_img_as_base64("images/into/I7.JPG")
# img8 = get_img_as_base64("images/into/I8.JPG")
# img9 = get_img_as_base64("images/into/I9.jpg")
# img10 = get_img_as_base64("images/into/I10.JPG")
# img11 = get_img_as_base64("images/into/I11.JPG")
# img12 = get_img_as_base64("images/into/I12.jpg")
# img13 = get_img_as_base64("images/into/I12.jpg")
# img14 = get_img_as_base64("images/into/I14.jpg")
# img15 = get_img_as_base64("images/into/I15.jpg")

# -----> Sidebar
with st.sidebar:
    sidebar.App()

if st.session_state['index_page'] == 0:
    
    st.header("🌏 บ้านเชี่ยวหลาน :blue[(Web App Demo)]")
    
    html = f"""
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
    components.html(html, height=630, scrolling=False)
  
    # html = f"""
    #     <style>
    #         body{{
    #             margin: 0;
    #             padding: 0;
    #             display: flex;
    #             justify-content: center;
    #             align-items: center;
    #         }}

    #         .slider{{
    #             width: 800px;
    #             height: 500px;
    #             border-radius: 10px;
    #             overflow: hidden;
    #         }}

    #         .slides{{
    #             width: 500%;
    #             height: 500px;
    #             display: flex;

    #         }}

    #         .slides input{{
    #             display: none;
    #         }}

    #         .slide{{
    #             width: 20%;
    #             transition: 2s;
    #         }}

    #         .slide img{{
    #             width: 800px;
    #             height: 500px;
    #         }}

    #         .navigation-mannual{{
    #             position: absolute;
    #             width: 800px;
    #             margin-top: -40px;
    #             display: flex;
    #             justify-content: center;
    #         }}

    #         .mannual-btn{{
    #             border: 2px solid #ccc;
    #             padding: 5px;
    #             border-radius: 10px;
    #             cursor: pointer;
    #             transition: 1s;
    #         }}

    #         .mannual-btn:not(:last-child){{
    #             margin-right: 40px;
    #         }}
    #         .mannual-btn:hover{{
    #             background-color: #ccc;
    #         }}
    #         #radio1:checked ~ .first{{
    #             margin-left: 0;
    #         }}
    #         #radio2:checked ~ .first{{
    #             margin-left: -20%;
    #         }}
    #         #radio3:checked ~ .first{{
    #             margin-left: -40%;
    #         }}
    #         #radio4:checked ~ .first{{
    #             margin-left: -60%;
    #         }}
    #         #radio5:checked ~ .first{{
    #             margin-left: -80%;
    #         }}
    #         #radio6:checked ~ .first{{
    #             margin-left: -100%;
    #         }}
    #         #radio7:checked ~ .first{{
    #             margin-left: -120%;
    #         }}
    #         #radio8:checked ~ .first{{
    #             margin-left: -140%;
    #         }}
    #         #radio9:checked ~ .first{{
    #             margin-left: -160%;
    #         }}
    #         #radio10:checked ~ .first{{
    #             margin-left: -180%;
    #         }}
    #         #radio11:checked ~ .first{{
    #             margin-left: -200%;
    #         }}
    #         #radio12:checked ~ .first{{
    #             margin-left: -220%;
    #         }}
    #         #radio13:checked ~ .first{{
    #             margin-left: -240%;
    #         }}
    #         #radio14:checked ~ .first{{
    #             margin-left: -260%;
    #         }}
    #         #radio15:checked ~ .first{{
    #             margin-left: -280%;
    #         }}

    #         .navigation-auto{{
    #             position: absolute;
    #             display: flex;
    #             width: 800px;
    #             justify-content: center;
    #             margin-top: 460px;
    #         }}

    #         .navigation-auto div{{
    #             border: 2px solid #333;
    #             padding: 5px;
    #             border-radius: 10px;
    #             transition: 1s;
    #         }}

    #         .navigation-auto div:not(:last-child){{
    #             margin-right: 40px;
    #         }}

    #         #radio1:checked ~.navigation-auto .auto-btn-1{{
    #             background: #ccc;
    #         }}
    #         #radio2:checked ~.navigation-auto .auto-btn-2{{
    #             background: #ccc;
    #         }}
    #         #radio3:checked ~.navigation-auto .auto-btn-3{{
    #             background: #ccc;
    #         }}
    #         #radio4:checked ~.navigation-auto .auto-btn-4{{
    #             background: #ccc;
    #         }}
    #         #radio5:checked ~.navigation-auto .auto-btn-5{{
    #             background: #ccc;
    #         }}
    #         #radio6:checked ~.navigation-auto .auto-btn-6{{
    #             background: #ccc;
    #         }}
    #         #radio7:checked ~.navigation-auto .auto-btn-7{{
    #             background: #ccc;
    #         }}
    #         #radio8:checked ~.navigation-auto .auto-btn-8{{
    #             background: #ccc;
    #         }}
    #         #radio9:checked ~.navigation-auto .auto-btn-9{{
    #             background: #ccc;
    #         }}
    #         #radio10:checked ~.navigation-auto .auto-btn-01{{
    #             background: #ccc;
    #         }}
    #         #radio11:checked ~.navigation-auto .auto-btn-11{{
    #             background: #ccc;
    #         }}
    #         #radio12:checked ~.navigation-auto .auto-btn-12{{
    #             background: #ccc;
    #         }}
    #         #radio13:checked ~.navigation-auto .auto-btn-13{{
    #             background: #ccc;
    #         }}
    #         #radio14:checked ~.navigation-auto .auto-btn-14{{
    #             background: #ccc;
    #         }}
    #         #radio15:checked ~.navigation-auto .auto-btn-15{{
    #             background: #ccc;
    #         }}

    #     </style>

    #     <body>
    #     <div class="slider">
    #         <div class="slides">
    #         <input type="radio" name="radio-btn" id="radio1">
    #         <input type="radio" name="radio-btn" id="radio2">
    #         <input type="radio" name="radio-btn" id="radio3">
    #         <input type="radio" name="radio-btn" id="radio4">
    #         <input type="radio" name="radio-btn" id="radio5">
    #         <input type="radio" name="radio-btn" id="radio6">
    #         <input type="radio" name="radio-btn" id="radio7">
    #         <input type="radio" name="radio-btn" id="radio8">
    #         <input type="radio" name="radio-btn" id="radio9">
    #         <input type="radio" name="radio-btn" id="radio10">
    #         <input type="radio" name="radio-btn" id="radio11">
    #         <input type="radio" name="radio-btn" id="radio12">
    #         <input type="radio" name="radio-btn" id="radio13">
    #         <input type="radio" name="radio-btn" id="radio14">
    #         <input type="radio" name="radio-btn" id="radio15">

    #         <div class="slide first">
    #             <img src="data:image/png;base64,{img1}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img2}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img3}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img4}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img5}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img6}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img7}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img8}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img9}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img10}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img11}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img12}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img13}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img14}" alt="">
    #         </div>
    #         <div class="slide">
    #             <img src="data:image/png;base64,{img15}" alt="">
    #         </div>
    #             <div class="navigation-auto">
    #                 <div class="auto-btn-1"></div>
    #                 <div class="auto-btn-2"></div>
    #                 <div class="auto-btn-3"></div>
    #                 <div class="auto-btn-4"></div>
    #                 <div class="auto-btn-5"></div>
    #                 <div class="auto-btn-6"></div>
    #                 <div class="auto-btn-7"></div>
    #                 <div class="auto-btn-8"></div>
    #                 <div class="auto-btn-9"></div>
    #                 <div class="auto-btn-10"></div>
    #                 <div class="auto-btn-11"></div>
    #                 <div class="auto-btn-12"></div>
    #                 <div class="auto-btn-13"></div>
    #                 <div class="auto-btn-14"></div>
    #                 <div class="auto-btn-15"></div>
    #             </div>
    #         </div>

    #         <div class="navigation-mannual">
    #             <label for="radio1" class="mannual-btn"></label>
    #             <label for="radio2" class="mannual-btn"></label>
    #             <label for="radio3" class="mannual-btn"></label>
    #             <label for="radio4" class="mannual-btn"></label>
    #             <label for="radio5" class="mannual-btn"></label>
    #             <label for="radio6" class="mannual-btn"></label>
    #             <label for="radio7" class="mannual-btn"></label>
    #             <label for="radio8" class="mannual-btn"></label>
    #             <label for="radio9" class="mannual-btn"></label>
    #             <label for="radio10" class="mannual-btn"></label>
    #             <label for="radio11" class="mannual-btn"></label>
    #             <label for="radio12" class="mannual-btn"></label>
    #             <label for="radio13" class="mannual-btn"></label>
    #             <label for="radio14" class="mannual-btn"></label>
    #             <label for="radio15" class="mannual-btn"></label>
    #         </div>
    #     </div>

    #     <script>
    #         var counter = 1;
    #         setInterval(function()  {{
    #             document.getElementById('radio'+ counter).checked = true;
    #             counter++; 
    #             if(counter>15){{
    #                 counter=1
    #             }}
    #         }}, 5000);
    #     </script>
    #     </body>
    #     """
    # components.html(html, height=500, scrolling=False)

    st.header('📌 หัวข้อเนื้อหา')
    st.caption("\-⠀**แนะนำกลุ่มชุมชนบ้านเชี่ยวหลาน** / **แนะนำแหล่งท่องเที่ยว** / **แนะนำโปรแกรมการท่องเที่ยว**")
    st.markdown("- เนื้อหาข้อมูลต่าง ๆ⠀.⠀.⠀.")
    st.markdown("- เนื้อหาข้อมูลต่าง ๆ⠀.⠀.⠀.")
    st.markdown("- เนื้อหาข้อมูลต่าง ๆ⠀.⠀.⠀.")

elif st.session_state['index_page'] == 1: # ----------> เมนูแสดงภาพวิวท่องเที่ยว

    img = image_select(
    label="",
    images=[
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg",
        "images/topic_1.jpg", 
        "images/topic_1.jpg",
    ],
    captions=["⠀ บ้านสวนกัญจรดา", "⠀ อชิระฟาร์ม", "⠀ จุดชมวิวเขื่อน", 
              "⠀ บ้านน้ำขิงโฮมสเตย์", "⠀ ผ้าทอมือบ้านดชี่ยวหลาน", "⠀ ท่าเรือ", 
              "⠀ เขาตาพัด", "⠀ เขาสามเกรอ", "⠀ แพนางไพร", "⠀ ลานพระแทน"],
            use_container_width=True, index=0,
    )
    
    if img == "images/topic_1.jpg":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)

        col1, col2 = st.columns([2.04,1])
        col1.image(Image.open("images/t_1_1.jpg"))
        col2.image(Image.open("images/t_1_2.jpg"))
        col2.image(Image.open("images/t_1_3.jpg"))

        col1, col2 = st.columns([1,1.18])
        col1.image(Image.open("images/t_1_4.jpg"))
        col2.image(Image.open("images/t_1_5.jpg"))
    
    elif img == "images/topic_2.jpg":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns([1,1,1,1])
        col1.image(Image.open("images/t_2_6.jpg"))
        col2.image(Image.open("images/t_2_7.jpg"))
        col3.image(Image.open("images/t_2_8.jpg"))
        col4.image(Image.open("images/t_2_9.jpg"))

        col1, col2 = st.columns([1,2.025])
        col1.image(Image.open("images/t_2_5.jpg"))
        col1.image(Image.open("images/t_2_3.jpg"))
        col2.image(Image.open("images/t_2_1.jpg"), use_column_width=True)
      
        col1, col2 = st.columns([1.12,1])
        col1.image(Image.open("images/t_2_4.jpg"))
        col2.image(Image.open("images/t_2_2.jpg"))
      
    elif img == "images/topic_3.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)

        col1, col2 = st.columns([2.285,1])
        col1.image(Image.open("images/t_3_3.jpg"))
        col2.image(Image.open("images/t_3_1.jpg"))

        col1, col2, col3 = st.columns([1.05,1,1])
        col1.image(Image.open("images/t_3_2.jpg"))
        col2.image(Image.open("images/t_3_4.png"))
        col3.image(Image.open("images/t_3_5.png"))

    elif img == "images/topic_4.jpg":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1,1])
        col1.image(Image.open("images/t_4_1.jpg"), use_column_width=True)
        col2.image(Image.open("images/t_4_2.jpg"), use_column_width=True)
        st.image(Image.open("images/t_4_3.png"), use_column_width=True)

    elif img == "images/topic_5.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        st.image(Image.open("images/t_5_1.png"), use_column_width=True)

    elif img == "images/topic_6.jpg":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)

        col1, col2 = st.columns([1.54,1])
        with col1:
            col1.image(Image.open("images/t_6_1.jpg"))
            col_1, col_2 = st.columns([1.12,1])
            col_1.image(Image.open("images/t_6_3.jpg"))
            col_2.image(Image.open("images/t_6_4.jpg"))

        with col2:
            st.image(Image.open("images/t_6_6.jpg"))
            st.image(Image.open("images/t_6_5.jpg"))
            st.image(Image.open("images/t_6_2.jpg"))
       
    elif img == "images/topic_7.png":
        # CSS : Image
        st.markdown("""<style>img { border-radius: 20px;}</style>""", unsafe_allow_html=True)
        
        st.image(Image.open("images/t_7_2.png"), use_column_width=True)
        col1, col2 = st.columns([1.18,1])
        col1.image(Image.open("images/t_7_1.png"), use_column_width=True)
        col2.image(Image.open("images/t_7_3.png"), use_column_width=True)

elif st.session_state['index_page'] == 2:

    # -----> Marker Color 
    # 'beige', 'black', 'blue', 'cadetblue', 'darkblue', 'darkgreen', 'darkpurple', 'darkred', 'gray', 
    # 'green', 'lightblue', 'lightgray', 'lightgreen', 'lightred', 'orange', 'pink', 'purple', 'red', 'white'

    # map = folium.Map(location=[ave_lat, ave_lon], zoom_start=10, width="100%", height="100%")
    # f1 = folium.FeatureGroup("Vehicle 1")
    # folium.PolyLine(points, popup='<b>Path of Vehicle_1</b>', tooltip='Vehicle_1', color='#2980B9', weight=5).add_to(map)
    
    map = folium.Map(location=[8.997002687634067, 98.77581889750773], zoom_start=13.3, width="100%", height="100%")
    
    if st.session_state['trip'] == "ทริปครึ่งเดียว" or st.session_state['trip'] == "Half Day Trip":
        
        st.header("🧭 :green[โปรแกรมท่องเที่ยว ทริปครึ่งวัน]")

        # -----> Image position
        point_1 = get_img_as_base64("images/index_1.jpg")
        point_2 = get_img_as_base64("images/index_1.jpg")
        point_3 = get_img_as_base64("images/index_1.jpg")
        point_4 = get_img_as_base64("images/index_1.jpg")
        point_5 = get_img_as_base64("images/index_1.jpg")
        point_6 = get_img_as_base64("images/index_1.jpg")
        point_7 = get_img_as_base64("images/index_1.jpg")

        # -----> CSS : Button
        css = f"""<style>
        body {{
            margin: 0;
            height: 100%;
            background-image: url('data:image/png;base64,{point_1}');
            background-position: center;
            background-repeat: no-repeat;
            background-size: 100% 100%;
        }}

        *,
        *::before,
        *::after {{
        box-sizing: border-box;
        }}

        :root{{
            --bg-color: #454545;
        }}

        body {{
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        width: 100vw;
        height: 100vh;
        color: #ffffff;
        background-color: var(--bg-color);
        font-family: 'Maitree', serif;
        text-shadow: black
        }}

        h1{{
            font-size: 25px;
            font-weight: normal;
            text-shadow: -2px 0 black, 0 2px black, 2px 0 black, 0 -2px black
        }}

        .home-title span{{
            position: relative;
            overflow: hidden;
            display: block;
            line-height: 1.2;
        }}

        .home-title span::after{{
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 100%;
            height: 100%;
            background: white;
            animation: a-ltr-after 1s cubic-bezier(.77,0,.18,1) forwards;
            transform: translateX(-101%);
        }}

        .home-title span::before{{
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 100%;
            height: 100%;
            background: var(--bg-color);
            animation: a-ltr-before 1s cubic-bezier(.77,0,.18,1) forwards;
            transform: translateX(0);
        }}

        .home-title span:nth-of-type(1)::before,
        .home-title span:nth-of-type(1)::after{{
            animation-delay: 0.1s;
        }}

        .home-title span:nth-of-type(2)::before,
        .home-title span:nth-of-type(2)::after{{
            animation-delay: 0.12s;
        }}

        @keyframes a-ltr-after{{
            0% {{transform: translateX(-100%)}}
            100% {{transform: translateX(101%)}}
        }}

        @keyframes a-ltr-before{{
            0% {{transform: translateX(0)}}
            100% {{transform: translateX(200%)}}
        }}
        </style>"""

        ##### Half Day trip #####
        # A1 ----------> บ้านสวนกัญจรดา
        detail = f"""{css} <body> <center><h1 class="home-title"><span> บ้านสวนกัญจรดา </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=300, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([8.97164226197811, 98.83714420416014], icon=folium.Icon(color="red" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="บ้านสวนกัญจรดา").add_to(map)
        
        # B2 ----------> กลุ่มผ้าทอมือบ้านดชี่ยวหลาน
        detail = f"""{css} <body> <center><h1 class="home-title"><span> กลุ่มผ้าทอมือบ้านดชี่ยวหลาน </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=400, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([8.972084208287145, 98.84599565197693], icon=folium.Icon(color="blue" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="กลุ่มผ้าทอมือบ้านดชี่ยวหลาน").add_to(map)
        
        # B4 ----------> จุดชมวิวเขื่อน
        detail = f"""{css} <body> <center><h1 class="home-title"><span> จุดชมวิวเขื่อน </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=300, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([8.978806932251912, 98.82447589107123], icon=folium.Icon(color="darkblue" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="จุดชมวิวเขื่อน").add_to(map)
        
        # B5 ----------> ท่าเทียบเรือเขื่อนเชี่ยวหลาน
        detail = f"""{css} <body> <center><h1 class="home-title"><span> ท่าเทียบเรือเขื่อนเชี่ยวหลาน </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=400, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([8.977535661932436, 98.82050467559426], icon=folium.Icon(color="green" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="ท่าเทียบเรือเขื่อนเชี่ยวหลาน").add_to(map)
        
        # C1 ----------> เขาตาพัด
        detail = f"""{css} <body> <center><h1 class="home-title"><span> เขาตาพัด </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=300, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([9.013626145479003, 98.74467583599849], icon=folium.Icon(color="orange" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="เขาตาพัด").add_to(map)
        
        # C2 ----------> เขาสามเกลอ
        detail = f"""{css} <body> <center><h1 class="home-title"><span> เขาสามเกลอ </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=300, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([8.997424514651449, 98.70875600747672], icon=folium.Icon(color="cadetblue" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="เขาสามเกลอ").add_to(map)
        
        # C3 ----------> แพนางไพร
        detail = f"""{css} <body> <center><h1 class="home-title"><span> แพนางไพร </span></h1></center> </body>"""
        point = folium.IFrame(detail, width=300, height=200)
        popup = folium.Popup(point, max_width="auto")
        folium.Marker([9.007169792112235, 98.69600422245975], icon=folium.Icon(color="gray" ,icon="glyphicon glyphicon-flag"), popup=popup, tooltip="แพนางไพร").add_to(map)

        ##### PolyLine #####
        # Line : A1 -> B1
        folium.PolyLine(GPX("GPX/half day trip/A1_B2.gpx"), popup='', tooltip='', color='#CD3C28', weight=5).add_to(map)
        # Line : B2 -> B4
        folium.PolyLine(GPX("GPX/half day trip/B2_B4.gpx"), popup='', tooltip='', color='#38A9DB', weight=5).add_to(map)
        # Line : B4 -> B5
        folium.PolyLine(GPX("GPX/half day trip/B4_B5.gpx"), popup='', tooltip='', color='#0066A2', weight=5).add_to(map)
        
        line_1 = [[8.977535661932436, 98.82050467559426], [8.97664672883349, 98.80438846114797], [8.98518338535902, 98.78663555533123],
                  [9.005337475828775, 98.7665588150486], [9.011035953592158, 98.7579802701891], [9.013626145479003, 98.74467583599849]]
        
        line_2 = [[9.013626145479003, 98.74467583599849], [9.015917327539068, 98.74351786721083], [9.01679145303608, 98.7409733149574], 
                  [9.016427234336161, 98.73208582085486], [9.01966876783419, 98.72297706131624], [9.019996561751535, 98.7180723446766],
                  [9.0198508756056, 98.71663411949599], [9.018284745860932, 98.71538028215372], [9.0125088607388, 98.71160011658804],
                  [9.002274054139207, 98.70769109428569], [9.000730140747711, 98.70797432603273], [8.997424514651449, 98.70875600747672]]
        
        line_3 = [[8.997424514651449, 98.70875600747672], [8.997096644581802, 98.7082898812048], [8.997181662228302, 98.7077278508317],
                  [8.998125303540146, 98.70568746274704], [9.00044431387393, 98.7029359736714], [9.007169792112235, 98.69600422245975]]
        
        # Line : B5 -> C1
        folium.PolyLine(line_1, popup='', tooltip='', color='#71AF26', weight=5).add_to(map)
        # Line : C1 -> C2
        folium.PolyLine(line_2, popup='', tooltip='', color='#F0942F', weight=5).add_to(map)
        # Line : C2 -> C3
        folium.PolyLine(line_3, popup='', tooltip='', color='#426776', weight=5).add_to(map)
   
        map = st_folium(map, width='auto', returned_objects="last_object_clicked")

    elif st.session_state['trip'] == "ทริปหนึ่งวัน" or st.session_state['trip'] == "Two Day Trip":
        
        st.header("🧭 :green[โปรแกรมท่องเที่ยว ทริปหนึ่งวัน]")

        # A-1 ----------> บ้านสวนกัญจรดา
        folium.Marker([8.97164226197811, 98.83714420416014], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="บ้านสวนกัญจรดา").add_to(map)
        # A-2 ----------> บ้านน้ำขิง โฮมสเตย์
        folium.Marker([8.963414959513365, 98.84006403848186], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="บ้านน้ำขิง โฮมสเตย์").add_to(map)
        # A-3 ----------> ระเบียงไม้​ โฮมสเตย์​
        folium.Marker([8.963707207320072, 98.83895320248189], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ระเบียงไม้​ โฮมสเตย์​").add_to(map)

        # B-1 ----------> อชิลฟาร์ม
        folium.Marker([8.9741592, 98.8347331], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="อชิลฟาร์ม").add_to(map)
        # B-2 ----------> กลุ่มผ้าทอมือบ้านดชี่ยวหลาน
        folium.Marker([8.972084208287145, 98.84599565197693], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="กลุ่มผ้าทอมือบ้านดชี่ยวหลาน").add_to(map)
        # B-3 ----------> ลานพระแทน
        folium.Marker([8.97555234016401, 98.84349346285818], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ลานพระแทน").add_to(map)
        # B-4 ----------> จุดชมวิวเขื่อน
        folium.Marker([8.978806932251912, 98.82447589107123], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="จุดชมวิวเขื่อน").add_to(map)
        # B-5 ----------> ท่าเทียบเรือเขื่อนเชี่ยวหลาน
        folium.Marker([8.977535661932436, 98.82050467559426], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ท่าเทียบเรือเขื่อนเชี่ยวหลาน").add_to(map)
        
        # C-1 ----------> เขาตาพัด
        folium.Marker([9.013626145479003, 98.74467583599849], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="เขาตาพัด").add_to(map)
        # C-2 ----------> เขาสามเกลอ
        folium.Marker([8.997424514651449, 98.70875600747672], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="เขาสามเกลอ").add_to(map)
        # C-3 ----------> แพนางไพร
        folium.Marker([9.007169792112235, 98.69600422245975], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="แพนางไพร").add_to(map)
        # C-4 ----------> ควนคางคก
        folium.Marker([9.022635856761292, 98.70684102815568], icon=folium.Icon(color="orange"), popup="Thailand", tooltip="ควนคางคก").add_to(map)

        map = st_folium(map, width='auto', returned_objects="last_object_clicked")
        