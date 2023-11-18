import streamlit as st
import pandas as pd
import numpy as np

st.title("신정우's profile")

tab1,tab2=st.tabs(["About Me","Projects"])
with tab1:
  st.metric(label="나이",value="중1",delta="14")
with tab2:
  st.header("titanic data analysis")
  path='train (1).csv'
  t=pd.read_csv(path)
  t
  col1,col2,col3=st.columns(3)
  col1.metric(st.table(t.head()))
  
  col2.metric(st.table(t.tail()))
  
  col2.metric(st.table(t.describe()))
