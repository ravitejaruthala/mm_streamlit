# support_file.py
import streamlit as st
import time
import sqlite3
import secrets

streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

def get_db_connection():
    conn = sqlite3.connect('meeting_notes.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unique_code TEXT NOT NULL,
            author_name TEXT NOT NULL,
            author_email TEXT NOT NULL,
            meeting_date TEXT NOT NULL,
            meeting_agenda TEXT NOT NULL,
            meeting_notes TEXT NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def page_configuration(title_parameter, icon_parameter):
    st.set_page_config(page_title=title_parameter, page_icon=icon_parameter)
    st.sidebar.header(title_parameter)
    st.markdown(streamlit_style, unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align: center;'>{title_parameter}</h1>", unsafe_allow_html=True)

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
    search_container = st.container()
    selected = search_container.text_input("**Enter the Meeting ID**", placeholder="Search here...")
    if search_container.button("Fetch Meeting notes"):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM notes WHERE unique_code = ?", (selected,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            st.write(dict(result))
        else:
            st.write("No meeting found with that ID.")

def stream_data_content(subheader_parameter, content_parameter):
    st.subheader(subheader_parameter)
    for word in content_parameter.split(" "):
        yield word + " "
        time.sleep(0.03)

def generate_unique_code():
    return secrets.token_hex(8)  # 8 bytes = 16 characters in hexadecimal

def save_meeting_notes(author_name, author_email, meeting_date, meeting_agenda, meeting_notes):
    unique_code = generate_unique_code()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notes (unique_code, author_name, author_email, meeting_date, meeting_agenda, meeting_notes) VALUES (?, ?, ?, ?, ?, ?)",
        (unique_code, author_name, author_email, meeting_date, meeting_agenda, meeting_notes)
    )
    conn.commit()
    cur.close()
    conn.close()

def fetch_meeting_notes(unique_code):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE unique_code = ?", (unique_code,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def update_meeting_notes(unique_code, author_name, author_email, meeting_date, meeting_agenda, meeting_notes):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE notes SET author_name=?, author_email=?, meeting_date=?, meeting_agenda=?, meeting_notes=? WHERE unique_code=?",
        (author_name, author_email, meeting_date, meeting_agenda, meeting_notes, unique_code)
    )
    conn.commit()
    cur.close()
    conn.close()
