import folium
from streamlit_folium import folium_static
import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('お散歩アプリ　～De,Tarame!～')
st.title('ようこそ!!')

st.text('あなたの現在地は？　※参考緯度経度　東京：36,140')
la = st.text_input('緯度')
lo = st.text_input('経度')
if la and lo != '': 
    d = [int(la)-52, int(lo)-188]
else:
    pass

#視覚的要素だけの"Loading"機能実装
if st.checkbox('記入OK!'):
    st.write('あなたの行先を選定中。')
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Now Loading... {i+1}')
        bar.progress(i + 1)
        time.sleep(0.01)
        
# 入力された緯度経度を元にデタラメな緯度経度データを作成する
    st.title('行先が決まりました！こちらがあなたのお勧めお散歩ポイントです。')
    osanpo_data = pd.DataFrame(
        data=[d],
        index=['目的地'],
        columns=['x','y']
    )
    
# データを地図に渡す関数を作成する
    def Destination(df,m):
        for index, r in df.iterrows():
            
            # ピンをおく
            folium.Marker(
                location=[r.x, r.y],
                popup=index,
            ).add_to(m)
            
            # サークルマーカープロット(外径色は赤，内径色は青)
            folium.CircleMarker(
                location=d,
                radius=40,
                color='#ff0000',
                fill_color='#0000ff'
            ).add_to(m)
            
    st.subheader(f'あなたにピッタリの目的地ですね')
    # 地図の初期設定
    m = folium.Map(location=d, zoom_start=7)
    # データを地図に渡す
    Destination(osanpo_data,m)
    #地図情報表示
    folium_static(m)
    
    st.title('いってらっしゃい！')