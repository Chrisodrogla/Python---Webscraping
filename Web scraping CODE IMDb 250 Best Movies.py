#!/usr/bin/env python
# coding: utf-8

# # Import

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


website = 'https://www.imdb.com/chart/top/'


# In[4]:


response = requests.get(website)


# In[5]:


response.status_code


# In[9]:


soup = BeautifulSoup(response.content,'html.parser')

##try print(soup)


# In[67]:


results  = soup.find_all('td',class_="titleColumn")


# In[73]:


results[0].a.text ## Name


# In[70]:


results[0].span.text.strip('()') ## Year


# In[74]:


results[0].get_text(strip=True).split('.')[0] ## Ranking


# In[107]:


resultrates = soup.find_all('td',class_="ratingColumn imdbRating")


# In[109]:


resultrate[0].strong.text  ## rating


# In[110]:


Movie_Name = []
Yeear = []
Ranking = []

for result in results:
  
    Movie_Name.append(result.a.text)
    
    Yeear.append(result.span.text.strip('()'))
    
    Ranking.append(result.get_text(strip=True).split('.')[0])
    
  



# In[114]:


Rate = []

for resultrate in resultrates:
    Rate.append(resultrate.strong.text)


# In[ ]:





# In[118]:


Movie_Overview = pd.DataFrame({'Movie Title':Movie_Name,'Year':Yeear,'Ranking':Ranking,'Rating':Rate})


# In[119]:


Movie_Overview


# In[120]:


Movie_Overview.to_excel('results_single_page.xlsx',index=False)


# In[ ]:




