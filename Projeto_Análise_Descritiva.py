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

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns


# In[2]:


dados = pd.read_csv("C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/dados.csv",
                    sep = ',')
dados.head()


# ### Para avaliarmos o comportamento da variável RENDA vamos construir uma tabela de frequências considerando as seguintes classes em salários mínimos (SM)
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
# Salário mínimo <b>R$ 788,00</b>.
# 
# 

# <p> O código analisa a distribuição de renda de uma determinada população e cria um relatório que apresenta a frequência e o percentual de pessoas em cada classe de renda. Para isso, o código define intervalos de renda pré-determinados e atribui rótulos a cada classe. </p>

# In[4]:


classes = [dados.Renda.min(),
           2 * 788,
           5 * 788,
           15 * 788,
           25 * 788,
           dados['Renda'].max()]
classes


# In[5]:


labels = ['E', 'D', 'C', 'B', 'A']


# <p>Em seguida, criamos a frequência de renda em cada classe, e um novo conjunto de dados é criado para mostrar o percentual de pessoas em cada classe. </p>

# In[6]:


freq = pd.value_counts(pd.cut(x = dados['Renda'],
       bins = classes,
       labels = labels,
       include_lowest = True))
freq


# In[7]:


percentual = pd.value_counts(pd.cut(x = dados['Renda'],
                                    bins = classes,
                                    labels = labels,
                                    include_lowest = True), normalize = True)*100
percentual


# <p>Por fim, um dataframe é criado para armazenar as informações de frequência e percentual em cada classe de renda, e é utilizado para gerar um relatório final sobre a distribuição de renda da população em questão.</p>

# In[11]:



report = pd.concat([freq, percentual], axis = 1)
report.columns = ['Frequência', 'Percentual (%)']

report


# In[177]:


report['Frequência'].plot.bar(width = 1 ,
                              color = 'blue',
                              alpha = 0.5,
                              figsize = (14,6))


# <li>O gráfico apresenta a frequência de pessoas em cada classe de renda. O objetivo é apresentar visualmente a distribuição de renda da população em questão.</li>
# 
# 

# ### Histograma para as variáveis QUANTITATIVAS de nosso dataset
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


# ### Para a variável RENDA, vamos criar um histograma com as informações das pessoas com rendimento até R$ 20.000,00

# In[14]:


ax = sns.distplot(dados.query('Renda < 20000')['Renda'])
ax.figure.set_size_inches(14,6)
ax.set_title('Distribuição de Frequências - RENDA - Pessoas com renda até R$20.000,00', fontsize = 18)
ax.set_xlabel('R$', fontsize = 14)
ax


# In[16]:


selecao = (dados.Renda < 20000)
hist_de_ate_20 = dados[selecao]
histograma = hist_de_ate_20.hist(['Renda'], alpha = 0.5)


# <li>O código define quatro dicionários que serão utilizados para mapear valores de variáveis categóricas em seus respectivos rótulos. O primeiro dicionário, "sexo", associa o valor <strong>0</strong> a <strong>"Masculino"</strong> e o valor <strong>1</strong> a <strong>"Feminino"</strong>. O segundo dicionário, "cor", mapeia os valores <strong>0, 2, 4, 6</strong> e <strong>8</strong> em <strong>"Indígena", "Branca", "Preta", "Amarela"</strong> e <strong>"Parda"</strong>, respectivamente. O terceiro dicionário, <strong>"anos_de_estudo"</strong>, associa os números de <strong>1 a 17</strong> a descrições de anos de estudo. Por fim, o dicionário <strong>"UF"</strong> mapeia os valores dos códigos das unidades federativas do Brasil em seus respectivos nomes. A utilização desses dicionários é útil para dar significado aos valores categóricos em um conjunto de dados e para facilitar a análise e interpretação dos resultados.</li>

# In[19]:


sexo = {
    0: 'Masculino', 
    1: 'Feminino'
}
cor = {
    0: 'Indígena', 
    2: 'Branca', 
    4: 'Preta', 
    6: 'Amarela', 
    8: 'Parda'
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


# <li>Vamos analisar a distribuição de renda e a frequência e percentual de pessoas em diferentes faixas de renda, bem como a distribuição da cor da pele entre homens e mulheres. A análise foi feita por meio de tabelas de frequência e percentual.</li>

# In[20]:


tabela_freq = pd.crosstab(dados.Sexo, dados['Cor'])
tabela_freq.rename(index = sexo, columns = cor, inplace = True)
tabela_freq


# In[21]:


tabela_percentual = pd.crosstab(dados['Sexo'],
                                dados.Cor,
                                normalize = True)* 100
tabela_percentual.rename(index = sexo, columns = cor, inplace = True)
tabela_percentual.round(2)


# ## Análise descritiva para a variável RENDA

# ### Média aritimética

# In[22]:


dados['Renda'].mean()


# ### Mediana

# In[23]:


dados['Renda'].median()


# ### Moda

# In[24]:


dados.Renda.mode()[0]


# ### Desvio médio absoluto

# In[25]:


dados['Renda'].mad()


# ### Variância

# In[26]:


dados['Renda'].var()


# ### Desvio-padrão

# In[27]:


dados.Renda.std()


# <p> Estamos analisando a renda máxima, média e mediana de acordo com a cor e o sexo dos entrevistados. A tabela resultante mostra esses valores agregados para cada combinação de cor e sexo.</p>
# 

# In[28]:



research_max = pd.crosstab(dados.Cor, dados['Sexo'], aggfunc = ['max','mean','median'], values = dados.Renda)
research_max.rename(columns = sexo, inplace =True)
research_max.rename(index = cor, inplace =True)
research_max


# 
# <li>Nesta análise vamos calcular as medidas de dispersão (Desvio Médio Absoluto - MAD, Variância e Desvio Padrão) da renda por cor e sexo. Os resultados são apresentados em uma tabela, onde as linhas correspondem às diferentes cores e as colunas correspondem aos diferentes sexos.</li>

# In[193]:



desvio_med = pd.crosstab(dados.Cor, dados['Sexo'],
                         aggfunc = {'mad','var','std'},
                         values = dados.Renda)
desvio_med.rename(columns = sexo, index = cor, inplace = True)
desvio_med


# <li>Nesta análise, estamos visualizando um gráfico de caixa que compara a renda de pessoas de diferentes cores e gêneros, mas apenas para aqueles com renda abaixo de R$ 10.000. O gráfico mostra a distribuição de renda em cada grupo, destacando as diferenças entre eles. As cores representam as diferentes etnias e os pontos indicam valores extremos (outliers).</li>

# In[196]:



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
# <li>Estamos analisando o percentual de indivíduos que possuem renda igual ou inferior a <strong>788,00</strong> em relação ao total de observações. O resultado é apresentado como uma porcentagem.</li>

# In[32]:


from scipy import stats

percentual = stats.percentileofscore(dados.Renda, 788, kind = 'weak')
percentual


# ### Qual o valor máximo ganho por 99% das pessoas de nosso <i>dataset</i>?
# 

# In[33]:


dados['Renda'].quantile(0.99)


# <p>Vamos realizar uma análise de dados a partir da tabela dados, apresentando informações sobre a média, mediana, valor máximo e desvio padrão da renda de indivíduos de diferentes gêneros e anos de estudo. A análise é dividida por cor/raça e apresentada por meio de tabelas de frequência e porcentagens, gráficos de boxplot e crosstabs. O objetivo é obter informações sobre a distribuição de renda de diferentes grupos e suas relações com variáveis como gênero, cor/raça e anos de estudo.</p>

# In[44]:


anos_estudos = pd.crosstab(dados['Anos de Estudo'], dados.Sexo, aggfunc = ['mean',
                                                                           'median',
                                                                           'max',
                                                                           'std'],
                           values = dados.Renda)
anos_estudos.rename(index = anos_de_estudo, inplace = True)
anos_estudos.rename(columns = sexo, inplace = True)
anos_estudos


# <p>Criando um gráfico box-plot que analisa a renda por sexo e anos de estudo de indivíduos com idade igual a 50 anos e renda inferior a R$ 10.000. A figura apresenta a mediana, os quartis, e os valores mínimo e máximo para cada categoria, separados por sexo. Além disso, a legenda indica qual cor representa cada sexo. O eixo X indica a renda e o eixo Y, o número de anos de estudo.</p>

# In[52]:


ax = sns.boxplot(x = 'Renda',
               y = 'Anos de Estudo',
               hue = 'Sexo',
               data = dados.query('Renda < 10000 and Idade == 50'),
               orient = 'h')

ax.figure.set_size_inches(14,10)

ax.set_title('Box-Plot da RENDA por SEXO e ANOS DE ESTUDO', fontsize = 18)

ax.set_xlabel('RENDA', fontsize = 14)
ax.set_ylabel('Anos de Estudo', fontsize = 18)
ax.set_yticklabels([key for key in anos_de_estudo.values()], fontsize = 15)

handles, _ = ax.get_legend_handles_labels()

ax.legend(handles, ['Masculino', 'Feminino'], fontsize = 14)

ax


# ### Obtendo a média, mediana, valor máximo e desvio-padrão da variável RENDA segundo as UNIDADES DA FEDERAÇÃO
# 

# In[201]:


# modo 1 de visualizar usando a função GROUPBY().AGG({})

report_20230223 = dados.groupby('UF').agg({'Renda':['mean', 'median', 'max', 'std']})
report_20230223.rename(index = uf, inplace = True)
report_20230223.head()


# In[202]:


# modo 2 de visualizar usando a função CROSSTAB e AGGFUNC[]

report_20230224 = pd.crosstab(dados.UF, dados.Sexo,
                              aggfunc = ['mean','median', 'max', 'std'],
                              values = dados['Renda'])
report_20230224.rename(index = uf, columns = sexo, inplace = True)
report_20230224.round(2)


# ### Nessa análise, vamos plotar um gráfico de boxplot que mostra a distribuição da renda dos indivíduos de diferentes unidades da federação. A seleção é feita apenas para rendas menores do que 10.000 reais.
# <br>
# <li>O objetivo dessa análise é identificar diferenças na distribuição de renda entre as unidades da federação, permitindo comparações entre elas. Essa informação pode ser utilizada, por exemplo, para entender melhor as desigualdades socioeconômicas entre as regiões do país e orientar políticas públicas para reduzir essas desigualdades.</li>

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




