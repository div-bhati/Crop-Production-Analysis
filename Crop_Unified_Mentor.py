#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #for data manipulation and analysis
import numpy as np #for numerical operations and handling arrays
import matplotlib.pyplot as plt #for creating visaul plots
import seaborn as sns #for statstical visualization
import warnings #removes warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import sqlalchemy as sal #for database integration using sql
get_ipython().run_line_magic('matplotlib', 'inline')
#displays the plot inide the notebook


# In[2]:


#Importing the CSV file
data = pd.read_csv("Crop Production data.csv")


# In[3]:


data.info() #displays summary of dataframe


# In[4]:


data.describe() #provides count, mean, standard deviation, min max & percentiles( for numerical data in columns)


# In[5]:


data.isna().sum() #returns sum of NA(not available) values in the dataframe


# In[6]:


data = data.dropna() #removes all the NA values in the dataframe


# In[7]:


data.isnull().sum() #returns the sum of NULL values in the dataframe


# In[8]:


data.describe() #updated description of values after dropping NA values


# In[9]:


data['Season'] = data['Season'].str.strip() #removes any leading or trailing whitespaces in the column
data["State_Name"]= data['State_Name'].str.strip() #removes any leading or trailing whitespaces in the column


# In[10]:


seasons = {"Rabi":"Rabi","Kharif":"Kharif","Zaid":"Zaid","Summer":"Zaid","Whole Year":"Zaid","Autumn":"Kharif"}
data['Season'] = data['Season'].map(seasons)
#Altering values like Summer, whole year and replacing them with correct crop season values


# In[11]:


data.Season.value_counts() #counting the Season column in the dataframe 


# In[12]:


data = data.dropna()


# In[13]:


data.info()


# In[14]:


data.shape


# In[15]:


data['District_Name'].unique() 


# In[16]:


data['Season'].unique() #Checking the updated values after replacing the summer. whole year as values


# In[17]:


data['State_Name'].unique() #returns all the name of states in the dataframe


# Categorizing the states into zones. Creating North Zone, South Zone, East Zone, etc.
# 
# This will help in visualizing the data in dashboards

# In[18]:


north_india = ['Jammu and Kashmir',"Punjab","Himachal Pradesh","Haryana","Uttarakhand","Uttar Pradesh","Chandigarh"]
east_india = ['Bihar',"Odisha","Jharkhand","West Bengal"]
south_india = ['Andhra Pradesh',"Karnataka","Kerala","Tamil Nadu","Telangana"]
west_india = ["Rajasthan","Gujarat","Goa","Maharashtra"]
central_india =['Madhya Pradesh',"Chhattisgarh"]
north_east_india = ['Assam',"Meghalaya","Mizoram","Nagaland","Sikkim","Manipur","Tripura","Arunachal Pradesh"]
union_territories = ['Andaman and Nicobar Islands',"Dadra and Nagar Haveli","Puducherry"]


# In[19]:


def set_zones(row):
    if row["State_Name"].strip() in north_india:
        val="North Zone"
    elif row['State_Name'].strip() in east_india:
        val="East Zone"
    elif row["State_Name"].strip() in south_india:
        val= "South Zone"
    elif row['State_Name'].strip() in west_india:
        val="West Zone"
    elif row['State_Name'].strip() in central_india:
        val="Central Zone"
    elif row['State_Name'].strip() in north_east_india:
        val="NE Zone"
    elif row['State_Name'].strip() in union_territories:
        val="Union Territory"
    else:
        val ="No Val"
    return val


# In[20]:


data["Zones"] = data.apply(set_zones,axis=1)
data["Zones"].unique()


# In[21]:


data["Zones"].value_counts()


# In[22]:


data["Crop"].unique()


# Creating a new column crop category. It will help in further clarification in visualization

# In[23]:


crop = data['Crop']

