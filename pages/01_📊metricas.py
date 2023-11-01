#==========Libraries==========#
import plotly.express as px
import pandas as pd
#==========Bibliotecas necessárias============#
import streamlit as st
from PIL import Image
st.set_page_config(page_title='Registro Fotográfico',page_icon='🌌',layout='wide')

df = pd.read_csv('dataset/dados_tec_con.csv', thousands = ',', decimal = '.')
df1 = df.copy()
df1.drop([6,7,8,9,10,11,12,13,14], inplace=True)
df['forca_max'] = df['forca_max'].astype( float )
df2 = df.copy()

#=====Sidebar=====#
image = Image.open('image.png')
st.sidebar.image(image, width=80)
st.sidebar.markdown('## Universidade Federal do Pará')
st.sidebar.markdown('### Grupo 1')
st.sidebar.markdown("""---""")

st.sidebar.write('## :dart: Escolha a Compressão:')
compress_options = st.sidebar.multiselect('',
    ['Axial','Diametral'],
    default = ['Axial'])

#----Filtro Sidebar-----#
linhas_selecionadas = df2['metodo'].isin(compress_options)
df2 = df2.loc[linhas_selecionadas, :]


#====Logo UFPA====#
image = Image.open('image.png')
col1,col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.image(image, width=120)
with col3:
    st.write('')

#=======Códigos===============#
st.markdown('# Métricas do Ensaio de Compressão')
col1,col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.markdown('## Grupo 1 ')
with col3:
    st.write('')

st.markdown('---')

st.markdown('### Valores de Resistência Obtidos :rocket:')
with st.container():
    col1,col2,col3 = st.columns(3)
    col1.metric('Resistência CP1 (7 Dias)', f'{df1.iloc[0,10]} Mpa','Bom')
    col2.metric('Resistência CP2 (7 Dias)', f'{df1.iloc[1,10]} Mpa','Bom')
    col3.metric('Resistência CP3 (28 Dias)', f'{df1.iloc[2,10]} Mpa','-Ruim')

with st.container():
    col1,col2,col3 = st.columns(3)
    col1.metric('Resistência CP4 (28 Dias)', f'{df1.iloc[3,10]} Mpa','-Ruim')
    col2.metric('Resistência CP5 (28 Dias)', f'{df1.iloc[4,10]} Mpa','Bom')
    col3.metric('Resistência CP6 (28 Dias)', f'{df1.iloc[5,10]} Mpa','Bom')

st.markdown('---')
st.markdown('### Gráficos :bar_chart:')
with st.container():
    col1,col2 = st.columns(2)
    with col1:
        df_aux = df1.loc[df1['metodo'] == 'Axial', ['dias','forca_max']]
        fig = px.bar(df_aux,x='dias',
                            y='forca_max',labels={
                            'forca_max': 'Força Máxima (Kgf)',
                            'dias': 'Dias'},
                            color = 'dias',
                            color_discrete_sequence=px.colors.qualitative.G10_r,
                            template='ggplot2',
                            text='forca_max'
                            )
        fig.update_traces(textposition='inside',texttemplate='%{text:.5s}')
        fig.update_yaxes(showticklabels=False) # Tira o eixo y
        fig.update_layout(title = {
            'text' : 'FORÇA MÁXIMA NA COMPRESSÃO AXIAL APÓS 7 E 28 DIAS',
            'y' : 0.9,
            'x' : 0.15
        })
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        df_aux = df1.loc[df1['metodo'] == 'Axial', ['dias','resistencia_obtida']]
        fig = px.bar(df_aux,x='dias',
                            y='resistencia_obtida',labels={
                            'resistencia_obtida': 'Resistência Obtida (Mpa)',
                            'dias': 'Dias'},
                            color = 'dias',
                            color_discrete_sequence=px.colors.qualitative.Set1_r,
                            template='ggplot2',
                            text='resistencia_obtida'
                            )
        fig.update_traces(textposition='inside',texttemplate='%{text:.5s}')
        fig.update_yaxes(showticklabels=False) # Tira o eixo y
        fig.update_layout(title = {
            'text' : 'RESISTÊNCIA OBTIDA NA COMPRESSÃO AXIAL APÓS 7 E 28 DIAS',
            'y' : 0.9,
            'x' : 0.15
        })
        st.plotly_chart(fig, use_container_width=True)

