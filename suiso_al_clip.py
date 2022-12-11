import numpy as np 
import pandas as pd
import streamlit as st

st.title('吹送距離clip後変換ファイル作成')

st.sidebar.markdown("### clip後のcsvファイルを入力してください")
uploaded_files = st.sidebar.file_uploader("choose a csv file", accept_multiple_files=False)
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=None).encode('utf-8')

sig_figures = st.selectbox('有効数字を選択してください',[2,3,4,5,6])

if uploaded_files:
    df =  pd.read_csv(uploaded_files)
    df = pd.DataFrame(data=df)
    df1 = df[df.iloc[:,1] != -1]
    df2 = df1.iloc[:,1:4]
    df3 = df1.iloc[:,10:17]
    df4 = pd.concat([df2,df3],axis=1,sort=False)
    df4 = df4.round(sig_figures)
    df4.reset_index(inplace=True,drop=True)
    for i in df4.index:
        if df4.iloc[i,1] != df4.iloc[i,4] or df4.iloc[i,2] != df4.iloc[i,5]:
            df4.iloc[i,3] = 0
    df4 = df4[df4.iloc[:,3] != 0]
    df4.reset_index(inplace=True,drop=True)
    df4 = df4.iloc[:,0:6]
    for i in df4.index:   
        for j in df4.index:
            if df4.iloc[i,1] == df4.iloc[j,1] and df4.iloc[i,2] == df4.iloc[j,2]:
                if df4.iloc[i,4] > df4.iloc[j,4]:
                    df4.iloc[i,5] = 0
    df4 = df4[df4.iloc[:,5] != 0]
    fname = 'convert'
    csv = convert_df(df4)
    st.download_button(
        fname,data = csv,file_name='convert.csv',
        mime = 'text/csv'
    )
            
    
