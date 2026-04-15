import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Tugas ITE", layout="wide")

FILE_DATA = "data_tugas.csv"

# ========================
# Fungsi Simpan & Load
# ========================
def simpan_data(data):
    df = pd.DataFrame([data])
    if os.path.exists(FILE_DATA):
        df.to_csv(FILE_DATA, mode='a', header=False, index=False)
    else:
        df.to_csv(FILE_DATA, index=False)

def load_data():
    if os.path.exists(FILE_DATA):
        return pd.read_csv(FILE_DATA)
    else:
        return pd.DataFrame()

# ========================
# Sidebar Login Dosen
# ========================
st.sidebar.title("🔐 Login Dosen")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if username == "indrawan" and password == "161023":
        st.session_state["dosen_login"] = True
    else:
        st.error("Login gagal")

# ========================
# HALAMAN UTAMA
# ========================
st.title("📘 Form Tugas Analisis Kasus ITE")

# ========================
# FORM MAHASISWA (TANPA LOGIN)
# ========================
st.subheader("🧑‍🎓 Input Tugas Mahasiswa")

nama = st.text_input("Nama")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

etika = st.text_area("Analisis Etika")
hukum = st.text_area("Analisis Hukum")
dampak = st.text_area("Dampak")
solusi = st.text_area("Solusi")
refleksi = st.text_area("Refleksi")

if st.button("📩 Submit Tugas"):
    if nama and nim:
        data = {
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
        st.success("Tugas berhasil disimpan!")
    else:
        st.warning("Nama dan NIM wajib diisi!")

st.divider()

# ========================
# TAMPILKAN DATA (READ ONLY)
# ========================
st.subheader("📄 Data Jawaban Mahasiswa")

df = load_data()

if not df.empty:
    st.dataframe(df)
else:
    st.info("Belum ada data")

# ========================
# DASHBOARD DOSEN
# ========================
if "dosen_login" in st.session_state:

    st.divider()
    st.title("📊 Dashboard Dosen")

    if df.empty:
        st.warning("Belum ada data")
    else:
        # Filter mahasiswa
        st.subheader("🔍 Filter Mahasiswa")
        pilih_nim = st.selectbox("Pilih NIM", df["nim"].unique())

        data_mhs = df[df["nim"] == pilih_nim]

        st.write("### Detail Jawaban")

        for i, row in data_mhs.iterrows():
            with st.expander(f"{row['nama']} ({row['nim']})"):
                st.write("**Kelas:**", row["kelas"])
                st.write("**Etika:**", row["etika"])
                st.write("**Hukum:**", row["hukum"])
                st.write("**Dampak:**", row["dampak"])
                st.write("**Solusi:**", row["solusi"])
                st.write("**Refleksi:**", row["refleksi"])
