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
        data=[[int(la)-52,int(lo)-188]],
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

    #スライダーをつける
    rad = st.slider('目的地を中心とした円の半径 (km)',
                    value=40,min_value=5, max_value=50)
    # 半径の距離
    # st.subheader('目的地からの距離{:,}km'),format(rad)
    st.subheader(f'あなたにピッタリの目的地ですね')
    # 地図の初期設定
    m = folium.Map(location=[int(la)-52,int(lo)-188], zoom_start=7)
    # データを地図に渡す
    Destination(osanpo_data,m)
    #地図情報表示
    folium_static(m)
    
    st.title('いってらっしゃい！')