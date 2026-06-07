import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Efisiensi IPAL Calculator",
    page_icon="💧",
    layout="centered"
)

# =========================
# UI HEADER
# =========================
st.title("💧 Kalkulator Efisiensi IPAL")
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
