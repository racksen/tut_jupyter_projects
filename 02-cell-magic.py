
# coding: utf-8

# ## Jupyter Cell Magic
# 
# [youtube](https://www.youtube.com/watch?v=DMW11FGz5Kg)
# [notebook](https://github.com/nicolaskruchten/pyconca/blob/master/jupyter_magic.ipynb)

# ## Time for some Magic!
# <hr>
# Lines and cells that start with % are not interpreted like normal Python code: they are magical. Let's try a simple one first which will show us what magic is available
# % - Line magic
# %% - Cell magic

# In[1]:


get_ipython().run_line_magic('lsmagic', '')


# In[2]:


get_ipython().run_line_magic('ls', '')


# In[3]:


get_ipython().run_line_magic('time', 'print("do you have time")')


# In[4]:


get_ipython().run_cell_magic('timeit', '', 'x =0 \nfor i in range(10): x+=i')


# In[5]:


get_ipython().run_cell_magic('bash', '', 'curl http://localhost:8888/')


# In[6]:


# 3rd party magic
get_ipython().run_line_magic('load_ext', 'sql')


# In[7]:


get_ipython().run_line_magic('sql', 'sqlite://')


# In[8]:


get_ipython().run_cell_magic('sql', '', '\nDROP TABLE IF EXISTS hockey;\nCREATE TABLE hockey ("Team", "Stanley Cups Won", "Country");\nINSERT INTO hockey VALUES ("Montreal Canadiens", 24, "Canada");\nINSERT INTO hockey VALUES ("Detroit Red Wings", 11, "USA");\nINSERT INTO hockey VALUES ("Boston Bruins", 6, "USA");\nINSERT INTO hockey VALUES ("Chicago Blackhawks", 11, "USA");\nINSERT INTO hockey VALUES ("Toronto Maple Leafs", 13, "Canada");')


# In[9]:


get_ipython().run_line_magic('sql', 'SELECT * FROM hockey ORDER BY "Stanley Cups Won" DESC LIMIT 3')


# In[10]:


class Thing():
    def _repr_html_(self):
        return """<h3 style="color: blue; text-align: center;">Hi Senthil!, I am a blue thing</h3><br/>"""

thing = Thing()
thing


# ## Going visual with Matplotlib
# The matplotlib cell magic lets us tell Jupyter we want to see charts inline with the notebook.

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


data = get_ipython().run_line_magic('sql', "SELECT * FROM hockey WHERE country='Canada' ")

data.pie()


# In[13]:


import seaborn as sns
sns.set()

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")


# In[14]:


import pandas as pd


# In[15]:


df = pd.read_csv('../ml_datasets/mps.csv',encoding='latin-1')
df.head()


# In[16]:


df.pivot_table(index="Party", columns="Province", aggfunc=len, values="Name")


# In[17]:


from pivottablejs import pivot_ui
pivot_ui(df)


# In[18]:



from ipywidgets import interact

@interact
def echo(input="Hello, world!", times=[1,5,1]):
    return (input+" ")*times


# In[19]:


import matplotlib.pyplot as plt

@interact
def polynomial(split=[0,10,20,100]):
    plt.pie([split/100.0, 1.0-split/100.0], labels=["Montreal Canadiens", "Toronto Maple Leafs"])
    plt.show()

