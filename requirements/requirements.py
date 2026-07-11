#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np


# ## 1. Creating job requirements for each domain :

# In[13]:


Domains = [
    "Data Scientist",
    "Data Analyst",
    "Front-End Developer",
    "Full Stack Developer",
    "Python Developer"
]

Description = [

"""We are seeking a motivated Data Scientist to join our team. Candidates should have strong knowledge of Python, SQL, Statistics, Machine Learning, Data Preprocessing, Exploratory Data Analysis (EDA), and Natural Language Processing (NLP). Familiarity with Scikit-learn, Pandas, NumPy, Matplotlib, and model evaluation techniques is preferred. Candidates should possess strong analytical thinking, problem-solving skills, attention to detail, teamwork, and proficiency in English with excellent written and verbal communication skills.""",

"""We are hiring a Data Analyst with strong analytical and problem-solving abilities. Candidates should be proficient in SQL, Python, Excel, Power BI, data visualization, dashboard development, and statistical analysis. Knowledge of data cleaning, business intelligence, reporting, KPI analysis, and exploratory data analysis is expected. Familiarity with Pandas, NumPy, and DAX is an added advantage. Excellent communication skills, attention to detail, teamwork, and proficiency in English are mandatory.""",

"""We are looking for a Front-End Developer with a strong understanding of HTML, CSS, JavaScript, responsive web design, and modern UI development. Experience with React.js, Bootstrap, REST APIs, Git, and version control is preferred. Candidates should have knowledge of UI/UX principles, cross-browser compatibility, debugging, and responsive layouts. Strong problem-solving abilities, creativity, teamwork, and proficiency in English are essential.""",

"""We are seeking a Full Stack Developer with knowledge of both front-end and back-end technologies. Candidates should be proficient in HTML, CSS, JavaScript, React.js, Node.js, Express.js, MongoDB, SQL, REST APIs, and Git. Understanding of authentication, database management, debugging, software development practices, and deployment concepts is preferred. Strong communication skills, teamwork, analytical thinking, and proficiency in English are required.""",

"""We are hiring a Python Developer with strong programming and logical reasoning skills. Candidates should have experience with Python, Object-Oriented Programming (OOP), SQL, APIs, data structures, and database management. Familiarity with Flask, Django, Pandas, NumPy, debugging, version control using Git, and software development best practices is preferred. Candidates should demonstrate problem-solving ability, teamwork, adaptability, and proficiency in English with excellent communication skills."""

]

Required_Skills = [
    "Python, SQL, Machine Learning, Statistics, Pandas, NumPy, Scikit-learn, NLP",
    
    "Python, SQL, Excel, Power BI, Statistics, Pandas, NumPy, DAX",
    
    "HTML, CSS, JavaScript, React.js, Bootstrap, REST API, Git",
    
    "HTML, CSS, JavaScript, React.js, Node.js, Express.js, MongoDB, SQL, REST API, Git",
    
    "Python, OOP, SQL, Flask, Django, REST API, Pandas, NumPy, Git"
]


# In[14]:


Description_data = pd.DataFrame(
    {
    "Domain" : Domains,
    "Description" : Description,
    "Required_skills" : Required_Skills
    },
)


# In[15]:


Description_data


# In[18]:


Requirements = Description_data.to_csv("Requirement.csv",index=False  )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




