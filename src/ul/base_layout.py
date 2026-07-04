import streamlit as st 

def style_backdround_home():
    st.markdown("""
        <style>
            .stApp{
                background: linear-gradient(to bottom, #33cc33 0%, #ffffff 80%) !important;
                }
            .stApp div[data-testid="stColumn"]{
                background-color:#E0E3FF !important;
                padding:1.3rem !important;
                border-radius:3.5rem !important;}
        </style>
                
                """,unsafe_allow_html=True)
    
'''def style_background_dashboad():
    st.markdown("""
        <style>
            .stApp{
                background : #ffffb3 !important;
                }
        </style>
                
                """,unsafe_allow_html=True)'''
    

def style_base_layout():
        st.markdown("""
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Changa+One:ital@0;1&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');
        
        /*Hide Streamlit menu, header and footer*/
            #MainMenu,
            header,
            footer {
                visibility: hidden;
            }

        /* Reduce top padding */
            .block-container {
                padding-top:1.5rem !important;
            }
            
            h1{
                    font-family: "Changa One", sans-serif !important;
                    font-size: 3.5rem !important;
                    line-height:0.9 !important;
                    margin-bottom:0rem !important; 
                }
            h2{
                    font-family: "Changa One",sans-serif !important;
                    font-size: 3.5rem !important;
                    line-height:0.9 !important;
                    margin-bottom:0rem !important; 
                }
            h3, h4, p {
                    font-family:"Outfit",sans-serif;
                    }
             button{
                    border-radius:1.5rem !important;
                    background: #EE82EE !important;
                    color: white !important;
                    padding:10px 20px !important;
                    border: none !important;
                    transition: transform 0.25 ease-in-out !important;
                    }
            button[kind="secomdary"]{
                    border-radius:1.5rem !important;
                    background: #FF69B4 !important;
                    color: white !important;
                    padding:10px 20px !important;
                    border: none !important;
                    transition: transform 0.25 ease-in-out !important;
                    }
             button[kind="tertiary"]{
                    border-radius:1.5rem !important;
                    background: #7CFC00 !important;
                    color: white !important;
                    padding:10px 20px !important;
                    border: none !important;
                    transition: transform 0.25 ease-in-out !important;
                    }
            button:hover{
                    transform :scale(1.05)} 
        </style>
                 """
                    , unsafe_allow_html=True)
        
