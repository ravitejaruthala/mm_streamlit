import streamlit as st
from support_file import *

initialize_db()
summary_content = """
Welcome to MinuteMate!

Capture and organize your meeting notes effortlessly with our intuitive platform. Never miss a detail again!

Whether you're in a brainstorming session, team meeting, or client discussion, this application is your trusted companion for effective note-taking. Get started now and experience seamless productivity.

Happy note-taking!
"""

instructions_content = """
To ensure that we record your meeting notes promptly, please follow these steps:
1. Provide your full name as it will be mentioned in your meeting notes.
2. Ensure that the email account is active and can receive messages.
3. Carefully type your email address to avoid common mistakes, such as missing the "@" symbol or adding unnecessary spaces.
4. Double-check for errors that might prevent delivery, such as extra periods or incorrect domain names.
5. Try to specify the meeting agenda such that it summarizes the meeting purpose.
6. Keep note of the factual data, meeting conclusions and other important details in the Minutes of Meeting text data field.
"""
information_content = """
We understand how important your privacy is, and we want to assure you that your data is treated with the utmost respect. Here are the key points regarding your data when using our application:

***No Commercial Use:*** Your data will never be used for commercial purposes. We do not sell, rent, or share your data with any other entities for marketing or any other commercial activities.

***Privacy by Design:*** Our app is designed with your privacy in mind. Any data processed during your session is used solely to provide the service you requested and nothing else.

Thank you for trusting MinuteMate. Your privacy and trust are our top priorities.

"""

page_configuration("MinuteMate", "📋")
st.write(stream_data_content("About MinuteMate:", summary_content))
st.write(stream_data_content("Instructions:", instructions_content)) 
st.write(stream_data_content("More Information:", information_content))