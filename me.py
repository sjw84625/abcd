import streamlit as st
import pandas as pd
import numpy as np

st.title("신정우's profile")

path='train (1).csv'
t=pd.read_csv(path)
t

t.columns

t.info()

t.head()
