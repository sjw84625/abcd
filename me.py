import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("신정우's profile")

path='train (1).csv'
t=pd.read_csv(path)
t

st.table(t.info())

st.table(t.head())

st.table(t.tail())

table=t.pivot_table(index=['Sex'],columns=['Pclass'],aggfunc='size')
sns.heatmap(table,annot=True,fmt='d',cmap='rainbow')
