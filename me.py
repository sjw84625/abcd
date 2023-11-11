import streamlit as st
import pandas as pd
import numpy as np

st.title("신정우's profile")

path='train (1).csv'
t=pd.read_csv(path)
t

t1,t2,t3=(["","",""])
with t1:
  t.info()
with t2:
  t.head()
with t3:
  t.tail()
