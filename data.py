import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv('data.csv')
studentDf = df.loc[df['student_id']=='TRL_xyz']
print(studentDf.groupby('level')['attempt'].mean())
fig = px.bar(studentDf,x=studentDf.groupby('level')['attempt'].mean(),
            y=['Level 1','Level 2','Level 3','Level 4'],
            orientation='h')
fig.show()