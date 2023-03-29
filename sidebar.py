import streamlit as st
from PIL import Image
# from streamlit_toggle import st_toggle_switch

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
        
        if st.button("**ชุมชนบ้านเชี่ยวหลาน**"):
            st.session_state['index_page'] = 0
        if st.button("**แนะนำแหล่งท่องเที่ยว**"):
            st.session_state['index_page'] = 1
        if st.button("**โปรแกรมการท่องเที่ยว**"):
            st.session_state['index_page'] = 2

        if st.session_state['index_page'] == 2:
            st.write('')
            st.session_state['trip'] = st.selectbox(
            ' 🚍⠀เลือกทริปการท่องเที่ยว',
            ('ทริปวันเดียว', 'ทริปสองวัน', 'อื่น ๆ⠀.⠀.'))
            
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

        if st.button("**Ban Chiew Lan Community**"):
            st.session_state['index_page'] = 0
        if st.button("**Recommended attractions**"):
            st.session_state['index_page'] = 1
        if st.button("**Cheow Lan Travel Program**"):
            st.session_state['index_page'] = 2
        
        if st.session_state['index_page'] == 2:
            st.write('')
            st.session_state['trip'] = st.selectbox(
            ' 🚍⠀Choose a trip',
            ('One Day Trip', 'Two Day Trip', 'Other⠀.⠀.'))
            
    st.write(''), st.write('')
    # col1, col2 = st.columns(2)
    # with col1:
    st.caption("### ⠀:green[─────────⠀**Streamlit**⠀─────────]⠀")

    # with col2:
    #     st.session_state['language'] = st_toggle_switch(
    #         label="𝐓𝐇𝐀𝐈 / 𝐄𝐍𝐆", key="switch_1",
    #         default_value=False, label_after=False,
    #         inactive_color="#D3D3D3",  # optional
    #         active_color="#11567f",  # optional
    #         track_color="#29B5E8",  # optional
    #     )
