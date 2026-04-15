import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Tugas ITE", layout="wide")

FILE_DATA = "data_tugas.csv"

# ========================
# Fungsi Simpan Data
# ========================
def simpan_data(data):
    df = pd.DataFrame([data])
    if os.path.exists(FILE_DATA):
        df.to_csv(FILE_DATA, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE_DATA, index=False)

# ========================
# Load Data
# ========================
def load_data():
    if os.path.exists(FILE_DATA):
        return pd.read_csv(FILE_DATA)
    else:
        return pd.DataFrame()

# ========================
# Login Sederhana
# ========================
st.sidebar.title("🔐 Login")

role = st.sidebar.selectbox("Login sebagai:", ["Mahasiswa", "Dosen"])

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

login = st.sidebar.button("Login")

# Dummy akun
akun_dosen = {"dosen": "123"}
akun_mahasiswa = {"mhs1": "123", "mhs2": "123"}

if login:
    if role == "Dosen" and akun_dosen.get(username) == password:
        st.session_state["login"] = True
        st.session_state["role"] = "dosen"
        st.session_state["user"] = username
    elif role == "Mahasiswa" and akun_mahasiswa.get(username) == password:
        st.session_state["login"] = True
        st.session_state["role"] = "mahasiswa"
        st.session_state["user"] = username
    else:
        st.error("Login gagal")

# ========================
# Jika sudah login
# ========================
if "login" in st.session_state:

    # ========================
    # MAHASISWA
    # ========================
    if st.session_state["role"] == "mahasiswa":
        st.title("📘 Form Tugas Mahasiswa")

        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        kelas = st.text_input("Kelas")

        etika = st.text_area("Analisis Etika")
        hukum = st.text_area("Analisis Hukum")
        dampak = st.text_area("Dampak")
        solusi = st.text_area("Solusi")
        refleksi = st.text_area("Refleksi")

        if st.button("Submit"):
            data = {
                "user": st.session_state["user"],
                "nama": nama,
                "nim": nim,
                "kelas": kelas,
                "etika": etika,
                "hukum": hukum,
                "dampak": dampak,
                "solusi": solusi,
                "refleksi": refleksi
            }
            simpan_data(data)
            st.success("Tugas tersimpan!")

        # Tampilkan data miliknya
        st.subheader("📄 Jawaban Anda")
        df = load_data()
        if not df.empty:
            df_user = df[df["user"] == st.session_state["user"]]
            st.dataframe(df_user)

    # ========================
    # DOSEN
    # ========================
    elif st.session_state["role"] == "dosen":
        st.title("📊 Dashboard Dosen")

        df = load_data()

        if df.empty:
            st.warning("Belum ada data")
        else:
            st.subheader("Semua Jawaban Mahasiswa")
            st.dataframe(df)

            # Filter per mahasiswa
            st.subheader("🔍 Filter Mahasiswa")
            pilih_user = st.selectbox("Pilih Mahasiswa", df["user"].unique())

            data_mhs = df[df["user"] == pilih_user]

            st.write("### Detail Jawaban")
            st.write(data_mhs)

            # View detail satu per satu
            for i, row in data_mhs.iterrows():
                with st.expander(f"{row['nama']} - {row['nim']}"):
                    st.write("**Etika:**", row["etika"])
                    st.write("**Hukum:**", row["hukum"])
                    st.write("**Dampak:**", row["dampak"])
                    st.write("**Solusi:**", row["solusi"])
                    st.write("**Refleksi:**", row["refleksi"])

else:
    st.title("🔐 Silakan Login Terlebih Dahulu")
