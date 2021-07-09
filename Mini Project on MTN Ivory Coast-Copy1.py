#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries
import numpy as np 
import pandas as pd 


# In[15]:


#load datasets 
#load Telcom dataset 1 and assign it variable df1

df1=pd.read_csv('C:\\Users\\mac\Downloads\Telcom_dataset.csv')
df1.head()


# In[82]:


#load Telcom dataset day 2 and assign it variable df2 

df2=pd.read_csv('C:\\Users\\mac\Downloads\Telcom_dataset2.csv')
df2.head()


# In[101]:


#load Telcom Dataset 3 and assign it variable df3 

df3=pd.read_csv('C:\\Users\\mac\Downloads\Telcom_dataset3.csv')
df3.head()


# In[148]:


#rename columns according to description given in geodata sets

#df1
dict={'PRODUTC':'PRODUCT','DATETIME':'DATE_TIME','DW_A_NUMBER':'DW_A_NUMBER_INT',
     'DW_B_NUMBER':'DW_B_NUMBER_INT' ,'CELLID':'CELL_ID','SIET_ID':'SITE_ID'}
df1.rename(columns=dict,inplace=True)
display(df1)

#df2
df2.rename(columns=dict,inplace=True)
display(df2)

#df3
df3.rename(columns=dict,inplace=True)
display(df3)


# In[195]:


#getting information and descriptive statistics from the three datasets 

df1.info()
df1.describe()



# In[150]:


df2.info()
df2.describe()


# In[151]:


df3.info()
df3.describe()


# In[152]:


# observations from the telcom datasets
#what was the most used product on day one, day two and day three 
#day one
df1['PRODUCT'].value_counts().idxmax()

# what was the highest amount of money spent on voice and sms in the three days 


# In[153]:


#day two
df2['PRODUCT'].value_counts().idxmax()


# In[154]:


#day three
df3['PRODUCT'].value_counts().idxmax()


# In[155]:


# what was the highest amount of money spent on voice and sms in the three days
#day one 
df1.groupby('PRODUCT').VALUE.max()


# In[156]:


#day two
df2.groupby('PRODUCT').VALUE.max()


# In[157]:


#day three
#might have an outlier* 
df3.groupby('PRODUCT').VALUE.max()


# In[158]:


#Observations from day one, two and three infered from the telcom datasets 
#the value column is the only one that is an integer the rest are strings-Might need to change the date and time column 
#The only column that contains missing values is the site_id column 
#The most used product on day one was Voice and on day two and three was SMS 
#The highest billing price paid for MTN products on the three days for the three products was as follows:
#day one
    #Voice    1860
    #data     4440
    #sms       100
#for day two
    #Voice    3380
    #data     1000
    #sms       100
#for day three
    #Voice    12900
    #data       832
    #sms        100


# In[178]:


#since the three datasets contain the same number of rows and columns,it is easier to concatenate and clean then analyze the data
#concatenate data 
telcom_df=pd.concat([df1,df2,df3],axis=0)
telcom_df


# In[179]:


#Clean data by , dropping unnecessary columns, checking for duplicate values, checking for unique values and handling missing data
#drop unnecessary columns 
telcom_df.drop(['COUNTRY_A','COUNTRY_B','CELL_ON_SITE'],axis=1)


# In[180]:


#check for duplicate values
telcom_df.duplicated().sum()


# In[164]:


#view the duplicated rows 
telcom_df.loc[telcom_df.duplicated(),:]
#drop duplicates that don't repeat along column
#Do more research on how to drop 
#there are 253 duplicated rows more understanding is needed to know whether to drop or keep these duplicated values-team decision 


# In[163]:


#view unique data
telcom_df.nunique()


# In[170]:


#view number missing values in data 
telcom_df.isnull().sum()


# In[175]:


#drop missing values only found in site_id column so drop via subset
telcom_df.dropna()


# In[ ]:


#check for unique values
telcom_df.nunique()


# In[181]:


#change the datatype of the date and time 
telcom_df['DATE_TIME'] = pd.to_datetime(telcom_df['DATE_TIME'])


# In[182]:


#check if the date and time dtype has changed 
telcom_df.info()


# In[ ]:


#Next step is to analyse the geo data set and merge them to answer the questions


# In[188]:


#geo data set 
df_cells_geo=pd.read_csv('C:\\Users\\mac\Downloads\cells_geo - cells_geo.csv')
#split the dataset
df_cells_geo=df_cells_geo[';VILLES;STATUS;LOCALISATION;DECOUPZONE;ZONENAME;LONGITUDE;LATITUDE;REGION;AREA;CELL_ID;SITE_CODE'].str.split(pat=';',n=11, expand=True)
#drop the column 0
df_cells_geo.drop([0],axis=1,inplace=True)
#rename the columns 
df_cells_geo.columns=['VILLES','STATUS','LOCALISATION','DECOUPZONE','ZONENAME','LONGITUDE','LATITUDE','REGION','AREA','CELL_ID','SITE_CODE']
#replace empty whitespace with NaN
df_cells_geo.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df_cells_geo


# In[203]:


#cleaning the geo data set
#missing values, duplicate values, drop unnecessary columns, outliers 
#handle our missing values 
df_cells_geo.isnull().sum()
#drop missing values 
df_cells_geo.dropna()


# In[205]:


#duplicate values 
df_cells_geo.duplicated().sum()


# In[209]:


#viewing the duplicate values 
df_cells_geo.loc[df_cells_geo.duplicated(), :]
#dropping our duplicate values 
df_cells_geo.drop_duplicates()


# In[1]:


#outliers-Angela 


# In[210]:


df_cells_geo.describe()


# In[212]:


df_cells_geo. info()


# In[2]:


#check for common values in the two dataframes to understand where to merge
#Moe and Sylvia 


# In[240]:


#merge the geo dataset and telcom dataset 

df_merged=telcom_df.merge(df_cells_geo, left_on='SITE_ID', right_on='SITE_CODE')
df_merged.info()


# In[3]:


#what was the most used product for the three days in Ivory Coast -Patrick


# In[241]:


#what was the most used city that is city with the highest usage -Moe 


# In[ ]:


#most used during business and home hours -Victor 
#working hours in ivory coast are 8AM to 5PM that means home hours are 6PM-7AM
#Source for working hours was google site https://www.expatfinder.com/ivory-coast/expat-guides/article/working-in-ivory-coast/1915


# In[ ]:


#Analysis 


# In[ ]:




