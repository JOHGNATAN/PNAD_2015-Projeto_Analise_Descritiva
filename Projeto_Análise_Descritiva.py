#!/usr/bin/env python
# coding: utf-8

# # <font color=green>DATASET DO PROJETO</font>
# ***

# ### Pesquisa Nacional por Amostra de Domicílios - 2015
# 
# A <b>Pesquisa Nacional por Amostra de Domicílios - PNAD</b> investiga anualmente, de forma permanente, características gerais da população, de educação, trabalho, rendimento e habitação e outras, com periodicidade variável, de acordo com as necessidades de informação para o país, como as características sobre migração, fecundidade, nupcialidade, saúde, segurança alimentar, entre outros temas. O levantamento dessas estatísticas constitui, ao longo dos 49 anos de realização da pesquisa, um importante instrumento para formulação, validação e avaliação de políticas orientadas para o desenvolvimento socioeconômico e a melhoria das condições de vida no Brasil.

# ### Fonte dos Dados
# 
# https://ww2.ibge.gov.br/home/estatistica/populacao/trabalhoerendimento/pnad2015/microdados.shtm

# ### Variáveis utilizadas
# 
# > ### Renda
# > ***
# 
# Rendimento mensal do trabalho principal para pessoas de 10 anos ou mais de idade.
# 
# > ### Idade
# > ***
# 
# Idade do morador na data de referência em anos.
# 
# > ### Altura (elaboração própria)
# > ***
# 
# Altura do morador em metros.
# 
# > ### UF
# > ***
# 
# |Código|Descrição|
# |---|---|
# |11|Rondônia|
# |12|Acre|
# |13|Amazonas|
# |14|Roraima|
# |15|Pará|
# |16|Amapá|
# |17|Tocantins|
# |21|Maranhão|
# |22|Piauí|
# |23|Ceará|
# |24|Rio Grande do Norte|
# |25|Paraíba|
# |26|Pernambuco|
# |27|Alagoas|
# |28|Sergipe|
# |29|Bahia|
# |31|Minas Gerais|
# |32|Espírito Santo|
# |33|Rio de Janeiro|
# |35|São Paulo|
# |41|Paraná|
# |42|Santa Catarina|
# |43|Rio Grande do Sul|
# |50|Mato Grosso do Sul|
# |51|Mato Grosso|
# |52|Goiás|
# |53|Distrito Federal|
# 
# > ### Sexo	
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Masculino|
# |1|Feminino|
# 
# > ### Anos de Estudo
# > ***
# 
# |Código|Descrição|
# |---|---|
# |1|Sem instrução e menos de 1 ano|
# |2|1 ano|
# |3|2 anos|
# |4|3 anos|
# |5|4 anos|
# |6|5 anos|
# |7|6 anos|
# |8|7 anos|
# |9|8 anos|
# |10|9 anos|
# |11|10 anos|
# |12|11 anos|
# |13|12 anos|
# |14|13 anos|
# |15|14 anos|
# |16|15 anos ou mais|
# |17|Não determinados| 
# ||Não aplicável|
# 
# > ### Cor
# > ***
# 
# |Código|Descrição|
# |---|---|
# |0|Indígena|
# |2|Branca|
# |4|Preta|
# |6|Amarela|
# |8|Parda|
# |9|Sem declaração|

# #### <font color='red'>Observação</font>
# ***
# > Os seguintes tratamentos foram realizados nos dados originais:
# > 1. Foram eliminados os registros onde a <b>Renda</b> era inválida (999 999 999 999);
# > 2. Foram eliminados os registros onde a <b>Renda</b> era missing;
# > 3. Foram considerados somente os registros das <b>Pessoas de Referência</b> de cada domicílio (responsável pelo domicílio).

# ***
# ***

# ### Utilize a célula abaixo para importar as biblioteca que precisar para executar as tarefas
# #### <font color='red'> pandas, numpy, seaborn</font>

# In[169]:


import pandas as pd 
import numpy as np
import seaborn as sns


# ### Importe o dataset e armazene o conteúdo em uma DataFrame

# In[170]:


dados = pd.read_csv("C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/dados.csv", sep = ',')


# ### Visualize o conteúdo do DataFrame

# In[171]:


dados.head()


