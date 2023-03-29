#  http://localhost:8501


import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib as plt
import seaborn as sns


st.title('Portafolio de inversiones S&P500')

st.markdown('***')

st.header('Indicadores S&P500 - hasta marzo 2023')
st.markdown('***')

#st.sidebar.text('barra lateral - seleccionar opciones')

st.subheader('Compañias S&P500')


#---------------------------------------------
#GRAFICAMOS LAS TENDENCIAS DEL MERCADO
#---------------------------------------------

df = pd.read_csv("2GSPC.csv", encoding="UTF8")
st.write(df)

fig = px.line(df, x='Date', y="Adj Close")
fig.update_layout(title='Tendencia del precio cierre ajustado - S&P500',
              xaxis_title='Año',
              yaxis_title='Precio cierre ajustado - Adj Close')
st.write(fig)


#---------------------------------------------
#GRAFICAMOS LAS TENDENCIAS POR SECTORES
#---------------------------------------------

st.subheader('Tendencia por Sectores')

df2 = pd.read_csv("3sp500sectorrendimiento.csv", encoding="UTF8")
st.write(df2)

fig2 = px.bar(df2, x='Sector', y="Adj Close")
st.write(fig2)


#df3 = df2.groupby('Sector')['Adj Close'].sum()

#plt.figure(figsize=(16, 9))
#sns.barplot(x='Sector', y='Adj Close', data=df3, order=df3.sort_values('Adj #Close', ascending=False).Sector, color='skyblue')
#plt.title('Compañias por sectores - S&P 500')
#plt.xlabel('Sectores - S&P 500')
#plt.xticks(rotation = 30)
#plt.ylabel('Cantidad de empresas - S&P 500')
#st.write(plt)



#---------------------------------------------
#GRAFICAMOS LAS TENDENCIAS DE LAS EMPRESAS SELECCIONADAS
#---------------------------------------------
#empresas = ['ROP', 'FICO', 'ADBE', 'TDY', 'LRCX', 'AAPL', 'MSFT']
#añadiremos a apple y microsoft porque siempre son referentes
# 'ROP'  = Roper Technologies, Inc., 
# 'FICO' = Fair Isaac Corporation, 
# 'ADBE' = Adobe Inc.
# 'TDY'  = Teledyne Technologies Incorporated, 
# 'LRCX' = Lam Research Corporation
# 'AAPL' = Apple Inc., 
# 'MSFT' = Microsoft

##fields = ['country', 'points', 'price', 'variety']

st.subheader('Tendencia por Empresas - Top 5 del sector TECH')

df3 = pd.read_csv("4precios7companies.csv", encoding="UTF8")
st.write(df3)

#---------------------------------------------------------------------------

#plt.figure(figsize=(16, 9))
#plt.plot(df3['ROP_Close'], color='red')
#plt.plot(df3['FICO_Close'], color='pink')
#plt.plot(df3['ADBE_Close'], color='green')
#plt.plot(df3['TDY_Close'], color='orange')
#plt.plot(df3['LRCX_Close'], color='purple')
#plt.plot(df3['AAPL_Close'], color='black')
#plt.plot(df3['MSFT_Close'], color='blue')
#plt.title('Precios de apertura y cierre de las 7 empresas')
#st.write(plt)

#---------------------------------------------------------------------------


col1, col2 = st.columns(2)

# 'ROP' = Roper Technologies, Inc., 
#fig = px.line(df3, x='DateIE', y="ROP_Close")

fig = px.line(df3, x='DateIE', y='ROP_Close', title='Tendencia del precio cierre ajustado - Roper Technologies, Inc.')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col1.write(fig)


#import plotly.graph_objects as go
#
#fig = go.Figure(data=[go.Candlestick(x=df3['DateIE'],
#                open=df3['ROP_Open'],
#                close=df3['ROP_Close'])])
#
#col1.write(fig)



# 'FICO' = Fair Isaac Corporation, 
#fig = px.line(df3, x='DateIE', y="FICO_Close")

fig = px.line(df3, x='DateIE', y='FICO_Close', title='Tendencia del precio cierre ajustado - Fair Isaac Corporation.')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col2.write(fig)



# 'ADBE' = Adobe Inc.
#fig = px.line(df3, x='DateIE', y="ADBE_Close")

fig = px.line(df3, x='DateIE', y='ADBE_Close', title='Tendencia del precio cierre ajustado -  Adobe Inc.')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col1.write(fig)




# 'TDY'  = Teledyne Technologies Incorporated, 
#fig = px.line(df3, x='DateIE', y="TDY_Close")

fig = px.line(df3, x='DateIE', y='TDY_Close', title='Tendencia del precio cierre ajustado -  Teledyne Technologies Incorporated.')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col2.write(fig)



# 'LRCX' = Lam Research Corporation
#fig = px.line(df3, x='DateIE', y="LRCX_Close")

fig = px.line(df3, x='DateIE', y='LRCX_Close', title='Tendencia del precio cierre ajustado -  Lam Research Corporation.')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col2.write(fig)




#------------------------------------------------------------------------
st.subheader('Tendencia empresas referentes en el mercado TECH')
col3, col4 = st.columns(2)

# 'AAPL' = Apple Inc., 
#fig = px.line(df3, x='DateIE', y="AAPL_Close")

fig = px.line(df3, x='DateIE', y='AAPL_Close', title='Tendencia del precio cierre ajustado - Apple Inc.')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col3.write(fig)



# 'MSFT' = Microsoft
#fig = px.line(df3, x='DateIE', y="MSFT_Close")

fig = px.line(df3, x='DateIE', y='MSFT_Close', title='Tendencia del precio cierre ajustado - Microsoft')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col4.write(fig)



