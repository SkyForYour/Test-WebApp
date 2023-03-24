import streamlit as st

from PIL import Image 
from io import BytesIO

def App():
    
    logo = Image.open("images/logo_edit.png")
    st.image(logo, use_column_width=True)
    
    if st.session_state['language'] == 0:
        
        st.markdown("## ⠀⠀:green[ยินดีต้อนรับสู่บ้านเชี่ยวหลาน]⠀⠀")
        # -----> HTML + CSS
        css_button = """<style>
        .stButton > button {
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
        padding: 15px 21.05%;
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

        if st.button("**⠀ชุมชนบ้านเชียวหลาน⠀**"):
            st.session_state['index_page'] = 0
        if st.button("**แนะนำแหล่งท่องเที่ยวบ้านเชี่ยวหลาน**"):
            st.session_state['index_page'] = 1
        if st.button("**โปรแกรมการท่องเที่ยวบ้านเชี่ยวหลาน**"):
            st.session_state['index_page'] = 2
    
    elif st.session_state['language'] == 1:

        st.markdown("## ⠀⠀:green[Welcome to Baan Cheow Lan]⠀⠀")    
        # -----> HTML + CSS
        css_button = """<style>
        .stButton > button {
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
        padding: 15px 15.8%;
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

        if st.button("**⠀Ban Chiew Lan Community⠀**"):
            st.session_state['index_page'] = 0
        if st.button("**Introducing Ban Chiew Lan tourist attractions**"):
            st.session_state['index_page'] = 1
        if st.button("**Ban Chiew Lan Travel Program**"):
            st.session_state['index_page'] = 2

    st.write(''), st.write('')
    st.caption("### \- :green[**Streamlit 🌏 ⠀**]")
