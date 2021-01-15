#!/usr/bin/env python
# coding: utf-8

# <h1> Libraries </h1>

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns


# <h1> Operations </h1>

# <h2> Create heatmap </h2>

# In[2]:


def create_heatmap(totals, size=(10,5), annotations=True):
    correlation_matrix = totals.corr()
   
    plt.figure(figsize=size)
    color_palette = sns.color_palette("light:#4d91ff", as_cmap=True)
    ax = sns.heatmap(data=correlation_matrix, cmap=color_palette, annot=annotations)
    plt.title("Heatmap: correlation matrix")

    plt.show()


# <h2> Points </h2>

# In[3]:


def getTotalPoints(totals,size=(5,15)):
    t = totals["Points"].sort_values(ascending=False)
    plt.figure(figsize=size)
    t.plot.bar()
    plt.show()
    return t

def displayPoints(totals):
    ordered = totals.sort_values(by="Points",ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered["Points"][i]}')


# <h2> Assists </h2>

# In[4]:


def getTotalAssists(totals,size=(5,15)):
    t = totals["Assists"].sort_values(ascending=False)
    plt.figure(figsize=size)
    t.plot.bar()
    plt.show()
    return t

def displayAssists(totals):
    ordered = totals.sort_values(by="Assists",ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered["Assists"][i]}')


# <h2> Rebounds </h2>

# In[5]:


def getTotalRebounds(totals,size=(5,15)):
    t = totals["Rebounds"].sort_values(ascending=False)
    plt.figure(figsize=size)
    t.plot.bar()
    plt.show()
    return t

def displayRebounds(totals):
    ordered = totals.sort_values(by="Rebounds",ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered["Rebounds"][i]}')


# <h2> Steals </h2>

# In[6]:


def getTotalSteals(totals,size=(5,15)):
    t = totals["Steals"].sort_values(ascending=False)
    plt.figure(figsize=size)
    t.plot.bar()
    plt.show()
    return t

def displaySteals(totals):
    ordered = totals.sort_values(by="Steals",ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered["Steals"][i]}')


# <h2> Blocks </h2>

# In[7]:


def getTotalBlocks(totals,size=(5,15)):
    t = totals["Blocks"].sort_values(ascending=False)
    plt.figure(figsize=size)
    t.plot.bar()
    plt.show()
    return t

def displayBlocks(totals):
    ordered = totals.sort_values(by="Blocks",ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered["Blocks"][i]}')


# <h2> Totals <h2>

# In[8]:


def getTotalTotals(totals,size=(5,15)):
    t = totals.sum(axis=1)
    t = t.sort_values(ascending=False)
    plt.figure(figsize=size)
    t.plot.bar()
    plt.show()
    return t

def displayTotals(total_totals):
    i = 0
    for element in total_totals.index:
        print(f"{i+1}-{element} : {total_totals[i]}")
        i+=1


# <h1> By position </h1>

# <h2> Guards </h2>

# In[9]:


def TotalsByPosition_Guards(point_guards, shooting_guards):
    
    pg_totals = point_guards.sum(axis=1)
    sg_totals = shooting_guards.sum(axis=1)
    
    t = pg_totals.sort_values(ascending=False)
    
    plt.figure(figsize=[5,5])
    plt.title("Point guards")
    t.plot.bar()
    plt.show()
    
    ordered = pg_totals.sort_values(ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered.values[i]}')
        
    t = sg_totals.sort_values(ascending=False)
    
    plt.figure(figsize=[5,5])
    plt.title("Shooting guards")
    t.plot.bar()
    plt.show()
    
    ordered = sg_totals.sort_values(ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered.values[i]}')


# <h2> Forwards </h2>

# In[10]:


def TotalsByPosition_Forwards(small_forwards, power_forwards):
    
    sf_totals = small_forwards.sum(axis=1)
    pf_totals = power_forwards.sum(axis=1)
    
    t = sf_totals.sort_values(ascending=False)
    
    plt.figure(figsize=[5,5])
    plt.title("Small Forwards")
    t.plot.bar()
    plt.show()
    
    ordered = sf_totals.sort_values(ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered.values[i]}')

        
    t = pf_totals.sort_values(ascending=False)
    plt.figure(figsize=[5,5])
    plt.title("Power forwards")
    t.plot.bar()
    plt.show()
    
    ordered = pf_totals.sort_values(ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered.values[i]}')


# <h2> Centers </h2>

# In[11]:


def TotalsByPosition_Centers(centers):
    
    c_totals = centers.sum(axis=1)
    
    t = c_totals.sort_values(ascending=False)
    
    plt.figure(figsize=[5,5])
    plt.title("Centers")
    t.plot.bar()
    plt.show()
    
    ordered = c_totals.sort_values(ascending=False) 
    size = ordered.shape[0]
    for i in range(size):
        print(f' {i+1} - {ordered.index[i]} :  {ordered.values[i]}')


# <h1> Players comparison </h1>

# In[12]:


def compare_players(total_one, player_one, total_two, player_two):
    
    if total_one is not None and total_two is not None:
        if total_one > total_two:
            print(f"{player_one} has a higher total")
        else:
            print(f"{player_two} has a higher total")
    else:
        print("Error!")

