#!/usr/bin/env python
# coding: utf-8

# <h1> Libraries </h1>

# In[1]:


import ipywidgets as widgets


# <h1> Common widget <h1>

# In[2]:


def output_widget():
    return widgets.Output()


# <h1> Heatmap </h1>

# In[3]:


def heatmap_widgets():
    
    heatmap_button = widgets.Button(
        description="Show heatmap",
        button_style="info"
    )
    
    heatmap_checkbox = widgets.Checkbox(
        value=True,
        description="Show annotations"
    )
  
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
    
    heatmap_output = widgets.Output()
    
    return heatmap_button, heatmap_checkbox, heatmap_width, heatmap_height, heatmap_output 


# <h1> Points <h1> 

# In[4]:


def points_widgets():
    
    points_button = widgets.Button(
    description="Show total points",
    button_style="info"
    )

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
    
    points_output = widgets.Output()
    
    return points_button, points_width, points_height, points_output


# <h1> Assists </h1>

# In[5]:


def assists_widgets():
  
    assists_button = widgets.Button(
    description="Show total assists",
    button_style="info"
    )
    
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
    
    assists_output = widgets.Output()
    
    return assists_button, assists_width, assists_height, assists_output


# <h1> Rebounds </h1>

# In[6]:


def rebounds_widgets():

    rebounds_button = widgets.Button(
    description="Show total rebounds", 
    button_style="info"
    )
    
    rebounds_width = widgets.IntSlider(
    description="Width",
    value=20,
    min=5,
    max=20
    )

    rebounds_height = widgets.IntSlider(
    description="height",
    value=5,
    min=5,
    max=15
    )
    
    rebounds_output = widgets.Output()
    
    return rebounds_button, rebounds_width, rebounds_height, rebounds_output


# <h1> Steals </h1>

# In[7]:


def steals_widgets():
    
    steals_button = widgets.Button(
        description="Show total steals",
        button_style="info"
    )
    
    steals_width = widgets.IntSlider(
        description='Width',
        value=20,
        min=5,
        max=20
    )

    steals_height = widgets.IntSlider(
        description="Height",
        value=5,
        min=5,
        max=15
    )
    
    steals_output = widgets.Output()
    
    return steals_button, steals_width, steals_height, steals_output


# <h1> Blocks </h1>

# In[8]:


def blocks_widgets():
    
    blocks_button = widgets.Button(
        description="Show total blocks",
        button_style="info"
    )

    blocks_width = widgets.IntSlider(
        description="Width",
        value=20,
        min=5,
        max=20
    )

    blocks_height = widgets.IntSlider(
        description='Height',
        value=5,
        min=5,
        max=15
    )
    
    blocks_output = widgets.Output()
    
    return blocks_button, blocks_width, blocks_height, blocks_output


# <h1> Totals </h1>

# In[ ]:


def totals_widgets():

    totals_button = widgets.Button(
        description="Show totals",
        button_style="info"
    )

    totals_width = widgets.IntSlider(
        description="Width",
        value=20,
        min=5,
        max=20
    )

    totals_height = widgets.IntSlider(
        description="Height",
        value=5,
        min=5,
        max=15
    )

    totals_output = widgets.Output()
    
    return totals_button, totals_width, totals_height, totals_output

