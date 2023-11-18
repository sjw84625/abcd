import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("신정우's profile")

tab1,tab2=st.tabs(["About Me","Projects"])
with tab1:
  st.metric(label="나이",value="중1",delta="14")
with tab2:
  st.header("titanic data analysis")
  path='train (1).csv'
  t=pd.read_csv(path)
  t
  #col1,col2,col3,col4=st.columns(4)
  st.table(t.head())
  
  st.table(t.tail())
  
  st.table(t.describe())

  # st.table(t.isna().sum())
  # st.table(t.groupby('Embarked').count())
  # t['Age'].fillna(t['Age'].mean(),inplace=True)
  # t.isna().sum()
  # t['Embarked'].unique()
  # t['Embarked'].fillna('S',inplace=True)
  # st.table(t.isna().sum())

  st.header("여성과 남성의 비율")
  st.table(t.groupby(['Sex'])['PassengerId'].count())

  st.header("생존 여성과 남성의 비율")
  st.table(t.groupby(['Sex','Survived'])['PassengerId'].count())

  #seaborn.barplot(x='Sex',y='Survived',data=t)