# ### Para avaliarmos o comportamento da variável RENDA vamos construir uma tabela de frequências considerando as seguintes classes em salários mínimos (SM)
# #### <font color='blue'>Descreva os pontos mais relevantes que você observa na tabela e no gráfico.</font>
# 
# Classes de renda:
# 
# <b>A</b> ► Acima de 25 SM
# 
# <b>B</b> ► De 15 a 25 SM
# 
# <b>C</b> ► De 5 a 15 SM
# 
# <b>D</b> ► De 2 a 5 SM
# 
# <b>E</b> ► Até 2 SM
# 
# Para construir as classes de renda considere que o salário mínimo na época da pesquisa era de <b>R$ 788,00</b>.
# 
# #### Siga os passos abaixo:

# ### 1º Definir os intevalos das classes em reais (R$)

# In[172]:


classes = [dados.Renda.min(),
           2 * 788,
           5 * 788,
           15 * 788,
           25 * 788,
           dados['Renda'].max()]
classes


# ### 2º Definir os labels das classes

# In[173]:


labels = ['E', 'D', 'C', 'B', 'A']


# ### 3º Construir a coluna de frequências

# In[174]:


freq = pd.value_counts(pd.cut(x = dados['Renda'],
       bins = classes,
       labels = labels,
       include_lowest = True))
freq


# ### 4º Construir a coluna de percentuais

# In[175]:


percentual = pd.value_counts(pd.cut(x = dados['Renda'],
                                    bins = classes,
                                    labels = labels,
                                    include_lowest = True), normalize = True)*100
percentual


# ### 5º Juntar as colunas de frequência e percentuais e ordenar as linhas de acordo com os labels das classes

# In[176]:



report = pd.concat([freq, percentual], axis = 1)
report.columns = ['Frequência', 'Percentual (%)']

report


# ### Construa um gráfico de barras para visualizar as informações da tabela de frequências acima

# In[177]:


report['Frequência'].plot.bar(width = 1 ,
                              color = 'blue',
                              alpha = 0.5,
                              figsize = (14,6))


# ### Crie um histograma para as variáveis QUANTITATIVAS de nosso dataset
# 

# In[178]:


ax = sns.distplot(dados['Altura'])
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências - Altura', fontsize = 18)
ax.set_xlabel('Metros', fontsize = 18)
ax


# In[179]:


ax = sns.distplot(dados.Idade)
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequência - Idade', fontsize = 18)
ax.set_xlabel('Anos', fontsize = 18)
ax


# In[180]:


ax = sns.distplot(dados['Renda'])
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências - Renda', fontsize = 18)
ax.set_xlabel('R$', fontsize = 18)
ax


# ### Para a variável RENDA, construa um histograma somente com as informações das pessoas com rendimento até R$ 20.000,00

# In[181]:


ax = sns.distplot(dados.query('Renda < 20000')['Renda'])
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências - RENDA - Pessoas com renda até R$20.000,00', fontsize = 18)
ax.set_xlabel('R$', fontsize = 14)
ax


# In[182]:


selecao = (dados.Renda < 20000)
hist_de_ate_20 = dados[selecao]
histograma = hist_de_ate_20.hist(['Renda'], alpha = 0.5)


# ### Construa uma tabela de frequências e uma com os percentuais do cruzando das variáveis SEXO e COR
# 
# #### <font color='red'>Utilize os dicionários abaixo para renomear as linha e colunas das tabelas de frequências e dos gráficos em nosso projeto</font>

# In[183]:


sexo = {
    0: 'Masculino', 
    1: 'Feminino'
}
cor = {
    0: 'Indígena', 
    2: 'Branca', 
    4: 'Preta', 
    6: 'Amarela', 
    8: 'Parda', 
    9: 'Sem declaração'
}
anos_de_estudo = {
    1: 'Sem instrução e menos de 1 ano', 
    2: '1 ano', 
    3: '2 anos', 
    4: '3 anos', 
    5: '4 anos', 
    6: '5 anos', 
    7: '6 anos', 
    8: '7 anos', 
    9: '8 anos', 
    10: '9 anos', 
    11: '10 anos', 
    12: '11 anos', 
    13: '12 anos', 
    14: '13 anos', 
    15: '14 anos', 
    16: '15 anos ou mais', 
    17: 'Não determinados'
}
uf = {
    11: 'Rondônia', 
    12: 'Acre', 
    13: 'Amazonas', 
    14: 'Roraima', 
    15: 'Pará', 
    16: 'Amapá', 
    17: 'Tocantins', 
    21: 'Maranhão', 
    22: 'Piauí', 
    23: 'Ceará', 
    24: 'Rio Grande do Norte', 
    25: 'Paraíba', 
    26: 'Pernambuco', 
    27: 'Alagoas', 
    28: 'Sergipe', 
    29: 'Bahia', 
    31: 'Minas Gerais', 
    32: 'Espírito Santo', 
    33: 'Rio de Janeiro', 
    35: 'São Paulo', 
    41: 'Paraná', 
    42: 'Santa Catarina', 
    43: 'Rio Grande do Sul', 
    50: 'Mato Grosso do Sul', 
    51: 'Mato Grosso', 
    52: 'Goiás', 
    53: 'Distrito Federal'
}


# In[184]:


tabela_freq = pd.crosstab(dados.Sexo, dados['Cor'])
tabela_freq.rename(index = sexo, columns = cor, inplace = True)
tabela_freq


# In[185]:


tabela_percentual = pd.crosstab(dados['Sexo'],
                                dados.Cor,
                                normalize = True)* 100
tabela_percentual.rename(index = sexo, columns = cor, inplace = True)
tabela_percentual.round(2)


# ## Realize, para a variável RENDA, uma análise descritiva com as ferramentas que aprendemos em nosso treinamento

# ### Obtenha a média aritimética

# In[186]:


dados.mean()


# ### Obtenha a mediana

# In[187]:


dados.median()


# ### Obtenha a moda

# In[188]:


dados.Renda.mode()[0]


# ### Obtenha o desvio médio absoluto

# In[189]:


dados.mad()


# ### Obtenha a variância

# In[190]:


dados.var()


# ### Obtenha o desvio-padrão

# In[191]:


dados.Renda.std()


# ### Obtenha a média, mediana e valor máximo da variável RENDA segundo SEXO e COR
# 

# In[192]:


# máximo da variável RENDA

research_max = pd.crosstab(dados.Cor, dados['Sexo'], aggfunc = {'max','mean','median'}, values = dados.Renda)
research_max.rename(columns = sexo, inplace =True)
research_max.rename(index = cor, inplace =True)
research_max


# ### Obtenha as medidas de dispersão da variável RENDA segundo SEXO e COR
# 

# In[193]:


#  desvio médio absoluto

desvio_med = pd.crosstab(dados.Cor, dados['Sexo'],
                         aggfunc = {'mad','var','std'},
                         values = dados.Renda)
desvio_med.rename(columns = sexo, index = cor, inplace = True)
desvio_med


# ### Construa um box plot da variável RENDA segundo SEXO e COR
# 
# #### <font color='red'> Pessoas com renda abaixo de R$ 10.000</font>
# 
# 

# In[194]:


selecao = (dados.Renda < 10000)
box_de_ate_10 = dados[selecao]


ax = sns.boxplot(x = 'Renda', y = 'Sexo',data = box_de_ate_10, orient = 'h')
ax.figure.set_size_inches(12,4)
ax.set_title('Renda abaixo de R$ 10.000', fontsize = 18)
ax.set_xlabel('Renda', fontsize = 14)
ax.set_yticklabels(['Masculino','Feminino'], fontsize = 12)
ax


# In[195]:


cor = {
    0: 'Indígena', 
    2: 'Branca', 
    4: 'Preta', 
    6: 'Amarela', 
    8: 'Parda', 
    9: 'Sem declaração'}
cor.values()


# In[196]:


# Construa um box plot da variável RENDA segundo SEXO e COR

selecao = (dados.Renda < 10000)
box_de_ate_10 = dados[selecao]


ax = sns.boxplot(x = 'Renda', y= 'Cor',
                 data = box_de_ate_10,
                 hue = 'Sexo',  orient = 'h')
ax.figure.set_size_inches(12,6)   # Tamanho da figura
ax.set_title('Renda abaixo de R$ 10.000',
             fontsize = 18)   # Configurando título do gráfico
ax.set_xlabel('R$', fontsize = 14)   # Configurando o label do eixo X

ax.set_ylabel('Cor', fontsize = 14) # Configurando o label do eixo Y
ax.set_yticklabels(['Indígena', 'Branca', 'Preta', 'Amarela', 'Parda'],
                   fontsize=12)

handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, ['Masculino', 'Feminino'], fontsize = 14)

ax


# 
# ### Qual percentual de pessoas de nosso <i>dataset</i> ganham um salário mínimo (R$ 788,00) ou menos?
# 
# #### Mais informações: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.percentileofscore.html
# 

# In[197]:


from scipy import stats

percentual = stats.percentileofscore(dados.Renda, 788, kind = 'weak')


# dentro de percentileofscore() seguido de 3, que seria o valor de corte por exemplo. Então o resultado será 70%.
# 
# Quando usamos o kind como 'strict' da mesma lista e corte, o resultado será 40%, pois informa que somente o que está abaixo do valor de corte.
# 
# O 'weak' que usamos já inclui o valor, pois queremos uma renda menor ou igual a um salário mínimo. No exemplo, o resultado é 80%.
# 
# Já o 'mean' identifica a mediana. É interessante começarmos a lidar com a biblioteca scipy, pois é bastante útil.

# ### Qual o valor máximo ganho por 99% das pessoas de nosso <i>dataset</i>?
# #### <font color='red'>Utilize o método <i>quantile()</i> do <i>pandas</i> para realizar estas análises.</font>

# In[198]:


dados['Renda'].quantile(0.99)


# ### Obtenha a média, mediana, valor máximo e desvio-padrão da variável RENDA segundo ANOS DE ESTUDO e SEXO
# #### <font color='blue'>Destaque os pontos mais importante que você observa nas tabulações</font>
# #### <font color='red'>O parâmento <i>aggfunc</i> da função <i>crosstab()</i> pode receber uma lista de funções. Exemplo: <i>aggfunc = ['mean', 'median', 'max', 'std']</i></font>

# In[ ]:





# In[199]:


# média, mediana, valor máximo e desvio-padrão da variável RENDA segundo ANOS DE ESTUDO e SEXO
anos_estudos = pd.crosstab(dados['Anos de Estudo'], dados.Sexo, aggfunc = ['mean', 'median', 'max', 'std'], values = dados.Renda)
anos_estudos.rename(index = anos_de_estudo, inplace = True)
anos_estudos.rename(columns = sexo, inplace = True)
anos_estudos


# ### Construa um box plot da variável RENDA segundo ANOS DE ESTUDO e SEXO
# 
# #### <font color='red'>1º - Pessoas com renda abaixo de R$ 10.000</font>
# #### <font color='red'>2º - Utilize a variável IDADE para identificar se a desigualdade se verifica para pessoas de mesma idade. Exemplo: <i>Renda < 10000 and Idade == 40</i> ou <i>Renda < 10000 and Idade == 50</i></font>
# 
# 

# In[200]:


ax = sns.boxplot(x = 'Renda',
               y = 'Anos de Estudo',
               hue = 'Sexo',
               data = dados.query('Renda < 10000 and Idade == 50'),
               orient = 'h')

ax.figure.set_size_inches(14,10)

ax.set_title('Box-Plot da RENDA por SEXO e ANOS DE ESTUDO', fontsize = 18)

ax.set_xlabel('RENDA', fontsize = 14)

ax.set_yticklabels([key for key in anos_de_estudo.values()], fontsize = 15)

handles, _ = ax.get_legend_handles_labels()

ax.legend(handles, ['Masculino', 'Feminino'], fontsize = 14)

ax


# ### Obtenha a média, mediana, valor máximo e desvio-padrão da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# 

# In[201]:


# modo 1 de visualizar usando a função GROUPBY().AGG({})

report_20230223 = dados.groupby('UF').agg({'Renda':['mean', 'median', 'max', 'std']})
report_20230223.rename(index = uf,inplace = True)
report_20230223.head()


# In[202]:


# modo 2 de visualizar usando a função CROSSTAB e AGGFUNC[]

report_20230224 = pd.crosstab(dados.UF, dados.Sexo,
                              aggfunc = ['mean','median', 'max', 'std'],
                              values = dados['Renda'])
report_20230224.rename(index = uf,columns = sexo, inplace = True)
report_20230224.round(2)


# ### Construa um box plot da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# 

# In[203]:


selecao1 = (dados['Renda'] < 10000) 
report_renda_filter_20230223 = dados[selecao1]

ax = sns.boxplot(x = 'Renda',
                 y = 'UF',
                 data = report_renda_filter_20230223,
                 orient = 'h')
ax.figure.set_size_inches(14,12)
ax.set_title(' RENDA segundo as UNIDADES DA FEDERAÇÃO',fontsize = 18)
ax.set_xlabel('Renda',fontsize = 18)
ax.set_ylabel('UF', fontsize = 20)
ax.set_yticklabels([key for key in uf.values()], fontsize = 16)
ax


# In[ ]:




