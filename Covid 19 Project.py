#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[8]:


covid_df=pd.read_csv("C:/Users/rohit/Downloads/COVID-19 Cases(05-12-2021).csv")


# In[9]:


covid_df.head()


# In[10]:


covid_df=covid_df[covid_df['Date']!='01-01-1970']


# In[20]:


covid_df.head()


# In[21]:


covid_df.describe()


# In[23]:


covid_df=covid_df[covid_df['Region']!='World']


# In[29]:


covid_df.drop(["S. No."],axis=1,inplace=True)


# In[34]:


covid_df.rename(columns={'Cured/Discharged':'Cured'},inplace=True)


# In[35]:


covid_df.rename(columns={'Confirmed Cases':'Confirmed'},inplace=True)


# In[36]:


covid_df.reset_index()


# In[38]:


covid_df['Date']=pd.to_datetime(covid_df['Date'],format='%d-%m-%Y')


# In[40]:


covid_df.head()


# In[42]:


covid_df['Active_Cases']=covid_df['Confirmed']-covid_df['Cured']-covid_df['Death']


# In[44]:


covid_df.tail()


# In[66]:


statewise=pd.pivot_table(covid_df,values=["Confirmed","Death","Cured"],index="Region",aggfunc=max)


# In[67]:


statewise["Recovery Rate"]=statewise["Cured"]*100/statewise["Confirmed"]


# In[68]:


statewise["Mortality Rate"]=statewise["Death"]*100/statewise["Confirmed"]


# In[69]:


statewise=statewise.sort_values(by="Confirmed",ascending=False)


# In[76]:


statewise.style.background_gradient(axis=0)


# In[82]:


#Top 10 Active Cases States

top_10_active_cases=covid_df.groupby(by= 'Region').max()[["Active_Cases","Date"]].sort_values(by=["Active_Cases"],ascending=False).reset_index()


# In[87]:


#Plotting Bar Plot for Top 10 States

top_10_active_cases=covid_df.groupby(by= 'Region').max()[["Active_Cases","Date"]].sort_values(by=["Active_Cases"],ascending=False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title("Top 10 States with most Active Cases in India",size=14)
ax=sns.barplot(data=top_10_active_cases[top_10_active_cases["Region"]!="India"].iloc[:10],y="Active_Cases",x="Region",linewidth=2,edgecolor="Red")
plt.xlabel("States")
plt.ylabel("Total Active Cases")
plt.show()


# In[97]:


#Top 10 States with Highest Deaths

top_deaths=covid_df.groupby(by= 'Region').max()[["Death","Date"]].sort_values(by=["Death"],ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 States with most Deaths in India",size=20)
ax1=sns.barplot(data=top_deaths[top_deaths["Region"]!="India"].iloc[:12],y="Death",x="Region",linewidth=3,edgecolor="Blue")
plt.xlabel("States")
plt.ylabel("Total Deaths")
plt.show()


# In[100]:


# Watching Growth Trend

fig=plt.figure(figsize=(12,6))

ax=sns.lineplot(data=covid_df[covid_df['Region'].isin(['Maharashtra','Kerala','Karnataka','Tamil Nadu','Uttar Pradesh'])],x='Date',y='Active_Cases',hue='Region')

ax.set_title("Top 5 Affected States in India",size=16)


# # Vaccine Data Statewise

# In[16]:


vaccine_df=pd.read_csv("C:/Users/rohit/Downloads/covid_vaccine_statewise.csv")


# In[17]:


vaccine_df.head()


# In[22]:


vaccine_df.info()


# In[102]:


vaccine_df.rename(columns={"Updated On" : 'Vaccine_Date'},inplace=True)


# In[103]:


#Calculating Nulls in our Data

vaccine_df.isnull().sum()


# In[104]:


vaccination = vaccine_df.drop(columns=['Sputnik V (Doses Administered)','AEFI','18-44 Years (Doses Administered)','45-60 Years (Doses Administered)','60+ Years (Doses Administered)'],axis=1)


# In[105]:


vaccination.head()


# In[122]:


# Male vs Female Vaccination (Making Pie Chart)

male = vaccination["Male(Individuals Vaccinated)"].sum()
female = vaccination["Female(Individuals Vaccinated)"].sum()
px.pie(names=['Male','Female'],values=[male,female],title="Male and Female Vaccination")


# In[116]:


# Remove rows where Region is India

vaccine=vaccine_df[vaccine_df.State!='India']


# In[117]:


vaccine.head()


# In[118]:


#Rename Columns

vaccine.rename(columns={"Total Individuals Vaccinated":"Total"},inplace=True)
vaccine.head()


# In[119]:


#Most Vaccinated States

max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values("Total",ascending=False)[:5]
max_vac


# In[121]:


fig=plt.figure(figsize=(10,5))
plt.title("Top 5 Vaccinated States in India",size=20)
x=sns.barplot(data=max_vac.iloc[:10],y=max_vac.Total,x=max_vac.index,linewidth=2,edgecolor="Red")
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show()


# In[ ]:




