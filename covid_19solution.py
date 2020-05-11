import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("covid_19_india.csv")
print(df.head())

df.rename(columns={"Date":"date","State/UnionTerritory":"state","Confirmed":"confirmed","Deaths":"deaths","Cured":"cured"}, inplace=True)


df['active']=df['confirmed']-df['cured']-df['deaths']
top=df[df['date']==df['date'].max()]
Country =top.groupby('state')['confirmed','active','deaths'].sum().reset_index()
print(Country.head())


plt.figure(figsize=(20,15))
plt.xticks(rotation =90, fontsize =20)
plt.yticks(fontsize=15)
plt.xlabel("Dates",fontsize=30)
plt.ylabel("Total cases",fontsize=30)
plt.title("Cases in India with respect to date", fontsize=30)
total_cases = df.groupby('date')['date','confirmed'].sum().reset_index()
total_cases['date']=pd.to_datetime(total_cases['date'])

ax = sns.pointplot(x = total_cases.date.dt.date, y = total_cases.confirmed , color='r')
ax.set(xlabel='Dates', ylabel='Total cases')
plt.show()





top_death=top.groupby(by='state')['deaths'].sum().sort_values(ascending = False).head(20).reset_index()


plt.figure(figsize =(15,10))
plt.xticks(fontsize=15)
plt.yticks(fontsize=10)
plt.xlabel("Total deaths cases",fontsize=30)
plt.ylabel("States",fontsize=30)
plt.title("Top 20 states of death cases",fontsize=30)
ax=sns.barplot(x = top_death.deaths,y = top_death.state)

for i, (value, name)in enumerate(zip(top_death.deaths,top_death.state)):
    ax.text(value, i-.05, size=10, ha='left', va='center')
ax.set(xlabel="Total cases", ylabel="state")
plt.show()



top_actives=top.groupby(by='state')['active'].sum().sort_values(ascending = False).head(20).reset_index()


plt.figure(figsize =(15,10))
plt.xticks(fontsize=15)
plt.yticks(fontsize=10)
plt.xlabel("Total cases",fontsize=30)
plt.ylabel("States",fontsize=30)
plt.title("Top 20 states",fontsize=30)
ax=sns.barplot(x = top_actives.active ,y = top_actives.state)

for i, (value, name)in enumerate(zip(top_actives.active,top_actives.state)):
    ax.text(value, i-.05, size=10, ha='left', va='center')
ax.set(xlabel="Total cases", ylabel="state")
plt.show()




