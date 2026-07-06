import streamlit as st 
from src.ul.base_layout import style_background_dashboad,style_base_layout
from  src.components.header import header_dashbord
from src.components.footer import footer_dashbord

def teacher_screen():

    style_background_dashboad()
    style_base_layout()
    
   # teacher_screen_register()

    if "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
         teacher_screen_login()
    elif st.session_state.teacher_login_type =="register":
         teacher_screen_register()
         

 
def teacher_screen_login():
    c1,c2 =st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
         header_dashbord()
    with c2:
        if st.button("Go Back to Home",type="secondary",key='loginbackbtu',shortcut="control+backspace"):
             st.session_state["login_type"] =None
             st.rerun()

    st.header("login using Password",text_alignment="center")
    st.space("medium")
    teacher_username =st.text_input("Enter Username",placeholder="Teacher user name")
    teacher_password =st.text_input("Enter Password",type="password",placeholder="password")
    st.divider()

    c3,c4 =st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c3:
         st.button("Login",icon=":material/passkey:",type="primary",key="logintoteacher",shortcut="control+enter",width="stretch")
    with c4:
        if st.button("Register Instead",icon=":material/passkey:",type="primary",key="registerinstead",width="stretch"):
             st.session_state.teacher_login_type ='register'
             st.rerun()

    footer_dashbord()


def teacher_screen_register():
    c1,c2 =st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
         header_dashbord()
    with c2:
        if st.button("Go Back to Home",type="secondary",key='loginback',shortcut="control+backspace"):
             st.session_state["login_type"] =None
             st.rerun()


             

    st.header("Create Teacher Profile")

    st.space("small")
    teacher_username =st.text_input("Enter Username",placeholder="Teacher user name")
    teacher_name =st.text_input("Enter Name",placeholder="Teacher Name")
    teacher_password =st.text_input("Enter Password",type="password",placeholder="password")
    teacher_password_confirm =st.text_input("Confirm your Password",type="password",placeholder="password")
    st.divider()

    c3,c4 =st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c3:
         st.button("Register Now",icon=":material/passkey:",type="primary",key="registernow",shortcut="control+enter",width="stretch")
    with c4:
         if st.button("login Instead",icon=":material/passkey:",type="primary",key="loginnow",width="stretch"):
              st.session_state.teacher_login_type ="login"

    footer_dashbord()