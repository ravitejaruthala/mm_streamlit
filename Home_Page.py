import streamlit as st
from support_file import *

import streamlit as st
from support_file import initialize_db

initialize_db()


summary = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

page_configuration("Minutes of Meeting", "📋")
st.write(stream_data_content("Web App Summary:", summary))
st.write(stream_data_content("Instructions:", summary)) 
st.write(stream_data_content("More Information:", summary))