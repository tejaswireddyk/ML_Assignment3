#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
vec=np.random.randint(low=1,high=21,size=15)
print (vec)
arr = vec.reshape(3,5)
print("Array shape:",arr.shape)
print(arr)

arr[np.arange(len(arr)),arr.argmax(axis=1)]=0
print(arr)


# In[13]:


arr=np.array([[3,-2],[1,0]])
print(arr)
eig_vals, eig_vecs =np.linalg.eig(arr)
print("Eigen values: ", eig_vals)
print("Right Eigen vectors: ",eig_vecs)


# In[30]:


arr=np.array([[0,1,2],[3,4,5]])
print(arr)
a= sum(np.diag(arr,k=0))
print(a)


# In[24]:


arr=np.array([[1,2],[3,4],[5,6]])
print(arr)
a= arr.reshape(2,3)
print(a)


# In[3]:


import matplotlib.pyplot as plt
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1, 0, 0, 0,0,0)  
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%',shadow=True, startangle=140)
plt.axis('equal')
plt.show()


# In[ ]:




