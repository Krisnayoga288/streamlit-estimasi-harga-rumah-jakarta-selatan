import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_rumah.sav','rb'))

st.title('Estimasi Harga Rumah di Jakarta Selatan')

Luas_Bangunan = st.number_input('Masukan Luas Bangunan (cm2)')
Luas_Tanah 	= st.number_input('Masukan Luas Tanah (cm2)')
Kamar_Tidur = st.number_input('Masukan Jumlah Kamar Tidur')
Kamar_Mandi = st.number_input('Masukan Jumlah kamar Mandi')
Kategori_Garasi = st.number_input('Kategori Garasi (0, 1, 2)')

predict = ''

if st.button ('Estimasi Harga'):
    predict = model.predict(
        [[Luas_Bangunan, Luas_Tanah, Kamar_Tidur, Kamar_Mandi, Kategori_Garasi]]
    )
    st.write ('Estimasi Harga Rumah :', predict)