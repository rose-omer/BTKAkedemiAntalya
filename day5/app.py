#calıştırmak için terminale bunu yapıştır
# streamlit run app.py

import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date
from io import BytesIO

sembol = st.sidebar.text_input("Hisse Senedi", value='ASELS.IS')
st.title(sembol + ' Hisse Senedi Grafiği')

start_date = st.sidebar.date_input('Başlangıç Tarihi', value=date(2023, 1, 1))
end_date = st.sidebar.date_input('Bitiş Tarihi', value=date.today())

df = yf.download(sembol, start=start_date, end=end_date)

# Zaman dilimi bilgisini kaldırıyoruz
df.index = df.index.tz_localize(None)

st.line_chart(df['Close'])

st.subheader('Hisse Senedi Verileri')
st.write(df)

st.subheader('Hisse Senedi Verileri Excel Dosyası')

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=True, sheet_name='Sheet1')
    writer.close()
    processed_data = output.getvalue()
    return processed_data

excel_data = to_excel(df)
st.download_button(
    label='Excel olarak indir',
    data=excel_data,
    file_name=f'{sembol}_data.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)