import streamlit as st 
import PIL 
import numpy as np 
from src.ul.base_layout import style_background_dashboad,style_base_layout
from  src.components.header import header_dashbord
from src.components.footer import footer_dashbord
from PIL import Image


def student_screen():


    style_background_dashboad()
    style_base_layout()

    c1,c2 =st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
         header_dashbord()
    with c2:
        if st.button("Go Back to Home",type="secondary",key='loginbackbtu',shortcut="control+backspace"):
             st.session_state["login_type"] =None
             st.rerun()
    
    st.header("login using FaceID",text_alignment="center")
    st.space("medium")

    photo_source = st.camera_input("position your face in the center!")

    if photo_source:
         np.array(Image.open(photo_source))
    footer_dashbord()
