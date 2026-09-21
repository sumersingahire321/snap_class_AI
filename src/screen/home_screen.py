import streamlit as st 
from  src.components.header import header_home
from src.ul.base_layout import style_backdround_home,style_base_layout


def home_screen():
   
    style_base_layout()
    header_home()
    style_backdround_home()
    
    

    
    col1,col2 = st.columns(2,gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://static.vecteezy.com/system/resources/thumbnails/045/546/274/small/boy-wear-graduation-hat-and-holding-book-3d-free-png.png",width=86)
        if st.button("Student Portal",type="primary",width="content",icon=':material/arrow_outward:',icon_position="right"):
            st.session_state["login_type"] = "student"
            st.rerun()
    
    with col2:
        st.header("I'm Teacher")
        st.image("https://static.vecteezy.com/system/resources/thumbnails/059/919/000/small/impressive-modern-teacher-pointing-at-chalkboard-professional-free-png.png",
                 width=120)
        if st.button("Teacher Portal",type="primary",width="content",icon=':material/arrow_outward:',icon_position="right"):
           st.session_state["login_type"] = "teacher"
           st.rerun()
    
