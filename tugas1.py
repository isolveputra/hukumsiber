import streamlit as st

st.set_page_config(page_title="Form Tugas Analisis ITE", layout="wide")

# Judul
st.title("📘 Form Tugas Analisis Kasus")
st.subheader("Etika dan Hukum Siber (UU ITE)")

# Identitas Mahasiswa
st.markdown("### 🧑‍🎓 Identitas Mahasiswa")
nama = st.text_input("Nama Mahasiswa")
nim = st.text_input("NIM")
kelas = st.text_input("Kelas")

st.divider()

# A. Analisis Etika
st.markdown("### A. Analisis Etika")
etika = st.text_area("Tuliskan analisis etika Anda:", height=150)

# B. Analisis Hukum
st.markdown("### B. Analisis Hukum (UU ITE)")
hukum = st.text_area("Tuliskan analisis hukum Anda:", height=150)

# C. Dampak
st.markdown("### C. Dampak Kasus")
dampak = st.text_area("Tuliskan dampak kasus:", height=150)

# D. Solusi
st.markdown("### D. Solusi dan Pencegahan")
solusi = st.text_area("Tuliskan solusi dan pencegahan:", height=150)

# E. Refleksi
st.markdown("### E. Refleksi Pribadi")
refleksi = st.text_area("Tuliskan refleksi Anda:", height=150)

st.divider()

# Tombol submit
if st.button("📩 Submit Tugas"):
    if nama and nim:
        st.success("Tugas berhasil dikirim!")
        
        st.markdown("### 📄 Ringkasan Jawaban")
        st.write("**Nama:**", nama)
        st.write("**NIM:**", nim)
        st.write("**Kelas:**", kelas)

        st.write("**Analisis Etika:**", etika)
        st.write("**Analisis Hukum:**", hukum)
        st.write("**Dampak:**", dampak)
        st.write("**Solusi:**", solusi)
        st.write("**Refleksi:**", refleksi)
    else:
        st.warning("Nama dan NIM wajib diisi!")
