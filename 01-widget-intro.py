
# coding: utf-8

# <hr>
# ## Jupyter Widgets
# <hr>

# In[1]:


from __future__ import print_function
from ipywidgets import interact, interactive, interact_manual, fixed
import ipywidgets as widgets


# In[2]:


# define a simple function and call it
def fn(x):
    return x
fn(3)


# In[3]:


interact(fn, x=3)


# In[4]:


interact(fn, x=True)


# In[5]:


interact(fn, x='Hi Senthil')


# In[6]:


@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)


# In[7]:


interact(fn, x = ['senthil', 'ramalingam'])


# In[8]:


interact(fn, x = [('name', 'Senthil'), ('age', 45)])


# In[9]:


# show just slider
def btn_click(b):
    print('Senthil')
    
btn = widgets.Button(description='Hello')
btn.on_click(btn_click)
display(btn)


# In[10]:


# show the widget interface
txt = widgets.Text()
txt.keys


# In[11]:


#display composite widgets 
display(txt,btn)


# In[12]:


#linking widgets
a = widgets.FloatText()
b= widgets.FloatSlider()
display(a,b)
mylink = widgets.jslink((a, 'value'), (b, 'value'))


# In[13]:


# observer widgets
int_range = widgets.IntSlider()
display(int_range)

def on_int_range_chage(change):
    print(change['new'])

int_range.observe(on_int_range_chage, names='value')


# In[14]:


get_ipython().run_line_magic('pinfo', 'widgets')

