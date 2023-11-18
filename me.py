import streamlit as st
import pandas as pd
import numpy as np

st.title("신정우's profile")


st.metric(label="나이",value="중1",delta="14")

path='train (1).csv'
t=pd.read_csv(path)
t

st.table(t.head())

st.table(t.tail())

st.table(t.describe())
