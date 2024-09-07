import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Suman Thapa Magar", anchor=False)
    st.write(
        "Full Stack Developer / Software Engineer with knowledge in multiple Techstack."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 6 Years experience building robust application in web and mobile
    - Strong hands-on experience and knowledge in Python, PHP and JavaScript
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Backend: Python, PHP, NodeJS, DOTNET
    - Frontend: React, JavaScript/TypeScript, Vue.js
    - Databases: Postgres, MySQL, SQLServer
    """
)
