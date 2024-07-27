import streamlit as st
from streamlit_option_menu import option_menu

def app():
    st.image("image/Header1.png")
    st.header("Welcome to Vike's Page!", divider="blue")
    st.write("Vike adalah sebuah alat penunjang mata pembelajaran fisika yang dibuat oleh team Galaxy Tab A28. Alat ini merupakan inovasi yang dicipatakan setelah mengikuti rangkaian pembelajaran bersama Samsung Innovation Campus.")
    st.write("Pilih Menu di bawah ini untuk mengenal Vike lebih jauh!")

    ##with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Description","Purposes", "Feature"],
        icons=['book', 'search','menu-up'],
        default_index=0,
        orientation="horizontal",
        styles={
            "Container": {'Padding': '3!important', 'background-color':None},
        'icon':{'color':'white', 'font-size':'20px'},
        'nav-link': {'color':'white', 'font-size': '18px', 'text-allign': 'left', 'margin': '0px','--hover-color':'#ffff00'},
        'nav-link-selected': {'background-color': 'blue'},}
    )
    
    if selected == "Description":
        st.title(f"So, What Is VIKE?")
        st.image("image/viketrophy.jpg", "Alat Vike")
        st.write("VIKE adalah alat  peraga fisika untuk menentukan percepatan sudut pada gerak benda di bidang miring yang dibuat menggunakan akrilik dan setiap titik dipasang sensor proximity untuk mengukur waktu gerak benda berupa bola. Bola akan bergerak di bidang miring diatas akrilik dengan sudut kemiringan yang bervariasi. Saat melalui sensor, waktu benda menempuh jarak tertentu dapat diketahui sehingga data yang dihasilkan adalah waktu sebagai fungsi jarak. Setelah data didapatkan, data akan dianalisis menggunakan analisis grafik linear pada spreadsheet dari analisis grafik akan muncul gradien garis sebagai parameter percepatan linear yang dapat diketahui juga kecepatan di titik-titik yang diinginkan.")
        st.write("VIKE dibuat dapat memberikan manfaat di bidang pendidikan karena  dapat digunakan sebagai alat praktikum penentuan percepatan benda yang menggelinding bidang miring, dari fenomena fisika ini diharapkan guru dapat menggunakan alat tersebut untuk praktikum dinamika translasi dan rotasi dengan panduan LKPD yang terbimbing.")
    if selected == "Purposes":
        st.title(f"The Reason Behind")
        col1, col2 = st.columns(2)
        col1.image("image/Desain Atas.jpg", "Desain awal Vike")
        col2.image("image/Desain samping.jpg", 'Desain Awal Vike')
        st.write("Team kami berisi anak - anak yang penuh antusias dalam belajar. Kami selalu ingin tahu lebih dalam mengenai ilmu yang telah kami dapatkan. Termasuk materi GLBB pada pembelajaran fisika. Namun kami belum mendapatkan suatu pembuktian praktik realistis bagaimana rumus rumus GLBB berlaku. Banyak pertanyaan yang muncul, seperti apakah benar bahwa percepatan bola memiliki hubungan dengan diketahuinya waktu gerak bola?")
        st.write("Oleh karena itulah kami menciptakan vike! Dengan vike kami mendapatkan pembuktian realistis bagaimana mencari percepatan suatu bola.")
        st.write("Salah satu guru fisika sekolah kami juga mengatakan bahwa, dengan dibuatnya alat ini akan memberikan manfaat dibidang pendidikan. Hal ini dikarenakan alat ini nantinya dapat digunakan sebagai alat praktikum penentuan percepatan benda. Dengan fenomena ini guru fisika kami mengharapkan alat ini dapat digunakan oleh berbagai guru untuk praktikum fisika dengan panduan LKPD yang tepimping")
    if selected == "Feature":
        st.title(f"What can users do on Vike?")
        st.write("Target pengguna alat Vike ini adalah **Guru** dan **Siswa**.")
        col1, col2 = st.columns(2)
        col1.title(":male-teacher: Guru")
        col1.write("Sesuai dengan latar belakang permasalahan dan solusi yang dibuat, guru fisika menjadi target pengguna utama dari produk kami. Dengan menggunakan alat ini, guru akan jauh lebih mudah menjelaskan konsep materinya.")
        col2.title(":female-student: Siswa")
        col2.write("Salah satu penerapan dari alat kami adalah sebagai bahan praktik siswa dalam membuktikan materi GLBB dan tumbukan secara real time sehingga membuat materi fisika jauh lebih menyenangkan")
        st.title("Fitur Produk")
        st.write("Fitur produk yang Vike sajikan berupa :")
        st.write("⏺Sensor yang dapat membaca catatan waktu saat bola melintas")
        st.write("⏺Spreadsheets yang dapat menghasilkan data berupa waktu saat bola melintas")
        st.write("⏺Memastikan data yang dihasilkan akurat dan memastikan waktu yang tercatat sesuai ")
