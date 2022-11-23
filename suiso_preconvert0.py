import numpy as np
import pandas as pd
import streamlit as st

st.title('吹送距離変換前処理ファイル')
st.write('streamlitで実装')

st.sidebar.markdown("### 調査地点のcsvファイルを入力してください")
uploaded_files = st.sidebar.file_uploader("choose a csv file", accept_multiple_files=False)

if uploaded_files:
    df = pd.read_csv(uploaded_files)
    df_columns = df.columns
    df1 = pd.DataFrame(
        data = {'distance':[],
                'radian':[]}
    )
    radian_menu = st.selectbox('角度を選択してください', ['16','32'])
    
    if radian_menu == '16':
        df2 = pd.concat([df, df1], sort=False)
        df2['distance'] = 1000
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=None).encode('utf-8')
        radians = list(range(0, 382.5, 22.5))
        for radian in radians:
            df2['radian'] = radian
            csv = convert_df(df2) 
            fname = 'ダウンロード' + str(radian)
            fname2 = 'suiso' + str(radian) + str('.csv')
            st.download_button(
                fname,data = csv,file_name=fname2,
                mime = 'text/csv'
            )
    elif radian_menu == '32':
        df2 = pd.concat([df, df1], sort=False)
        df2['distance'] = 1000
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=None).encode('utf-8')
        radians = list(range(0,370,10))
        for radian in radians:
            df2['radian'] = radian
            csv = convert_df(df2) 
            fname = 'ダウンロード' + str(radian)
            fname2 = 'suiso' + str(radian) + str('.csv')
            st.download_button(
                fname,data = csv,file_name=fname2,
                mime = 'text/csv'
            )
