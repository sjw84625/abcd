import streamlit as st
import pandas as pd
import numpy as np
#sns.barplot(x='Sex',y='Survived',data=t) -> st.bar_chart(x='Sex',y='Survived',data=t)
#sns.barplot(x='Pclass',y='Survived',data=t,hue='Sex') -> st.bar_chart(x='Pclass',y='Survived',data=t,color='Sex')
st.title("신정우's profile")

tab1,tab2=st.tabs(["About Me","Projects"])
with tab1:
  col1,col2,col3=st.columns(3)
  col1.metric(label="나이",value="중1",delta="14")
  col2.metric(label="학교",value="구암중학교",delta="구암초등학교")
  col3.metric(label="희망 전공",value="컴퓨터 공학과",delta="kaist")
with tab2:
  st.header("titanic data analysis")
  path='train (1).csv'
  t=pd.read_csv(path)
  t
  st.table(t.head())
  
  st.table(t.tail())
  
  st.table(t.describe())

  # st.table(t.isna().sum())
  # st.table(t.groupby('Embarked').count())
  t['Age'].fillna(t['Age'].mean(),inplace=True)
  # t.isna().sum()
  t['Embarked'].unique()
  t['Embarked'].fillna('S',inplace=True)
  # st.table(t.isna().sum())

  st.header("여성과 남성의 비율")
  st.table(t.groupby(['Sex'])['PassengerId'].count())

  st.header("생존 여성과 남성의 비율")
  st.table(t.groupby(['Sex','Survived'])['PassengerId'].count())

  st.bar_chart(x='Sex',y='Survived',data=t)

  st.header("객실 등급에 따른 생존 비율")
  st.table(t.groupby(['Pclass','Survived'])['PassengerId'].count())
  #st.bar_chart(x='Pclass',y='Survived',data=t,hue='Sex')
  st.bar_chart(x='Pclass',y='Survived',data=t,color='Sex')

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
  st.table(t.groupby(['Pclass'])['Fare'].count())

  st.header("가장 나이가 많은 사람")
  st.write(t['Age'].max())

  st.header("승선한 항구에 따른 평균요금")
  st.write("Cherbourg, Queenstown, Southampton")
  st.table(t.groupby(['Embarked'])['Fare'].count())

  st.header("어떤 항구에서 탑승한 여성의 생존확률이 가장 높을까?")
  #st.bar_chart(x='Embarked',y='Survived',data=t,hue='Sex')
  st.bar_chart(x='Embarked',y='Survived',data=t,color='Sex')
