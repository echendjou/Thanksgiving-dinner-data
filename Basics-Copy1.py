
# coding: utf-8

# In[ ]:


import pandas as pd
data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head()


# In[ ]:


data.columns


# In[ ]:


data["Do you celebrate Thanksgiving?"].value_counts()


# In[ ]:


data = data[data["Do you celebrate Thanksgiving?"] == "Yes"]


# In[ ]:


data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[ ]:


data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]


# In[ ]:


data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].value_counts()


# In[ ]:


apple_isnull = (pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"]))                
pumpkin_isnull = (pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"]))                  
pecan_isnull = (pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"]))
ate_pies = (apple_isnull & pumpkin_isnull & pecan_isnull)
ate_pies.value_counts()


# In[ ]:


data["Age"].value_counts()


# In[ ]:


def extract_age(age_str):
    if pd.isnull(age_str):
        return None
    age_str = age_str.split(" ")[0]
    age_str = age_str.replace("+", "")
    return int(age_str)

data["int_age"] = data["Age"].apply(extract_age)
data["int_age"].describe()


# Although we only have a rough approximation of age, and it skews downward because we took the first value in each string (the lower bound), we can see that age groups of respondents are fairly evenly distributed.

# In[ ]:


data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts()


# In[ ]:


def extract_income(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace(",", "")
    income_str = income_str.replace("$", "")
    return int(income_str)

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(extract_income)
data["int_income"].describe()


# Although we only have a rough approximation of income, and it skews downward because we took the first value in each string (the lower bound), the average income seems to be fairly high, although there is also a large standard deviation.

# In[ ]:


data[data["int_income"] < 50000]["How far will you travel for Thanksgiving?"].value_counts()


# In[ ]:


data[data["int_income"] > 150000]["How far will you travel for Thanksgiving?"].value_counts()


# It appears that more people with high income have Thanksgiving at home than people with low income. This may be because younger students, who don't have a high income, tend to go home, whereas parents, who have higher incomes, don't.

# In[ ]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age"
)


# In[ ]:


data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", 
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income"
)


# It appears that people who are younger are more likely to attend a Friendsgiving, and try to meet up with friends on Thanksgiving.
