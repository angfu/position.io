#streamlit run C:\Users\shimi\.spyder-py3\position.py
import streamlit as st
import pandas as pd

st.title('位置決め')

st.sidebar.title('基準座標')
st.sidebar.header('左上')
lx = st.sidebar.number_input('x座標（左上）', format = '%.5f')
ly = st.sidebar.number_input('y座標（左上）', format = '%.5f')

st.sidebar.header('右下')
rx = st.sidebar.number_input('x座標（右下）', format = '%.5f')
ry = st.sidebar.number_input('y座標（右下）', format = '%.5f')

x2 = (lx + rx)/2
y2 = (ly + ry)/2

x1 = x2 - 4.5
y1 = y2 + 4.5

x3 = x2 + 4.5
y3 = y2 - 4.5

list1 = [[x2,y1],[x3,y1],[x1,y2],[x2,y2],[x3,y2],[x1,y3],[x2,y3]]
index1 = ['(1,2)','(1,3)','(2,1)','(2,2)','(2,3)','(3,1)','(3,2)']
columns1 = ['x座標','y座標']

st.table(pd.DataFrame(data = list1, index = index1, columns = columns1))