#!/usr/bin/env python
# coding: utf-8

# # Video Game Sales  [Exploratory Data Analysis (EDA)] 
# 
# ![image.png](attachment:d83517d0-e50c-4e37-99f6-9040a9b2d3ef.png)!

# In[1]:


# Importing  necessary Liabraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#import the data 
data = pd.read_csv('vgsales.csv')


# In[149]:


#first look at the data
data.head(2)


# In[14]:


# over view of the dataset

data.info()

# The output shows we have null values in 2 columns 


# #### Cleaning 

# 
#  Since we have few number of null value, we can drop them it will not make any difference in the analysis 
# 
#                         or 
#  We can can replca null with mean or median : Data  Imputation 
#  
#     Mean or median :  Numberical (datatype)
#     Mode           : Catagorical (datatype)
#  
#  - we use function : data_filled_mean = data.fillna(data.mean())
# 

# In[13]:


data = data.dropna()   # Removing the null Values 
data.isna().sum()      # to get the null count column wise 


# In[ ]:







# ##  Column Wise EDA (Exploratory data analysis):  
# - Uni_variate Analysis (One column Analysis)
# - By-Variate
# - Multi-Variate analysis
# 
# 
# ####  Uni_variate Analysis (One column Analysis)
# 

# 
# 
# **1. Platform column**
# 
# - 1.  Which platform had the latest and earliest release and what were the sales of the games respectively in various parts of the world?

# In[17]:


data.head()


# In[24]:


#How many unique platforms are present in the data?

print(data['Platform'].nunique())
print(data['Platform'].unique())


# In[146]:


data['Year'].describe()

#The year of release for the earliest and latest is 1980, and 2020.


# In[37]:


# Applying Filter and saving it to new DataFrames 

Earliest = data.loc[(data['Year'] == 1980)]
Latest = data.loc[(data['Year'] == 2020)]


# In[150]:


Earliest.head(2)


# In[39]:


# now to find out the the platfoms for both earliest and lates 

print('Earliest Release platfomrs are :', Earliest['Platform'].unique())
print('Earliest Release platfomrs are :',Latest['Platform'].unique())


# In[169]:


# To calculate the sales in various regions, we will sum the values in each region

x =  ['NA_Sales','EU_Sales','JP_Sales', 'Other_Sales' ]


Earliest_Sales_RegionsWise = [Earliest['NA_Sales'].sum(),
                               Earliest['EU_Sales'].sum(),
                               Earliest['JP_Sales'].sum(),
                               Earliest['Other_Sales'].sum()]

Latest_Sales_RegionsWise = [Latest['NA_Sales'].sum(),
                            Latest['EU_Sales'].sum(),
                            Latest['JP_Sales'].sum(),
                            Latest['Other_Sales'].sum()]



# In[174]:


print(sns.barplot(x = x, y = Earliest_Sales_RegionsWise)) # Plot Earliest_Sales_RegionsWise
plt.show()


# In[175]:


# Latest_Sales_RegionsWise
print(sns.barplot(x = x, y = Latest_Sales_RegionsWise))
plt.show()


# In[178]:


# Line plot  comparing both earliest and Latest 

sns.lineplot(Earliest_Sales_RegionsWise)
sns.lineplot(Latest_Sales_RegionsWise)


# In[14]:


# ignore warnings
import warnings 

warnings.simplefilter(action='ignore', category=FutureWarning)


# **Conclusion  : The earliest release had considerable sales in various parts of the world. But the latest release did not have a lot of sales compared to the earliest.  Matter of fact, the sales were less than 1 million in sales for the latest release.**

# In[ ]:








# **2.  What was the most frequent platform, and how did it perform during the years in global sales and individual sales?**

# In[21]:


data['Platform'].value_counts()


# - Therefore DS has most number of counts 

# In[16]:


# now we will focus on the DS / Applying the filter on 

ds = data.loc[(data['Platform'] == 'DS')]
ds.head()


# In[17]:


ds['Year'].unique()


# In[30]:


final_NA = {1985: [], 2004:[], 2005: [], 2006: [], 2007: [], 2008:[], 2009: [], 2010: [], 2011: [], 2012:[], 2013: [], 2014: [], 2020: []}
final_EU = {1985: [], 2004:[], 2005: [], 2006: [], 2007: [], 2008:[], 2009: [], 2010: [], 2011: [], 2012:[], 2013: [], 2014: [], 2020: []}
final_JP = {1985: [], 2004:[], 2005: [], 2006: [], 2007: [], 2008:[], 2009: [], 2010: [], 2011: [], 2012:[], 2013: [], 2014: [], 2020: []}
final_Other = {1985: [], 2004:[], 2005: [], 2006: [], 2007: [], 2008:[], 2009: [], 2010: [], 2011: [], 2012:[], 2013: [], 2014: [], 2020: []}
final_Global = {1985: [], 2004:[], 2005: [], 2006: [], 2007: [], 2008:[], 2009: [], 2010: [], 2011: [], 2012:[], 2013: [], 2014: [], 2020: []}



# In[31]:


for i in ds.iterrows():
    print(i[1])
    break


# In[32]:


import numpy as np  # Import numpy for handling NaN values

for i in ds.iterrows():
    year = i[1][3]
    final_NA.setdefault(year, []).insert(0, i[1][6])
    final_EU.setdefault(year, []).insert(0, i[1][7])
    final_JP.setdefault(year, []).insert(0, i[1][8])
    final_Other.setdefault(year, []).insert(0, i[1][9])
    final_Global.setdefault(year, []).insert(0, i[1][10])
   


# In[33]:


for i in final_NA.keys():
  final_NA[i] = sum(final_NA[i])

for i in final_EU.keys():
  final_EU[i] = sum(final_EU[i])

for i in final_JP.keys():
  final_JP[i] = sum(final_JP[i])

for i in final_Other.keys():
  final_Other[i] = sum(final_Other[i])

for i in final_Global.keys():
  final_Global[i] = sum(final_Global[i])


# In[34]:


final_NA


# In[35]:


years = final_NA.keys()
sns.lineplot(data=final_NA, color='Blue', label='North America') #North America Sales
sns.lineplot(data=final_EU, color='Orange', label='Europe') #Europe Sales
sns.lineplot(data=final_JP, color='Green', label='Japan') #Japan Sales
sns.lineplot(data=final_Other, color='Purple', label='Rest of the world') #Rest of the world Sales


# ### OR

# In[187]:


NA_Sales = ds.groupby('Year')['NA_Sales'].sum()
EU_Sales = ds.groupby('Year')['EU_Sales'].sum()
JP_Sales = ds.groupby('Year')['JP_Sales'].sum()
Other_Sales = ds.groupby('Year')['Other_Sales'].sum()
Global_Sales = ds.groupby('Year')['Global_Sales'].sum()


sns.lineplot(NA_Sales,label = 'North America')
sns.lineplot(EU_Sales, label = 'Europe')
sns.lineplot(JP_Sales,label = 'Japan')
sns.lineplot(Other_Sales,label = 'Other countries' )


plt.ylabel('Sales')
plt.title('DS Platform : Regional Sales During the Years')



# In[ ]:





# #### Genre Column
# 
# What was the most frequent Genre, and how did it perform during the years in global sales and individual sales?

# In[106]:


data['Genre'].value_counts()


# In[107]:


# lets do the analysis from action genre
action = data.loc[(data['Genre'] == 'Action')]


# In[128]:


action = action.reset_index()

action.head(2)


# In[190]:


NA_Sales = action.groupby('Year')['NA_Sales'].sum()
EU_Sales = action.groupby('Year')['EU_Sales'].sum()
JP_Sales = action.groupby('Year')['JP_Sales'].sum()
Other_Sales = action.groupby('Year')['Other_Sales'].sum()
Global_Sales = action.groupby('Year')['Global_Sales'].sum()


sns.lineplot(NA_Sales,label = 'North America')
sns.lineplot(EU_Sales, label = 'Europe')
sns.lineplot(JP_Sales,label = 'Japan')
sns.lineplot(Other_Sales,label = 'Other countries' )


plt.ylabel('Sales')
plt.title('Action Genre : Regional  Sales During the Years')


# 
# 
# 
# 
# 
# ### OR
# 
# 
# 

# In[58]:


years = list(action['Year'].unique())
years = sorted(years)
years


# In[60]:


Final_NA = dict()
Final_EU = dict()
Final_JP = dict()
Final_Other = dict()
Final_Global = dict()

for i in years:
    Final_NA[i] = list()

for i in years:
  Final_EU[i] = list()

for i in years:
  Final_JP[i] = list()

for i in years:
  Final_Other[i] = list()

for i in years:
  Final_Global[i] = list()


# In[61]:


Final_NA


# In[62]:


# fill the values in list   

for i in action.iterrows():
  year = i[1][3]
  Final_NA[year].insert(0, i[1][6])
  Final_EU[year].insert(0, i[1][7])
  Final_JP[year].insert(0, i[1][8])
  Final_Other[year].insert(0, i[1][9])
  Final_Global[year].insert(0, i[1][10])


# In[64]:


for i in Final_NA.keys():
  Final_NA[i] = sum(Final_NA[i])

for i in Final_EU.keys():
  Final_EU[i] = sum(Final_EU[i])

for i in Final_JP.keys():
  Final_JP[i] = sum(Final_JP[i])

for i in Final_Other.keys():
  Final_Other[i] = sum(Final_Other[i])

for i in Final_Global.keys():
  Final_Global[i] = sum(Final_Global[i])


# In[68]:


Final_NA


# In[69]:


sns.lineplot(Final_NA, label="North America")
sns.lineplot(Final_EU, label="Europe")
sns.lineplot(Final_JP, label="Japan")
sns.lineplot(Final_Other, label='Rest of the World')


# In[ ]:








# ### Publisher Column 
# - What was the most frequent Publisher, and how did it perform during the years in global sales and individual sales?

# In[78]:


data['Publisher'].value_counts()


# In[195]:


# the most frequent publisher is Electronic Arts, let's analyze their sales over the years.

EA = data.loc[(data['Publisher'] == 'Electronic Arts')]  # filter by Electronic art 
EA.head(2)


# In[221]:


# Aggregate the sales year wise using groupby 

NA_Sales =  EA.groupby('Year')['NA_Sales'].sum()
EU_Sales =  EA.groupby('Year')['EU_Sales'].sum()
JP_Sales =  EA.groupby('Year')['JP_Sales'].sum()
Other_Sales =  EA.groupby('Year')['Other_Sales'].sum()
Global_Sales = EA.groupby('Year')['Global_Sales'].sum()


# PLot all the sales in line plot 
plt.figure(figsize =(7,5))
sns.lineplot(data = NA_Sales , label="North America")
sns.lineplot(data = EU_Sales, label="Europe")
sns.lineplot(data = JP_Sales,  label="Japan")
sns.lineplot(data = Other_Sales, label='Rest of the World')


plt.ylabel('Sales')
plt.show()


# ## OR

# ### Conclusion:
# 
# The line graph depicts sales trends from 1995 to 2015 in North America, Europe, Japan, and the rest of the world. 
# 
# key observations:
# 
# 1. **North America**: Sales peaked around 2005 and have been declining since then.
# 2. **Europe and Rest of the World**: These regions show similar trends, with sales peaking around 2005 but at lower levels than North America. The decline afterward is less steep.
# 3. **Japan**: Sales remained relatively stable throughout the years, with slight fluctuations.
# 
# Overall, the data suggests that North America experienced the most significant decline in sales, while Europe, the rest of the world, and Japan had varying levels of stability or decline. 
# 
# 
# 

# In[214]:


years


# In[215]:


# Create dictionarries fro all the sales regions 

EA_Final_NA = dict()
EA_Final_EU = dict()
EA_Final_JP = dict()
EA_Final_Other = dict()
EA_Final_Global = dict()

# for every key : years  creating a emty list so that we can add data later 

for i in years:
    EA_Final_NA[i] = list()

for i in years:
    EA_Final_EU[i]= list()

for i in years:
    EA_Final_JP[i]= list()

for i in years:
    EA_Final_Other[i]= list()

for i in years:
    EA_Final_Global[i] = list()


# In[216]:


EA_Final_NA


# In[217]:


# we need to fill sales data  in  the list  

for i in EA.iterrows():
  year = i[1][3]
  EA_Final_NA[year].insert(0, i[1][6])
  EA_Final_EU[year].insert(0, i[1][7])
  EA_Final_JP[year].insert(0, i[1][8])
  EA_Final_Other[year].insert(0, i[1][9])
  EA_Final_Global[year].insert(0, i[1][10])

# we need to aggregate the sales year wise 

for i in EA_Final_NA.keys():
  EA_Final_NA[i] = sum(EA_Final_NA[i])

for i in EA_Final_EU.keys():
  EA_Final_EU[i] = sum(EA_Final_EU[i])

for i in EA_Final_JP.keys():
  EA_Final_JP[i] = sum(EA_Final_JP[i])

for i in EA_Final_Other.keys():
  EA_Final_Other[i] = sum(EA_Final_Other[i])

for i in EA_Final_Global.keys():
  EA_Final_Global[i] = sum(EA_Final_Global[i])


# In[219]:


EA_Final_NA


# In[220]:


# now we will to plot 

sns.lineplot(EA_Final_NA, label="North America")
sns.lineplot(EA_Final_EU, label="Europe")
sns.lineplot(EA_Final_JP, label="Japan")
sns.lineplot(EA_Final_Other, label='Rest of the World')


# In[ ]:





# In[210]:


data.head(2)


# **Years Column**
# 
# - let's find out which year saw the most and least global sales, EU sales, Japan Sales, etc.

# In[223]:


data['Year'].value_counts()


# In[ ]:


# in Year 2009 we have maximun number games published so we will analyze 


# In[247]:


data.head(3)


# In[257]:


#  Sum up sales 


NA_Sales = data.groupby('Year')['NA_Sales'].sum()
EU_Sales = data.groupby('Year')['EU_Sales'].sum()
JP_Sales = data.groupby('Year')['JP_Sales'].sum()
Other_Sales = data.groupby('Year')['Other_Sales'].sum()
Global_Sales =  data.groupby('Year')['Global_Sales'].sum()
# plot the graph 

sns.lineplot(data = NA_Sales)
sns.lineplot(data = EU_Sales)
sns.lineplot(data = JP_Sales)
sns.lineplot(data = Other_Sales)
plt.title('Regional Sales During the Years')


# In[253]:


sns.lineplot(data = Global_Sales)
plt.title('Golbal Sales During the Years')


# Key Observations:
# 
# 1. **North America**: Sales in North America peaked around 2005 and have been declining since then. The decline is quite steep.
# 
# 2. **Europe and Rest of the World**: These regions also experienced a peak in sales around 2005, but at lower levels compared to North America. The decline afterward is less pronounced.
# 
# 3. **Japan**: Japan's sales remained relatively stable throughout the years, with minor fluctuations.
# 
# In summary:
# - North America had the highest peak in sales but the most significant decline.
# - Europe and the rest of the world followed a similar trend but with less intensity.
# - Japan maintained stability in sales.
# 
# Overall, the data suggests that global sales peaked around the year 2000 and have been declining since then. ¹²
# 

# In[ ]:








# #### Year Wise Top selling and least selling games

# In[481]:


# Find the game with the maximum global sales for each year
max_sales = data.loc[data.groupby("Year")["Global_Sales"].idxmax()][['Year', 'Name', 'Global_Sales']]
max_sales.columns = ['Year', 'Name_max', 'Global_Max_sales']

# Find the game with the minimum global sales for each year
min_sales = data.loc[data.groupby("Year")["Global_Sales"].idxmin()][['Year', 'Name', 'Global_Sales']]
min_sales.columns = ['Year', 'Name_min', 'Global_Min_sales']

# Merge the two DataFrames
mergd = pd.merge(min_sales, max_sales, on='Year', how='inner')
mergd


# In[490]:


# Plot 

years = mergd['Year']
max_sales = mergd['Global_Max_sales']
min_sales = mergd['Global_Min_sales']


sns.lineplot(x= years, y =max_sales)
sns.lineplot(x= years, y =min_sales)
plt.ylabel('Sales')


# In[ ]:





# In[ ]:




