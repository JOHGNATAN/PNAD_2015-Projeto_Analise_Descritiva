#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/dados.csv')
dados['Altura'] = dados['Altura'].round(2)
dados.head()


# 
# O primeiro passo em um trabalho de análise é o conhecimento do comportamento das variáveis envolvidas no estudo. Utilizando técnicas estatísticas como as análises das <b>DISTRIBUIÇÕES DE FREQUÊNCIAS</b> para avaliar melhor a forma como os fenômenos em estudo se distribuem.

# In[3]:



cod_gen = [0, 1]
desc_gen = ['Masculino',
            'Feminino']
sexo = dict(zip(cod_gen, desc_gen))

cod_skin_color = [0,2,4,6,8,9]
desc_skin_color = ['Indígena',
        'Branca',
        'Preta',
        'Amarela',
        'Parda',
        'Sem declaração']

cor = dict(zip(cod_skin_color, desc_skin_color))

frequencia = pd.crosstab(dados.Sexo,
                         dados.Cor)

frequencia.rename(index = sexo, inplace = True)
frequencia.rename(columns = cor, inplace = True)
frequencia


# In[6]:


# PERCENTUAL (%) POR COR

percentual = pd.crosstab(dados.Sexo,
                         dados.Cor,
                         normalize = True) * 100
percentual.rename(index = sexo, inplace = True)
percentual.rename(columns = cor, inplace = True)
percentual.round(2)


# In[7]:


# MÉDIA SALARIAL POR COR

media_salarial = pd.crosstab(dados['Sexo'], dados.Cor, 
                             aggfunc = 'mean',
                             values = dados.Renda)
media_salarial.rename(columns = cor, inplace = True)
media_salarial.rename(index = sexo, inplace = True)
media_salarial.round(2)


# In[21]:



# ESTRATIFICAÇÃO SOCIAL

classes = [0, 1573, 3152, 7880, 15760, 200000]
labels = ['E', 'D', 'C', 'B', 'A']

freq_= pd.value_counts(pd.cut(x = dados['Renda'],
       bins = classes,
       labels = labels,
       include_lowest = True))


percentual = pd.value_counts(pd.cut(x = dados['Renda'],
       bins = classes,
       labels = labels,
       include_lowest = True), normalize = True)*100


tabela = pd.concat([freq_,percentual], axis = 1)

tabela.columns = ['Frequência', 'Porcentagem (%)']
tabela.columns.name = 'Classes'

tabela.sort_index(ascending = False).round(2)


# In[ ]:




