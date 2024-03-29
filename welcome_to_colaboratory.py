# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set()

import plotly.express as px

df = pd.read_csv('retail_sales_dataset.csv')

df.head()

df.shape

df.info()

df.describe()

df.nunique()

df.columns

num_col=[]
for col in df.columns:
    if(df[col].dtypes != 'object'):
        num_col.append(col)

print(num_col)

cat_col=[]
for col in df.columns:
    if(df[col].dtypes == 'object'):
        cat_col.append(col)

print(cat_col)

# Finding null values
df.isnull().sum()

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
df['Month'].head()

df.shape

df.drop(df[df['Total Amount']<df['Price per Unit']].index,inplace = True)
df.shape

plt.figure(figsize=(12,8))
sns.lineplot(x='Month', y='Total Amount', data=df)
plt.title('Sales Trend Overtime')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount per month')
plt.show()

df['Month']=df['Date'].dt.month
transaction_count = df.groupby('Month')['Transaction ID'].count()

transaction_count

plt.figure(figsize=(12, 6))
sns.lineplot(x=transaction_count.index, y=transaction_count.values)
plt.title('Transaction Frequency Over Months')
plt.xlabel('Month')
plt.ylabel('Transaction Count')
plt.show()

col='Product Category'
i=df[col].value_counts().index
v=df[col].value_counts().values

# Pie Plot
fig=px.pie(names=i,values=v,height=350, width=700, color=i,color_discrete_map={'Clothing':'#F4D03F', 'Electronics':'#3498DB', 'Beaty':'#2ECC71'})
fig.update_layout(paper_bgcolor='#A9DFBF')
fig.update_traces(showlegend=False)
fig.update_layout(title=dict(text=f"Pie Plot of {col}",x=0.5,font=dict(size=25)))
fig.update_traces(textinfo='text+percent+label',textfont_color='white',textfont_size=14)
fig.show()

heatmap = df.pivot_table(index='Month', columns='Product Category', values='Total Amount', aggfunc='sum')
plt.figure(figsize=(12,8))
sns.heatmap(heatmap, annot=True, fmt='.0f')
plt.title('Sales Heatmap')
plt.xlabel('Product Category')
plt.ylabel('Month')
plt.show()

plt.figure(figsize=(10, 8))
sns.swarmplot(x='Product Category', y='Age', hue='Gender', data=df, palette='Set2', dodge=True)
plt.title('Distribution of Age and Gender across Product Category')
plt.xlabel('Product Category')
plt.ylabel('Age')
plt.legend(title='Gender')
plt.show()

age_bins = [0, 18, 25, 35, 50, 100]
age_group = ['0-18', '19-25', '26-35', '36-50', '50+']
df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_group)
df.head()

plt.figure(figsize=(12,7))
sns.barplot(x='Age Group', y='Quantity', hue='Product Category', data=df)

plt.title('Product Category purchased by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Quantity Purchased')
plt.show()

retention = df.groupby('Customer ID')['Date'].min().reset_index()
retention['Year Month'] = retention['Date'].dt.to_period('M')

plt.figure(figsize=(12,6))
sns.countplot(x='Year Month', data=retention)
plt.title('Customer Retention Over Time')
plt.xlabel('Year Month')
plt.ylabel('Number of Customers')
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x='Age Group', y='Total Amount', hue='Product Category', data=df)

plt.title('Customer Spending Behaviour')
plt.xlabel('Age Group')
plt.ylabel('Total Amount')
plt.show()