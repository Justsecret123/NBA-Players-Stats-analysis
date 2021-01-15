#!/usr/bin/env python
# coding: utf-8

# <h1> Libraries </h1>

# In[8]:


import ipywidgets as widgets


# <h1> Common widget <h1>

# In[7]:


def output_widget():
    return widgets.Output()


# <h1> Heatmap </h1>

# <h2> Button <h2>

# In[3]:


def heatmap_button():
    
    heatmap_button = widgets.Button(
        description="Show heatmap",
        button_style="info"
    )
    
    return heatmap_button
    


# <h2> Checkbox </h2>

# In[9]:


def heatmap_checkbox():
    
    heatmap_show_annotations = widgets.Checkbox(
        value=True,
        description="Show annotations"
    )
    
    return heatmap_show_annotations


# <h2> Width and Height sliders <h2>

# In[4]:


def heatmap_sliders():
    
    heatmap_width = widgets.IntSlider(
        value=10,
        min=5,
        max=10,
        description="Width"
    )

    heatmap_height = widgets.IntSlider(
        value=5, 
        min=5,
        max=10,
        description="Height"
    )
    
    return heatmap_width,heatmap_height


# <h1> Stats: points <h1> 

# <h2> Button </h2>

# In[11]:


def points_button():
    
    points_button = widgets.Button(
    description="Show total points",
    button_style="info"
    )
    
    return points_button


# <h2> Sliders </h2>

# In[12]:


def points_sliders():
    
    points_width = widgets.IntSlider(
    description="Width",
    value=20,
    min=5,
    max=20,
    )

    points_height = widgets.IntSlider(
    description="Height",
    value=5,
    min=5,
    max=15
    )
    
    return points_width,points_height


# <h1> Assists </h1>

# <h2> Button </h2>

# In[13]:


def assists_button():
    
    assists_button = widgets.Button(
    description="Show total assists",
    button_style="info"
    )
    
    return assists_button


# <h2> Sliders </h2>

# In[14]:


def assists_sliders():
    
    assists_width = widgets.IntSlider(
    description="Width",
    value=20,
    min=5,
    max=20
    ) 

    assists_height = widgets.IntSlider(
    description="Height",
    value=5,
    min=5,
    max=15
    )
    
    return assists_width, assists_height

