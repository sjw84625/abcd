import streamlit as st
import pandas as pd
import numpy as np

st.title("신정우's profile")

tab1,tab2=st.tabs(["About Me","Projects"])
with tab1:
  st.metric(label="나이",value="중1",delta="14")
with tab2:
  path='train (1).csv'
  t=pd.read_csv(path)
  t
  
  st.table(t.head())
  
  st.table(t.tail())
  
  st.table(t.describe())
