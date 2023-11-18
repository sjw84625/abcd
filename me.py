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

  st.bar_chart(x='Sex',y='Survived',data=t)

  st.header("객실 등급에 따른 생존 비율")
  st.table(t.groupby(['Pclass','Survived'])['PassengerId'].count())
  #st.bar_chart(x='Pclass',y='Survived',data=t,hue='Sex')

  st.header("승선 항구에 따른 생존 비율")
  st.table(t.groupby(['Embarked','Survived'])['PassengerId'].count())
  st.bar_chart(x='Embarked',y='Survived',data=t)

  st.header("산점도 차트")
  st.table(t['Age'].describe())
  st.scatter_chart(x='Age',y='PassengerId',data=t)

  # st.header("바이올린 차트")
  # st.violin_chart(x='Survived',y='Age',data=t)
  # st.violin_chart(x='Survived',y='Age',hue='Sex',data=t)
  # st.violin_chart(x='Survived',y='Age',hue='Sex',data=t,split=True)

  # st.header("히트맵")
  # table=t.pivot_table(index=['Sex'],columns=['Pclass'],aggfunc='size')
  # st.heatmap(table,annot=True,fmt='d',cmap='rainbow')
  # st.table(t.corr())

  st.header("티켓 등급별 평균 요금")
  t.groupby(['Pclass'])['Fare'].count()

  st.header("가장 나이가 많은 사람")
  t['Age'].max()

  st.header("승선한 항구에 따른 평균요금")
  st.table(t.groupby(['Embarked'])['Fare'].count())

  st.header("어떤 항구에서 탑승한 여성의 생존확률이 가장 높을까?")
  st.bar_chart(x='Embarked',y='Survived',data=t,hue='Sex')
