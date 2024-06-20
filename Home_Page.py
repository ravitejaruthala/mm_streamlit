import streamlit as st
from support_file import *

import streamlit as st
from support_file import initialize_db

initialize_db()


summary = """
Welcome to MinuteMate!

Capture and organize your meeting notes effortlessly with our intuitive platform. Never miss a detail again!

Whether you're in a brainstorming session, team meeting, or client discussion, this application is your trusted companion for effective note-taking.

Get started now and experience seamless collaboration and productivity.

Happy note-taking!
"""

page_configuration("MinuteMate", "📋")
st.write(stream_data_content("Web App Summary:", summary))
st.write(stream_data_content("Instructions:", summary)) 
st.write(stream_data_content("More Information:", summary))