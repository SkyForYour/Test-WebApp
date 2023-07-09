import base64
import os

from PIL import Image 
from io import BytesIO

import streamlit as st

from streamlit_toggle import st_toggle_switch
from PIL import Image

def App():

    if 'language' not in st.session_state: 
        st.session_state['language'] = 0

    # -----> Thai / English
    st.session_state['language'] = st_toggle_switch(
        label="ภาษาไทย / ภาษาอังกฤษ", key="switch_1",
        default_value=False, label_after=True,
        inactive_color="#D3D3D3",  active_color="#11567f", track_color="#29B5E8",  
    )
    
    col1, col2, col3 = st.columns([0.1,0.8,0.1])
    col2.image((Image.open("images/logo_edit.png")), width=230)

    if st.session_state['language'] == 0:
        
        # -----> HTML + CSS
        css_button = """<style>
            .stButton > button {
            width: 100%;
            background-color: #E8F8F5;
            border-radius: 100px;
            box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset,
                        rgba(44, 187, 99, .15) 0 1px 2px,
                        rgba(44, 187, 99, .15) 0 2px 4px,
                        rgba(44, 187, 99, .15) 0 4px 8px,
                        rgba(44, 187, 99, .15) 0 8px 16px,
                        rgba(44, 187, 99, .15) 0 16px 32px;
            color: #454545;
            cursor: pointer;
            display: inline-block;
            padding: 15px 23%;
            text-align: center;
            transition: all 250ms;
            border: 1;
            font-size: 100%;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            }

            .stButton > button:hover {
            box-shadow: rgba(44,187,99,.35) 0 -25px 18px -14px inset,
                    rgba(44,187,99,.25) 0 1px 2px,rgba(44,187,99,.25) 0 2px 4px,
                    rgba(44,187,99,.25) 0 4px 8px,rgba(44,187,99,.25) 0 8px 16px,
                    rgba(44,187,99,.25) 0 16px 32px;
            transform: scale(1.05) rotate(-1deg);
            }
            </style>"""
        st.markdown(css_button, unsafe_allow_html=True)
        
        if st.button("ชุมชนบ้านเชี่ยวหลาน"):
            st.session_state['index_page'] = 0
        if st.button("แนะนำแหล่งท่องเที่ยว"):
            st.session_state['index_page'] = 1
        if st.button("โปรแกรมการท่องเที่ยว"):
            st.session_state['index_page'] = 2

        if st.session_state['index_page'] == 2:

            st.session_state['trip'] = st.selectbox(
            ' 🚍⠀เลือกทริปการท่องเที่ยว',('ทริปครึ่งเดียว', 'ทริปหนึ่งวัน'))
            
    elif st.session_state['language'] == 1:

        # -----> HTML + CSS
        css_button = """<style>
            .stButton > button {
            width: 100%;
            background-color: #E8F8F5;
            border-radius: 100px;
            box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset,
                        rgba(44, 187, 99, .15) 0 1px 2px,
                        rgba(44, 187, 99, .15) 0 2px 4px,
                        rgba(44, 187, 99, .15) 0 4px 8px,
                        rgba(44, 187, 99, .15) 0 8px 16px,
                        rgba(44, 187, 99, .15) 0 16px 32px;
            color: #454545;
            cursor: pointer;
            display: inline-block;
            padding: 15px 18.5%;
            text-align: center;
            transition: all 250ms;
            border: 1;
            font-size: 100%;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            }

            .stButton > button:hover {
            box-shadow: rgba(44,187,99,.35) 0 -25px 18px -14px inset,
                    rgba(44,187,99,.25) 0 1px 2px,rgba(44,187,99,.25) 0 2px 4px,
                    rgba(44,187,99,.25) 0 4px 8px,rgba(44,187,99,.25) 0 8px 16px,
                    rgba(44,187,99,.25) 0 16px 32px;
            transform: scale(1.05) rotate(-1deg);
            }
            </style>"""
        st.markdown(css_button, unsafe_allow_html=True)

        if st.button("Ban Chiew Lan Community"):
            st.session_state['index_page'] = 0
        if st.button("Recommended attractions"):
            st.session_state['index_page'] = 1
        if st.button("Cheow Lan Travel Program"):
            st.session_state['index_page'] = 2
        
        if st.session_state['index_page'] == 2:
            st.session_state['trip'] = st.selectbox(
            ' 🚍⠀Choose a trip',('Half Day Trip', 'One Day Trip'))
            
    st.caption("### ⠀:green[─────────⠀**Streamlit**⠀─────────]⠀")
