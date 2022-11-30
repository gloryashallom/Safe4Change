from msilib import add_data
import streamlit as st
import os
from email.message import EmailMessage
import ssl 
import smtplib as s
import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()
from PIL import Image 
st.video("avoskin waste4change.mp4")

col1, col2 = st.columns(2)
with col1:
    st.write("# Love Avoskin Love Earth ")
    st.write("Program ini merupakan salah satu wujud komitmen Avoskin terhadap planet untuk pelestarian lingkungan. Kolaborasi atau kerjasama antara Avoskin dengan Safe ini mengajak pelanggan untuk peduli terhadap isu mengenai sampah dengan mengembalikan kemasan yang tidak terpakai agar dapat didaur ulang ataupun dikelola dengan bijaksana.")
with col2:
    st.write("")
    st.image("pict 1.jpg")
st.header("Kemasan Bekas yang Diterima")
st.write("Avoskin menerima pengembalian semua jenis kemasan bekas pakai produk Avoskin meliputi kemasan kardus, botol kaca, botol plastik, dan kemasan bekas sheet mask. Reward yang akan Kamu dapat bergantung dengan banyaknya botol kaca dan botol plastik yang kamu kembalikan.")
st.image("pict 2.jpg")
st.header("Cara Mengikuti Program")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("Daftarkan Diri")
    st.image("sign-in-1.jpg")
    st.write("Klik setor sekarang untuk daftarkan diri kamu")
with col2:
    st.subheader("Pilah & Kirim Kemasan")
    st.image("medicine-1.jpg")
    st.write("Pilah kemasan bekas Avoskin, bersihkan, bungkus dalam paket dan kirimkan ke mitra Safe terdekat")
with col3: 
    st.subheader("Konfirmasi Paket")
    st.image("packaging-1.jpg")
    st.write("Setelah paketmu diterima oleh Mitra Daur Ulang Safe, kamu akan mendapatkan notifikasi melalui akunmu")
with col4:
    st.subheader("Penukaran Reward")
    st.image("gift-1.jpg")
    st.write("Voucher dapat ditukarkan di website Avoskin dengan klik Redeem Sekarang")
result = st.button("Daftar Sekarang")

if result:
    st.subheader("Data Diri")
    st.caption("Silahkan lengkapi data berikut")
    with st.form(key="Data Diri"):
        Nama=st.text_input("Nama")
        choice=st.selectbox("Jenis Kelamin",["Laki-Laki","Perempuan"])
        Alamat=st.text_input("Alamat")
        Email=st.text_input("Email")
        Telepon=st.text_input("No Telepon")
        submission = st.form_submit_button(label="Submit")
    if submission== True:
            add_data(Nama, choice, Alamat, Email, Telepon)
            st.success("Successfully submitted")

def addData(a,b,c,d,e):
    cur.execute("""CREATE TABLE IF NOT EXISTS clg_form(NAME TEXT(50), CHOICE TEXT(50), ALAMAT TEXT(50), EMAIL TEXT(50), TELEPON TEXT(50))""")
    cur.execute("INSERT INTO clg_form VALUES (?,?,?,?,?)",(a,b,c,d,e))
    conn.commit()
    conn.close()
    st.success("Successfully submitted")

st.write("https://wa.me/message/UVY3WF5J65XTC1 ")
        
st.header("Klaim Hadiah")
st.write ("Kembalikan kemasan bekas pakai Avoskin dan klaim hadiahmu")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("1-4 Kemasan Botol")
    st.image("VOC 1.jpg")
    st.write("Setiap pengembalian kemasan bekas pakai Avoskin sebanyak 1-4 botol, kamu akan mendapatkan voucher discount dengan minimal purchase sebesar 199K")
with col2:
    st.header("5-9 Kemasan Botol")
    st.image ("VOC 2.jpg")
    st.write("Setiap pengembalian kemasan bekas pakai Avoskin sebanyak 5-9 botol kamu dapat memilih salah satu gift berupa produk Avoskin worth up to IDR 100K")
with col3: 
    st.header("10+ Kemasan Botol")
    st.image ("VOC 3.jpg")
    st.write("Setiap pengembalian kemasan bekas pakai Avoskin sebanyak 10 botol atau lebih, kamu dapat memilih salah satu gift berupa produk Avoskin worth up to IDR 200K")

col1,col2,col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.write("F.A.Q")
with col3:
    st.write("")
expander = st.expander("Ke mana saya bisa mengirimkan kemasan kosong Avoskin?")
expander.write("Untuk saat ini, kemasan botol milik Avoskin hanya dapat dikirimkan ke 19 drop point yang dimiliki oleh Waste4Change. 14 drop point terletak di Jakarta, 3 di Bandung, dan 2 di Semarang. Namun Avoskin akan bekerjasama dengan Waste4Change untuk menjalankan program ini di kota lain secepatnya.")
expander = st.expander("Apakah saya bisa mengirimkan kemasan produk brand lain untuk mendapatkan reward dari Avoskin?")
expander.write("Program ini khusus untuk pengembalian botol packaging produk Avoskin. Kamu pun dapat mengembalikan packaging kardus-nya, namun hal ini tidak akan mempengaruhi reward karena jumlah pengembalian packaging akan dihitung per kemasan botol atau tube.")
expander = st.expander("Apakah saya bisa menggabungkan material daur ulang lainnya dalam paket berisi produk kosong Avoskin saya?")
expander.write("Saat ini program hanya bisa menerima khusus untuk produk Avoskin.")