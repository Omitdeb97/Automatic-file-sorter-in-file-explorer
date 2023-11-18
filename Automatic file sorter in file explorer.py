#!/usr/bin/env python
# coding: utf-8

# # Automatic file sorter in file explorer

# In[1]:


import os, shutil


# In[7]:


path = r"C:/Users/amitd/OneDrive/Documents/Data analysing/python tutorial/"


# In[13]:


file_path = os.listdir(path)


# In[ ]:





# In[19]:


# Crecking the list of path  
os.listdir(path)


# In[12]:


# making directories 

folder_name = ["csv files", "jpg files", "text files"]

for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        print(path + folder_name[loop])
        os.makedirs(path + folder_name[loop])
    


# In[ ]:


# MOving file into path directory to created intial directory 


# In[22]:


# Uisng loop to iterate file and move then in created directory files 

for file in file_path:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file,path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "jpg files/" + file):
        shutil.move(path + file,path + "jpg files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file,path + "text files/" + file)
    


# In[ ]:





# In[ ]:





# In[ ]:




