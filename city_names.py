#!/usr/bin/env python
# coding: utf-8

# # Parsing city names from a Wikipedia table

# ## Scraping Wikipedia

# In[1]:


import requests
url = requests.get('https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9F-_und_Mittelst%C3%A4dte_in_Deutschland').text


# In[2]:


from bs4 import BeautifulSoup
html_all = BeautifulSoup(url, 'html.parser')
#print(html_all.prettify())


# In[3]:


html_cities = html_all.select('table',{'class': 'wikitable sortable zebra'})[1]
#print(html_cities)


# ## Data preparation

# In[4]:


import pandas as pd
#pd.set_option('display.max_rows', None)

cities = pd.read_html(str(html_cities))
cities = pd.DataFrame(cities[0])

cities = cities[['Rang', 'Name', '2019', 'Bundesland']]
cities.columns = ['rank', 'name', 'pop_2019', 'bundesland']

cities['pop_2019'] = cities['pop_2019'].str.replace('.', '', regex=True).astype('int64')

cities['name'] = cities['name'].str.replace('\d+', '', regex=True)
cities['name'] = cities['name'].str.replace('["(*)"]', '', regex=True)
cities['name'] = cities['name'].str.replace('/', ' / ', regex=True)
cities['name'] = cities['name'].str.replace('Porta ', 'Porta-', regex=True)
cities['name'] = cities['name'].str.rstrip()

cities


# ## Looking for common suffixes
# ### -ingen

# In[5]:


import collections
from collections import Counter

def count_ingen(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('ingen') and len(word)>6 and word != 'Thüringen':
            print(word)
            
for city in cities['name']:
    count_ingen(city)


# ### -dorf

# In[6]:


def count_dorf(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('dorf'):
            print(word)
            
for city in cities['name']:
    count_dorf(city)


# ### -au

# In[7]:


def count_au(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('au') and word != 'Breisgau' and word != 'Donau':
            print(word)
            
for city in cities['name']:
    count_au(city)


# ### -bach

# In[8]:


def count_bach(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('bach'):
            print(word)
            
for city in cities['name']:
    count_bach(city)


# ### -ach

# In[9]:


def count_ach(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('ach') and word[-4].endswith('b') == False:
            print(word)
            
for city in cities['name']:
    count_ach(city)


# ### -feld

# In[10]:


def count_feld(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('feld'):
            print(word)
            
for city in cities['name']:
    count_feld(city)


# ### -heim

# In[11]:


from collections import defaultdict, Counter
def count_heim(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('heim'):
            print(word)
            
for city in cities['name']:
    count_heim(city)


# ### -hausen

# In[12]:


def count_hausen(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('hausen'):
            print(word)
            
for city in cities['name']:
    count_hausen(city)


# ### -stadt

# In[13]:


def count_stadt(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('stadt') and word != 'Lutherstadt':
            print(word)
            
for city in cities['name']:
    count_stadt(city)


# ### -furt

# In[14]:


def count_furt(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('furt'):
            print(word)
            
for city in cities['name']:
    count_furt(city)


# ### -berg

# In[15]:


def count_berg(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('berg'):
            print(word)
            
for city in cities['name']:
    count_berg(city)


# ### -burg

# In[16]:


def count_burg(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('burg'):
            print(word)
            
for city in cities['name']:
    count_burg(city)


# ### -a

# In[17]:


def count_a(string):
    for word, v in collections.Counter(string.split()).items():
        if word.endswith('a'):
            print(word)
            
for city in cities['name']:
    count_a(city)

