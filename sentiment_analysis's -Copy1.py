#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install textblob


# In[3]:


from textblob import TextBlob


# In[6]:


def analysis(sentance):
    blob=TextBlob(sentance)
    
    sentiment=blob.sentiment
    print(f"Polarity of sentence: {sentiment.polarity:.2f}")
    print(f"Subjectivity of sentence: {sentiment.subjectivity:.2f}")
    
    if sentiment.polarity>0:
        print("Sentiment of sentence : It is a positive sentance")
    elif sentiment.polarity<0:
        print("Sentiment of sentence: It is a negative sentence")
    else:
        print("Sentiment of sentence: It is a neutral sentence")
        
analysis_text=input("Enter a sentence: ")
analysis(analysis_text)
            


# In[ ]:




