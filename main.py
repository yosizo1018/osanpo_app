import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('お散歩アプリ　～De,Tarame!～')
st.title('Welcome!!')

st.text('あなたの現在地は？　※参考緯度経度　東京：36,140')
la = st.text_input('緯度')
lo = st.text_input('経度')

if st.checkbox('記入OK!'):
    st.write('あなたの行先を選定中。')
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Now Loading... {i+1}')
        bar.progress(i + 1)
        time.sleep(0.03)
        
    st.title('行先が決まりました！こちらがあなたのお勧めお散歩ポイントです。')
    df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
    })

    st.map(df,
        latitude='col1',
        longitude='col2',
        size='col3',
        color='col4')
    
    st.title('いってらっしゃい！')