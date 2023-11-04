import streamlit as st
import pandas as pd
import numpy as np

st.title('신정우')

st.write('데이터프레임 튜토리얼')
dataframe=pd.DataFrame({
  'first column':[1,2,3,4]
  'second column':[10,20,30,40],
})
st.dataframe(datareame,use_container_width=False)
st.table(dataframe)