st.markdown('---')

with st.container():
    df_aux = df2.loc[:,['metodo','cp','forca_max']]
    fig = px.bar(df_aux,x='cp',
                        y='forca_max',
                        labels={
                        'forca_max': 'Força Máxima (Kgf)',
                        'cp': 'Corpos de Prova'},
                        color = 'cp',
                        color_discrete_sequence=px.colors.qualitative.Set1_r,
                        template='ggplot2',
                        text='forca_max'
                        )
    fig.update_traces(textposition='outside',texttemplate='%{text:.5s}')
    fig.update_yaxes(showticklabels=False) # Tira o eixo y
    fig.update_layout(title = {
        'text' : 'FORÇA MÁXIMA OBTIDA NOS CORPOS DE PROVA',
        'y' : 0.9,
        'x' : 0.25
    })
    st.plotly_chart(fig, use_container_width=True)

st.markdown('---')

with st.container():
    df_aux = df2.loc[:,['metodo','cp','resistencia_obtida']]
    fig = px.bar(df_aux,x='cp',
                        y='resistencia_obtida',
                        labels={
                        'resistencia_obtida': 'Resistência Obtida (Mpa)',
                        'cp': 'Corpos de Prova'},
                        color = 'cp',
                        color_discrete_sequence=px.colors.qualitative.Alphabet,
                        template='ggplot2',
                        text='resistencia_obtida'
                        )
    fig.update_traces(textposition='outside',texttemplate='%{text:.5s}')
    fig.update_yaxes(showticklabels=False) # Tira o eixo y
    fig.update_layout(title = {
        'text' : 'RESISTÊNCIA OBTIDA NOS CORPOS DE PROVA',
        'y' : 0.9,
        'x' : 0.25
    })
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('---')

    st.title('Cálculo de Dispesão :chart_with_upwards_trend:')
st.markdown('### :seven: Dias - Compressão Axial')

with st.container():
    col1,col2,col3 = st.columns(3)
    with col1:
        df_aux1 = df1.loc[df1['dias']=='sete', 'resistencia_obtida'].mean().round(3)
        st.metric('Média',df_aux1)
    with col2:
        df_aux2 = df1.loc[df1['dias']=='sete', 'resistencia_obtida'].std().round(2)
        st.metric('Desvio Padrão', df_aux2)
    with col3:
        df_aux3 = (df_aux2/df_aux1)*100
        df_aux3 = df_aux3.round(2)
        st.metric('Coeficiente de Variação',f'{df_aux3} %')

st.markdown('### :two::eight: Dias - Compressão Axial')

with st.container():
    col1,col2,col3 = st.columns(3)
    with col1:
        df_aux4 = (df1.loc[(df1['dias']=='vinte e oito') & (df1['metodo'] == 'Axial'), 'resistencia_obtida']
                      .mean()
                      .round(3))
        st.metric('Média',df_aux4)
    with col2:
        df_aux5 = (df1.loc[(df1['dias']=='vinte e oito') & (df1['metodo'] == 'Axial'), 'resistencia_obtida']
                      .std()
                      .round(2))
        st.metric('Desvio Padrão', df_aux5)
    with col3:
        df_aux6 = (df_aux5/df_aux4)*100
        df_aux6 = df_aux6.round(2)
        st.metric('Coeficiente de Variação',f'{df_aux6} %')

st.markdown('### :two::eight: Dias - Compressão Diametral')
with st.container():
    col1,col2,col3 = st.columns(3)
    with col1:
        df_aux7 = (df1.loc[(df1['dias']=='vinte e oito') & (df1['metodo'] == 'Diametral'), 'resistencia_obtida']
                      .mean()
                      .round(3))
        st.metric('Média',df_aux7)
    with col2:
        df_aux8 = (df1.loc[(df1['dias']=='vinte e oito') & (df1['metodo'] == 'Diametral'), 'resistencia_obtida']
                      .std()
                      .round(2))
        st.metric('Desvio Padrão', df_aux8)
    with col3:
        df_aux9 = (df_aux8/df_aux7)*100
        df_aux9 = df_aux9.round(2)
        st.metric('Coeficiente de Variação',f'{df_aux9} %')
