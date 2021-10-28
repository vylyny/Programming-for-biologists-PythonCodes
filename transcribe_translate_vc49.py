
# coding: utf-8

# In[18]:


import seq_tools_vc49 as vc


# In[ ]:


##############################################for "one_nt_seqs.fa" file ############


# In[19]:


f_one=vc.load_fasta("one_nt_seq.fa")


# In[20]:


print(vc.get_reverse_complement(f_one))


# In[21]:


print(vc.get_transcript(f_one))


# In[22]:


print(vc.get_translate(f_one,True))


# In[23]:


print(vc.get_translate(f_one,False))


# In[ ]:


############################################################## for "multiple_nt_seqs.fa"##################


# In[32]:


f_multiple=vc.load_fasta("multiple_nt_seqs.fa")
print(f_multiple)


# In[25]:


type(f_multiple)


# In[26]:


print(vc.get_reverse_complement(f_multiple))


# In[27]:


print(vc.get_transcript(f_multiple))


# In[28]:


print(vc.get_translate(f_multiple,True))


# In[29]:


print(vc.get_translate(f_multiple,False))

