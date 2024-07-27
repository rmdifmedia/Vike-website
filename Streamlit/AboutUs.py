import streamlit as st
import streamlit.components.v1 as components

def app():
    st.image("image/header2.png")
    st.header("Meet The Team!", divider='blue')

    col1, col2, col3, col4 = st.columns(4)

    col1.subheader("Aisyah", divider='blue')
    col1.image("image/aisweb.jpg")
    col1.write("Siti Aisyah, biasa dikenal sebagai Aisyah. Ia adalah *Software Engineer* serta *Creative Design* pada project ini.")

    col2.subheader("Rafa", divider='blue')
    col2.image("image/rafaweb.jpg")
    col2.write("Rafa Aaliyah Eka Ramadhani, biasa dikenal sebagai Rafa Ia adalah *Mechanical Engineer* pada project ini.")

    col3.subheader("Nadia", divider='blue')
    col3.image("image/nadiaweb.jpg")
    col3.write("Nadia Salsabila Bustomy, biasa dikenal sebagai Nadia. Ia adalah *Mechanical Engineer* pada project ini.")

    col4.subheader("Raya", divider='blue')
    col4.image("image/rayaweb.jpg")
    col4.write("Raya Medina Farelin, biasa dikenal sebagai Raya. Ia adalah *Software Engineer* serta *Creative Design* pada project ini.")




