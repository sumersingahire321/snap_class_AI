import streamlit as st

def header_home():
    logo_url = "https://cdn-icons-png.flaticon.com/512/2940/2940653.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column;align-items:center; justify-content:center;margin-bottom:30px">
                <img src="{logo_url}" style="height:100px;"/>
                <h1 style ="text-align:center; color:#FFFF00">SNAP<br/>CLASS</h1>
        </div>

   """,unsafe_allow_html=True)
  