#!/usr/bin/env python
# coding: utf-8

# <h1> Libraries </h1>

# In[1]:


import matplotlib.pyplot as plt


# <h1> Operations </h1>

# <h2> Points </h2>

# In[2]:


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

# In[3]:


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

# In[4]:


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

# In[5]:


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

# In[6]:


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

# In[7]:


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


# In[ ]:




