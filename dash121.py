#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://github.com/nickefy/advance-guide-to-data-visualization-with-plotly/blob/master/Advance%20Guide%20to%20Data%20Visualization%20with%20Plotly.ipynb
#https://towardsdatascience.com/python-for-data-science-advance-guide-to-data-visualization-with-plotly-8dbeaedb9724
import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np 
import plotly.graph_objs as go
import emoji
import pandas as pd
import plotly
from plotly.offline import iplot
from plotly.offline import init_notebook_mode, iplot


# In[2]:


df_etat = pd.ExcelFile(r"C:\Users\Naim\Documents\suivie_24_06_2020.xlsx")
df= df_etat.parse(0)


df


# In[3]:


#all plotly
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objects as go
import cufflinks as cf
init_notebook_mode(connected=True)
#others
import pandas as pd
import numpy as np
import plotly.express as px


# In[4]:



genders = list(df['ENQ'].unique())
data = []
list_updatemenus = []
for n, gender in enumerate(genders):
    visible = [False] * len(genders)
    visible[n] = True
    temp_dict = dict(label = str(gender),
                 method = 'update',
                 args = [{'visible': visible},
                         {'title': 'ENQUTEUR ' + str(gender)}])
    list_updatemenus.append(temp_dict)



list_updatemenus


# In[44]:


fig = px.scatter(df,  y="QID",
                 hover_data=[ 'ENQ',
                 'remarque_durés',]
)

buttonlist = []
for col in df.columns:
    buttonlist.append(
      dict(
          args=['y',[df[str(col)]] ],
          label=str(col),
          method='restyle'
      )
    )

fig.update_layout(
      title="Test data",
      yaxis_title="c",
      xaxis_title="QID",
      # Add dropdown
      updatemenus=[
          go.layout.Updatemenu(
              buttons=buttonlist,
              direction="down",
              pad={"r": 10, "t": 10},
              showactive=True,
              x=0.1,
              xanchor="left",
              y=1.1,
              yanchor="top"
          ),
      ],
      autosize=True
  )


fig.show()




# In[15]:


from plotly.offline import iplot 


# In[ ]:





# In[43]:



continents = list(df.remarque_durés.unique())
years = sorted(list(df.code_enq.unique()))
data = []
list_updatemenus = []
for n, year in enumerate(years):
    visible = [False] * len(years)
    visible[n] = True
    temp_dict = dict(label = str(year),
                 method = 'update',
                 args = [{'visible': visible},
                         {'title': year}])
    list_updatemenus.append(temp_dict)
    
for n, cont in enumerate(continents):
    for year in years:
        mask = (df.code_enq.values == year) & (df.remarque_durés.values == cont)
        trace = (dict(visible = False,
            text = df.ENQ[mask],      
            name = cont,
            y = df.loc[mask, 'duration'],
            x = df.loc[mask, 'Date_submission'],
            mode = 'markers',
            marker = dict(size = df.loc[mask, 'duration']*0.5))
                   )
        data.append(trace)
    data[int(n*len(years))]['visible'] = True
    
layout = dict(updatemenus=list([dict(buttons= list_updatemenus)]),
              xaxis=dict(title = 'Date_submission', range=[-0.05, max(str(df.loc[:, 'Date_submission'])) + str(0.1)]),
              yaxis=dict(title = 'Duré', range=[-0.1, max(str(df.loc[:, 'duration']))+str(0.1)]),
              title='Duré' )
fig = dict(data=data, layout=layout)
#iplot(fig, filename='update_dropdown')
fig.show() 

# In[ ]:




