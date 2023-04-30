#!/usr/bin/env python
# coding: utf-8

# In[162]:


#Impoertation des librairies 

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
from plotly.offline import plot
df=pd.read_excel("Global Superstore.xls")
df


# In[58]:


df.isnull().sum()


# In[59]:


df.dtypes


# In[163]:


df['year'] = df['Order_Date'].dt.year
df


# In[90]:


y=df.groupby('year')['Sales'].sum()
y


# In[91]:


x=range(2011,2015)
plt.bar(x,y,color ='maroon')
plt.xlabel("Année")
plt.ylabel("Chiffre d'affaire")
plt.title("l'évolution des ventes par année")
plt.show()


# In[166]:


fig=px.treemap(df,path=['Country'],values='Sales')
plot(fig)


# In[167]:


x=df.groupby('Country')['Sales'].sum()
x


# In[7]:


df['CA'] = df['Country'].map(x) 
df


# In[8]:


y=df.groupby('year')['Sales'].sum()
df['CA_ann'] = df['year'].map(y) 
df


# In[9]:


y=df.groupby(['year','Country'])['Sales'].sum()
y


# In[168]:


fig=px.treemap(df,path=['year','Country'],values='Sales')
plot(fig)


# In[169]:


fig=px.treemap(df,path=['Country'],values='Profit')
plot(fig)


# # Etude statistique

# In[113]:


sns.violinplot(x=df.groupby('Country')['Sales'].sum(),color='#01D758',inner='box').set(title='Statistiques du Chiffre d_affaire')


# In[114]:


sns.violinplot(x=df.groupby('Country')['Sales'].sum(),color='#048B9A',inner='quartile').set(title='Quartile de chiffre d_affaire')


# In[112]:


sns.boxplot(y=df.groupby('Country')['Sales'].sum(),color='#FFCF39').set(title='Boxplot de chiffre d_affaire')


# In[118]:


sns.boxplot(x=df.groupby('Region')['Sales'].sum().index,y=df.groupby('Region')['Sales'].sum()).set(title='statistiques de chiffre d_affaire par region')


# In[22]:


x=df.groupby('Country')['Profit'].sum()
x
df['Profit_pays'] = df['Country'].map(x) 
df


# In[ ]:





# In[122]:


sns.violinplot(x=df.groupby('Country')['Profit'].sum(),color='#F3D617',inner='box').set(title='Statistiques du Profit par pays')


# In[123]:


sns.violinplot(x=df.groupby('Country')['Profit'].sum(),color='#D473D4',inner='quartile').set(title='Quartile du Profit')


# In[121]:


sns.boxplot(y=df.groupby('Country')['Profit'].sum(),color='#4B0082').set(title='Boxplot de Profit')


# In[130]:


sns.lmplot(x="CA",y="Profit_pays",data=df,markers="<").set(title='Relation entre chiffre d_affaire et le profit ')


# In[37]:


df.groupby('Country')['Discount'].sum()


# In[38]:


x=df.groupby('Country')['Discount'].sum()
x
df['Discount_pays'] = df['Country'].map(x) 
df


# In[132]:


sns.lmplot(x="Profit_pays",y="Discount_pays",data=df,markers="d").set(title='Relation entre le Profit et le Discount')


# In[42]:


df.groupby('Country')['Country'].count()


# In[172]:


x=df.groupby('Country')['Country'].count()
x
df['N_Order'] = df['Country'].map(x) 
df


# In[133]:


sns.lmplot(x="CA",y="N_Order",data=df,markers="H").set(title='Relation entre le Chiffre d_affaire et le nombre de commande')


# In[50]:


df.groupby('Product Name')['Quantity'].sum()


# In[178]:



fig=px.treemap(df,path=['Product Name'],values='Quantity')
plot(fig)


# In[51]:


df.groupby('Category')['Quantity'].sum()


# In[140]:


df.groupby('Category')['Quantity'].sum().plot(kind='bar',color='y')
plt.ylabel("Quantity")
plt.title("produit vendue par catégorie")
plt.show()


# In[54]:


df.groupby('Sub-Category')['Quantity'].sum()


# In[55]:


df.groupby(['Category','Sub-Category'])['Quantity'].sum()


# In[139]:


df.groupby('Sub-Category')['Quantity'].sum().plot(kind='bar',color='m')
plt.ylabel("Quantity")
plt.title("produit vendue par sub-catégorie")
plt.show()


# In[61]:


df.groupby('Sub-Category')['Profit'].sum()


# In[143]:


df.groupby('Sub-Category')['Profit'].sum().plot(kind='bar',color='#A98307')
plt.ylabel("Profit")
plt.title("Profit par sub-catégorie")
plt.show()


# In[144]:


df.groupby('Segment')['Segment'].count().plot(kind='bar',color='#D9603B')
plt.ylabel("Quantity")
plt.title("Quantity vendue par segment de client")
plt.show()


# In[148]:


sns.distplot(df.groupby('Country')['Sales'].sum(),kde=True,hist=True,color='r')


# In[149]:


sns.distplot(df.groupby('Country')['Sales'].sum(),rug=True,hist=True,color='y')


# In[150]:


sns.distplot(df.groupby('Country')['Profit'].sum(),kde=True,hist=True,color='b')


# In[151]:


sns.distplot(df.groupby('Country')['Profit'].sum(),rug=True,color='g')


# In[155]:


sns.kdeplot(df.groupby('Country')['Profit'].sum(),color='#DD985C').set(title='densité de Profit')


# In[154]:


sns.kdeplot(df.groupby('Country')['Sales'].sum(),color='#293133').set(title='densité de chiffre d_affaire')


# In[175]:


fig=px.treemap(df,path=['Country'],values='Shipping Cost')
plot(fig)


# In[156]:


sns.kdeplot(df.groupby('Country')['Sales'].sum(),df.groupby('Country')['Profit'].sum(),color='g')


# In[157]:


sns.jointplot(x=df.groupby('Country')['Sales'].sum(),y=df.groupby('Country')['Profit'].sum(),kind="reg",color='r')


# In[78]:


sns.jointplot(x=df.groupby('Country')['Sales'].sum(),y=df.groupby('Country')['Profit'].sum(),kind="kde",color="green")


# In[181]:


sns.jointplot(x=df.groupby('Country')['Sales'].sum(),y=df.groupby('Country')['Profit'].sum(),kind="hex",color="blue")


# In[158]:


corr=df[["Sales","Quantity","Discount","Profit","Shipping Cost"]].corr()
sns.heatmap(corr,annot=True).set(title='influence des paramétres')


# In[161]:


g=sns.PairGrid(df[["CA","Profit_pays",]],diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot)


# In[ ]:




