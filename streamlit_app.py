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

        # Interpretasi sederhana
        if hasil >= 80:
            st.info("Kategori: Sangat Efektif 🟢")
        elif hasil >= 50:
            st.info("Kategori: Cukup Efektif 🟡")
        else:
            st.warning("Kategori: Kurang Efektif 🔴")

st.markdown("---")
st.caption("© Tugas Logika Pemrograman Komputer - IPAL Efficiency Tool")
