import streamlit as st

st.set_page_config(
    page_title="Efisiensi IPAL Calculator",
    page_icon="🧮",
    layout="centered"
)

# =========================
# CUSTOM BACKGROUND STYLE
# =========================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #e8f5e9);
    }

    /* Card-like container */
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.85);
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }

    /* Button styling */
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# UI HEADER
# =========================
st.title("🧮 Kalkulator Efisiensi IPAL")
st.caption("Menghitung efisiensi penurunan konsentrasi polutan berdasarkan data inlet & outlet")

st.markdown("---")

# =========================
# INPUT USER
# =========================
st.subheader("📥 Input Data Konsentrasi (BOD/COD/TSS/pH/Kadar Logam)")

cin = st.number_input(
    "Konsentrasi Inlet (C inlet)",
    min_value=0.0,
    format="%.4f"
)

cout = st.number_input(
    "Konsentrasi Outlet (C outlet)",
    min_value=0.0,
    format="%.4f"
)

# =========================
# RUMUS EFISIENSI
# =========================
def hitung_efisiensi(cinlet, coutlet):
    if cinlet == 0:
        return None
    return ((cinlet - coutlet) / cinlet) * 100

# =========================
# TOMBOL HITUNG
# =========================
st.markdown("---")

if st.button("🔍 Hitung Efisiensi"):
    hasil = hitung_efisiensi(cin, cout)

    if hasil is None:
        st.error("C_inlet tidak boleh 0 karena menyebabkan pembagian tidak terdefinisi.")
    else:
        st.success("Perhitungan berhasil!")

        st.metric(
            label="📊 Efisiensi IPAL",
            value=f"{hasil:.2f} %"
        )

    # =========================
    # INTERPRETASI EFISIENSI
    # =========================
    st.subheader("📌 Interpretasi Hasil")

    if hasil >= 90:
        st.success("Kategori: Sangat Efektif 🟢")
        st.write("Rentang: ≥ 90% — Kinerja IPAL sangat optimal, penurunan polutan sangat tinggi.")
        
    elif 75 <= hasil < 90:
        st.info("Kategori: Efektif 🟢")
        st.write("Rentang: 75% – 89% — Kinerja IPAL sudah baik dan memenuhi fungsi pengolahan.")

    elif 50 <= hasil < 75:
        st.warning("Kategori: Cukup Efisien 🟡")
        st.write("Rentang: 50% – 74% — Kinerja IPAL masih cukup, tetapi perlu optimasi proses.")

    elif 30 <= hasil < 50:
        st.error("Kategori: Kurang Efisien 🔴")
        st.write("Rentang: 30% – 49% — IPAL belum bekerja optimal, perlu evaluasi sistem.")

    else:
        st.error("Kategori: Tidak Efisien ⚠️")
        st.write("Rentang: < 30% — Kinerja IPAL sangat rendah, kemungkinan terjadi gangguan sistem.")
        
# =========================
# INFO STANDAR EFISIENSI IPAL
# =========================
st.markdown("---")
st.subheader("📚 Informasi Standar Efisiensi IPAL")

st.info("""
💡 Standar umum efisiensi IPAL (acuan edukasi):

🟢 ≥ 90%  → Sangat Efektif (kinerja optimal, sistem bekerja sangat baik)  
🟢 75% – 89% → Efektif (sudah memenuhi fungsi pengolahan dengan baik)  
🟡 50% – 74% → Cukup Efisien (masih bekerja, tapi perlu optimasi)  
🔴 30% – 49% → Kurang Efisien (perlu evaluasi sistem IPAL)  
⚠️ < 30% → Tidak Efisien (kinerja buruk, kemungkinan ada gangguan sistem)

📌 Catatan:
Nilai efisiensi dihitung dari penurunan konsentrasi polutan antara inlet dan outlet.
Semakin tinggi persen, semakin baik kemampuan IPAL dalam mengolah limbah.
""")

st.markdown("---")
st.caption("© Tugas Logika Pemrograman Komputer - IPAL Efficiency Tool")
