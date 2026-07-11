#!/usr/bin/env python
# coding: utf-8

# ## 1. Resume_text_extraction :

# In[42]:


import pdfplumber


# In[43]:


def extract_resume_text(pdf_name):
    resume_text = ""

    with pdfplumber.open(pdf_name) as pdf:
     for page in pdf.pages:
        text = page.extract_text()

        if text:
            resume_text += text +'\n'
    return resume_text       




# In[44]:



# ## 2. Cleaning the text :

# In[45]:


import re


# In[48]:


def clean_resume_text(resume_text):
    text = re.sub(r"\s+"," ",resume_text)                           # remove extra spaces
       
    text = re.sub(r"\S+@\S+"," ",text)                              # removes email as it will not be needed for us
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)              # removes unwanted links eg:my linked in profile
    text = re.sub(r"\+?\d[\d\s\-()]{8,}\d"," ", text)               # remove phone nos as they are not uch needed
    text = re.sub(r"[^a-zA-Z0-9.,()#+/\-]"," ",text)                #removes unwanted spl caharacters
    text = re.sub(r"\s+"," ",text)                                  # again removing extra spaces
    text = text.strip()                                             # removing trailing and ending spaces
    return text




# In[49]:





# ### So finally our content became little bit ok for our ai engine.

# In[ ]:




