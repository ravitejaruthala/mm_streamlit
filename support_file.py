import streamlit as st

streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""" 

def reset_value():
    st.session_state.author_name = None
    st.session_state.author_email = None
    st.session_state.meeting_agenda = None
    st.session_state.meeting_notes = None
    
def input_validation():
    reset_value()