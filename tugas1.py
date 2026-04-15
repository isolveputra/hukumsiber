import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Tugas ITE", layout="wide")

FILE_DATA = "data_tugas.csv"

# ========================
# FUNGSI
# ========================
def load_data():
    if os.path.exists(FILE_DATA):
        return pd.read_csv(FILE_DATA)
    else:
        return pd.DataFrame(columns=["nama","nim","kelas","jawaban","jumlah_kata"])

def save_data(df):
    df.to_csv(FILE_DATA, index=False)

def tambah_data(data):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    save_data(df)

def hitung_kata(teks):
    return len(teks.split())

# ========================
# HEADER
# ========================
st.title("📘 Tugas Analisis Kasus - Etika dan Hukum Siber")

# ========================
# LOGIN DOSEN (TERSEMBUNYI)
# ========================
with st.expander("🔐 Login Dosen (Klik untuk buka)"):
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        if username == "indrawan" and password == "161023":
            st.session_state["dosen_login"] = True
            st.success("Login berhasil!")
        else:
            st.error("Username / Password salah")

# ========================
# INSTRUKSI
# ========================
st.subheader("📖 Instruksi Tugas")
st.markdown("""
- Bacalah kasus di **SIPP PN**
- Lakukan analisis berdasarkan:
  - Etika
  - Hukum (UU ITE)
- Jawaban ditulis secara individu / kelompok
- Panjang jawaban: **500 – 800 kata**
""")

st.divider()

# ========================
# FORM MAHASISWA
# ========================
st.subheader("🧑‍🎓 Input Data Mahasiswa")

nama = st.text_input("Nama")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

st.subheader("✍️ Jawaban Analisis")

jawaban = st.text_area("Tuliskan jawaban Anda:", height=300)

jumlah_kata = hitung_kata(jawaban)

st.write(f"📊 Jumlah kata: **{jumlah_kata} kata**")

# Validasi kata
valid_kata = False

if jumlah_kata < 500:
    st.warning("Minimal 500 kata ❌")
elif jumlah_kata > 800:
    st.error("Maksimal 800 kata ❌")
else:
    st.success("Jumlah kata sesuai ✅")
    valid_kata = True

# ========================
# SUBMIT
# ========================
if st.button("📩 Submit Tugas"):
    if nama and nim:
        if valid_kata:
            data = {
                "nama": nama,
                "nim": nim,
                "kelas": kelas,
                "jawaban": jawaban,
                "jumlah_kata": jumlah_kata
            }
            tambah_data(data)
            st.success("Tugas berhasil disimpan!")
        else:
            st.error("Jumlah kata harus antara 500–800!")
    else:
        st.warning("Nama dan NIM wajib diisi!")

st.divider()

# ========================
# TAMPILKAN DATA
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
        idx = st.selectbox("Pilih Data (Index)", df.index)

        data = df.loc[idx]

        st.subheader("✏️ Edit Data")

        nama_edit = st.text_input("Nama", value=data["nama"], key="edit_nama")
        nim_edit = st.text_input("NIM", value=data["nim"], key="edit_nim")
        kelas_edit = st.text_input("Kelas", value=data["kelas"], key="edit_kelas")
        jawaban_edit = st.text_area("Jawaban", value=data["jawaban"], height=300, key="edit_jawaban")

        jumlah_kata_edit = hitung_kata(jawaban_edit)
        st.write(f"📊 Jumlah kata: **{jumlah_kata_edit} kata**")

        col1, col2 = st.columns(2)

        # UPDATE
        with col1:
            if st.button("💾 Update"):
                df.loc[idx] = [
                    nama_edit, nim_edit, kelas_edit,
                    jawaban_edit, jumlah_kata_edit
                ]
                save_data(df)
                st.success("Data berhasil diupdate!")

        # DELETE
        with col2:
            if st.button("🗑️ Hapus"):
                df = df.drop(idx).reset_index(drop=True)
                save_data(df)
                st.warning("Data berhasil dihapus!")