def crop_category(crop):
    for i in ['Rice', 'Maize', 'Bajra', 'Jowar', 'Korra', 'Ragi', 'Barley', 'Other Cereals & Millets', 'Small millets', 'Wheat', 'Jobster', 'Paddy', 'Total foodgrain', 'Samai']:
        if crop ==i:
            return "Cereal"
    for i in ['Other Kharif pulses', 'Moong(Green Gram)', 'Urad', 'Arhar/Tur', 'Horse-gram', 'Gram', 'Masoor', 'other misc. pulses', 'Other Rabi pulses', 'Blackgram', 'Peas & beans (Pulses)', 'Cowpea(Lobia)', 'Peas (vegetable)', 'Beans & Mutter(Vegetable)', 'Khesari', 'Guar seed', 'Moth', 'Rajmash Kholar', 'Lentil', 'Pulses total', 'Ricebean (nagadal)', 'Peas & beans (Pulses)']:
        if crop == i:
            return "Pulses"
    for i in ['Groundnut', 'Sunflower', 'Castor seed', 'Sesamum', 'Linseed', 'Safflower', 'Rapeseed &Mustard', 'Niger seed', 'Soyabean', 'Oilseeds total', 'other oilseeds']:
        if crop == i:
            return "Oil Seeds"
    for i in ['Banana', 'Mango', 'Orange', 'Pome Granet', 'Grapes', 'Lemon', 'Sapota', 'Papaya', 'Pome Fruit', 'Citrus Fruit', 'Other Fresh Fruits', 'Water Melon', 'Pineapple', 'Apple', 'Peach', 'Pear', 'Plums', 'Litchi', 'Ber', 'Jack Fruit', 'Other Citrus Fruit', 'Other Dry Fruit']:
        if crop == i:
            return "Fruits"
    for i in ['Sweet potato', 'Tapioca', 'Potato', 'Onion', 'Cabbage', 'Bottle Gourd', 'Brinjal', 'Bhindi', 'Tomato', 'Cucumber', 'Cauliflower', 'Bitter Gourd', 'Drum Stick', 'Snak Guard', 'Ribed Guard', 'Ash Gourd', 'Beet Root', 'Turnip', 'Carrot', 'Redish', 'Colocosia', 'Lab-Lab', 'Yam', 'Pump Kin', 'Other Vegetables']:
        if crop == i:
            return "Vegetables"
    for i in ['Black pepper', 'Dry chillies', 'Turmeric', 'Dry ginger', 'Ginger', 'Coriander', 'Garlic', 'Cardamom', 'Cond-spcs other']:
        if crop == i:
            return "Spices"
    for i in ['Arecanut', 'Cashewnut', 'Coconut ', 'Rubber', 'Tea', 'Coffee']:
        if crop == i:
            return "Plantation Crops"
    for i in ['Cotton(lint)', 'Kapas', 'Jute', 'Mesta', 'Jute & mesta', 'Other fibres', 'Sannhamp']:
        if crop == i:
            return "Fiber Crop"
    for i in ['Arecanut (Processed)', 'Atcanut (Raw)', 'Cashewnut Processed', 'Cashewnut Raw', 'Arcanut (Processed)', 'Perilla']:
        if crop == i:
            return "Others"


# In[24]:


#.apply is used to apply a lambda or a function
#Creating a column crop and inserting the values according to the crop column
data['Crop Category']= data['Crop'].apply(crop_category)


# In[25]:


#returns the count of unique values in the crop category column
data['Crop Category'].value_counts()


# In[26]:


data = data.dropna(subset=['Crop Category'])


# In[27]:


plt.figure(figsize=(15,7))
plt.tick_params(labelsize=10)
data.groupby("Crop_Year")["Production"].agg("sum").plot.bar()
# plt.bar(grouped_values.index,grouped_values)
plt.xlabel("Year")
plt.title("Crop Production by Year")
plt.ylabel("Production")
plt.show()


# In[28]:


plt.pie(data["Crop Category"].value_counts(),labels=data['Crop Category'].value_counts().index,autopct="%1.1f%%")
plt.show()


# In[29]:


plt.figure(figsize=(15,6))
plt.bar(data["Zones"].value_counts().index,data["Zones"].value_counts(),color="blue")
plt.xlabel("Zones")
plt.ylabel("Count")
plt.title("Count Of Crop Production By Zones")
plt.show()


# In[30]:


state_production = data.groupby('State_Name')['Production'].sum().reset_index()
top_states = state_production.sort_values(by='Production', ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x='State_Name', y='Production', data=top_states)
plt.xticks(rotation=45)  # Rotate state names for better readability
plt.title('Top 5 States by Total Production')
plt.xlabel('State')
plt.ylabel('Total Production (in billions)')
plt.show()


# In[31]:


district_production = data.groupby(['State_Name', 'District_Name'])['Production'].sum().reset_index()

district_production['Label'] = district_production['District_Name'] + ', ' + district_production['State_Name']

sorted_districts = district_production.sort_values(by='Production', ascending=False)
top_districts = sorted_districts.head(5)

plt.figure(figsize=(12, 8))

plt.pie(top_districts['Production'], labels=top_districts['Label'], autopct='%1.1f%%',startangle=140)

plt.title('Top Districts by Total Production')
plt.show()


# In[32]:


data["Season"].value_counts()


# In[33]:


season_production = data.groupby("Season")['Production'].sum().reset_index()
top_seasons = season_production.sort_values(by='Production', ascending=False)
colors = ['#16423C',"#6A9C89","#0D7C66"]
plt.figure(figsize=(10, 6))
sns.barplot(x='Season', y='Production', data=top_seasons,palette = colors)


plt.xticks(rotation=45)  #rotating season names for better readability
plt.title('Total Production by Crop Season')
plt.xlabel('Crop Season')
plt.ylabel('Total Production')
plt.show()


# In[34]:


engine = sal.create_engine("mysql+mysqlconnector://root:12345678@localhost/Crop_Production_Unified_Mentor")
connection = engine.connect()


# In[35]:


data.to_sql("crop_data",con=connection,index=False,if_exists="replace")

