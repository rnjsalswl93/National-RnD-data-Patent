
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np


# In[2]:


data1 = pd.read_excel('2017_Patent.xls')


# In[3]:


j=0
for i in data1['연구개발단계']:
    j+=1
print('데이터 수 :',j)


# In[4]:


cat1=[]
for i in data1['과학기술표준분류코드1-대']:
    cat1.append([])


# In[5]:


j=0
for i in data1['과학기술표준분류코드1-대']:
    cat1[j].append(i)
    j+=1
print(cat1)


# In[6]:


j=0
for i in data1['과학기술표준분류코드2-대']:
    cat1[j].append(i)
    j+=1
print(cat1)


# In[7]:


j=0
for i in data1['과학기술표준분류코드3-대']:
    cat1[j].append(i)
    j+=1
print(cat1)


# In[8]:


#중복 제거
catm1=[]
for i in cat1:
    j=set(i)
    t=list(j)
    catm1.append(t)
print(catm1)


# In[9]:


#nan제거
catmm1=[]
for i in  catm1:
    li=[]
    for j in i:
        if type(j)!=float and j!=0:
            li.append(j)
    catmm1.append(li)

catmm=[]
for i in catmm1:
    catmm.append(i)
print('list 이름 : catmm')
print('총 성과 수 :', len(catmm))
t=0
for i in catmm:
    if len(i)==0:
        t+=1
print('분류 되지않은 수 :', t)
c=0
for i in catmm:
    if len(i)>1:
        c+=1
print('2개 분야 이상 융합 수 :',c)
ccc=0
for i in catmm:
    if len(i)>2:
        ccc+=1
print('3개 분야 이상 융합 수 :', ccc)


# In[10]:


j=1
for i in catmm:
    print(j,i)
    j+=1


# In[11]:


#전체 코드 set
s=[]
for i in catmm:
    for j in i:
        s.append(j)
s=set(s)
s=list(s)
print('대분류 항목 수 :',len(s))
print(s)


# In[12]:


#edge list 초기화
edge=[]
for i in range(0,32):
    for j in range(i+1,33):
        edge.append([s[i],s[j],0])
print(len(edge))
for i in edge:
    print(i)


# In[13]:


j=0
for i in data1['특허수']:
    i=round(i,2)
    catmm[j].append(i)
    j+=1
for i in catmm:
    print(i)


# In[14]:


#edge list
for i in edge:
    for j in catmm:
        if i[0] in j and i[1] in j:
            plus=j[len(j)-1]
            plus=round(plus,2)
            i[2]+=plus
print(edge)


# In[15]:


count=0
for i in edge:
    if i[2]!=0:
        print(i)
        count+=1

