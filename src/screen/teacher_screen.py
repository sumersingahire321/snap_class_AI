import streamlit as st 
from src.ul.base_layout import style_background_dashboad,style_base_layout
from  src.components.header import header_dashbord
from src.components.footer import footer_dashbord
from src.database.db import check_teacher_exists,create_teacher,teacher_login

def teacher_screen():

    style_background_dashboad()
    style_base_layout()
    
   # teacher_screen_register()

    if "teacher_data" in st.session_state:
         teacher_dashboard()
    elif"teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
         teacher_screen_login()
    elif st.session_state.teacher_login_type =="register":
         teacher_screen_register()
         

def teacher_dashboard():
     teacher_data = st.session_state.teacher_data
     st.header(f"Welcome, {teacher_data['name']}")

def login_teacher(username,password):
     if not username or not password:
          return False

     teacher = teacher_login(username,password)

     if teacher:
          st.session_state.user_role ="teacher"
          st.session_state.teacher_data = teacher
          st.session_state.is_logged_in = True
          return True

     return False


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
          if st.button("Login",icon=":material/passkey:",type="primary",key="logintoteacher",shortcut="control+enter",width="stretch"):
               if login_teacher(teacher_username,teacher_password):
                  st.toast("Wellcome Back!",icon="👋")
                  import time
                  time.sleep(2)
                  st.rerun()
               else:
                    st.error("Invalid username and Password combo!")
                  
                         
    with c4:
        if st.button("Register Instead",icon=":material/passkey:",type="primary",key="registerinstead",width="stretch"):
             st.session_state.teacher_login_type ='register'
             st.rerun()

    footer_dashbord()

def register_teacher(teacher_name,teacher_username,teacher_password,teacher_password_confirm):
     if not teacher_username or not teacher_name or not teacher_password:
          return False,"All Fields are required!"
     if check_teacher_exists(teacher_username):
          return False,"Username already taken"
     if teacher_password != teacher_password_confirm:
          return False ,"Password do not match"
     try:
          create_teacher(teacher_username,teacher_password,teacher_name)
          return True,"Sucessfuly Created! Login Now"
     except Exception as e:
          return False,"Unexpected Error!"

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
         if st.button("Register Now",icon=":material/passkey:",type="primary",key="registernow",shortcut="control+enter",width="stretch"):
               success, message = register_teacher(teacher_name,teacher_username,teacher_password,teacher_password_confirm)
               if success:
                   st.success(message)
                   import time
                   time.sleep(2)
                   st.session_state.teacher_login_type = "login"
                   st.rerun()
               else:
                    st.error(message)
                   
    with c4:
         if st.button("login Instead",icon=":material/passkey:",type="primary",key="loginnow",width="stretch"):
              st.session_state.teacher_login_type ="login"

    footer_dashbord()