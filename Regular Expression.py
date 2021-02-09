#!/usr/bin/env python
# coding: utf-8

# Regular Expressions (RegEx)

# Channel: Morita DataLand

# Author: Morita Tarvirdians

# In[1]:


import re


# In[2]:


text = '''
This version provides numbered text that is numbered every 50 characters, up to 1000 characters. 
This numbered Latin-looking text works quite well to show the character lengths of your text as you design and set up your page layouts.

Hello. I recognized that you are a computer science student

if you're interested in online video tutorials you can find a lot of educational videos on the YouTube channel bellow:
@Morita DataLand

you can also connect them with this email:
tarvirdians.morita@gmail.com

This is an IP address: 168.212.226.204

another IP: 192.0.2.146

invalid IP: 999.999.999.999

This is a search Engine: https://www.google.com/

This is an Email address: example@example.com

another one: example123@example.com
'''


# In[3]:


# Email Validation

pattern = r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

emails = ["example@example.com", "example123@gmail.com", "example\\@gmail.com", "ab.axa.com", "Ab@gmail@com"]

for item in emails:
    if(re.search(pattern,item)):  
        print(item + " Valid")   
    else:  
        print(item + " Invalid")  


# In[4]:


# find Emails
pattern = r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
result = re.findall(pattern, text)
print(result)


# In[5]:


# find URLs
# https://
# http://
# www.

pattern = r"(?:www|https?)[^\s]+"
result = re.findall(pattern, text)
print(result)


# In[6]:


# find IPs
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
result = re.findall(pattern, text)
result


# In[7]:


# Substitute
pattern_email = r"(?:www|https?)[^\s]+"
pattern_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
pattern_url= r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
pattern_digit = r"[0-9]"

clean_text = re.sub(pattern_email, "", text)
clean_text = re.sub(pattern_ip, "", clean_text)
clean_text = re.sub(pattern_url, "", clean_text)
clean_text = re.sub(pattern_digit, "", clean_text)
print(clean_text)


# In[8]:


# Persian names
pattern = r"^[\u0600-\u06FF\s]+$"
names = ["موریتا", "مور123"]

for item in names:
    if re.search(pattern,item):
        print(item+ " valid")
    else:
        print(item+ " invalid")


# In[ ]:




