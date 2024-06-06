import streamlit as st
import time

streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""" 

def page_configuration(title_parameter, icon_parameter):
    st.set_page_config(page_title= title_parameter, page_icon= icon_parameter)
    st.sidebar.header(title_parameter)
    st.markdown(streamlit_style, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>"+title_parameter+"</h1>", unsafe_allow_html=True)
    
def reset_value():
    st.session_state.author_name = None
    st.session_state.author_email = None
    st.session_state.meeting_agenda = None
    st.session_state.meeting_notes = None
    st.toast('Done with the reset!', icon="🧹")
    
def input_validation():
    st.toast('Submitted successfully!', icon="✅")
    st.balloons()
    st.toast('You will receive an email shortly!', icon="✉️")
    
def display_search_container():
    search_container = st.container(border=True)
    selected = search_container.text_input("**Enter the Meeting ID**", placeholder="Search here...")
    searched = search_container.button("Fetch Meeting notes")
    
def stream_data_content(subheader_parameter, content_parameter):
    st.subheader(subheader_parameter)
    for word in content_parameter.split(" "):
        yield word + " "
        time.sleep(0.03)