import streamlit as st

def app():
    st.image("image/header3.png")
    st.header("Our Gallery!", divider='blue')
    col1, col2, col3= st.columns(3)

    col2.image("image/Tampak Atas.jpg", caption='Vike-Tampak Atas')
    col2.image("image/Desain Atas.jpg", "Desain awal bagian atas")
    col2.image("image/viketrophy.jpg", "Vike-Tampak Depan")

    col1.image("image/Tampak Samping (1).jpg", caption='Vike-Tampak Samping')
    col1.image("image/Desain samping.jpg", "Desain Awal bagian samping")
    col1.image("image/WhatsApp Image 2024-07-27 at 10.20.56 PM (1).jpeg", "Team belanja membeli alat dan bahan")

    col3.image("image/Tampak Samping.jpg", caption='Vike-Tampak Samping')
    col3.image("image/WhatsApp Image 2024-07-27 at 10.20.56 PM.jpeg", "Proses Pembuatan")
