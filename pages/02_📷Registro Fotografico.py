#==========Libraries==========#
import plotly.express as px
import pandas as pd
import xlrd
#==========Bibliotecas necessárias============#
import streamlit as st
from PIL import Image
st.set_page_config(page_title='Registro Fotográfico',page_icon='🌌',layout='centered')

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

#====Logo UFPA====#
image = Image.open('image.png')
col1,col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.image(image, width=120)
with col3:
    st.write('')

#======Intro======#
st.markdown('### Registro Fotográgico do Desenvolvimento do Ensaio')

#====Códigos======#
with st.container():
    st.markdown('### Compressão Axial - :seven: Dias')
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        image = Image.open('img_7d/01.jpeg')
        st.image(image, width = 120)
    with col2:
        image = Image.open('img_7d/02.jpeg')
        st.image(image, width = 120)
    with col3:
        image = Image.open('img_7d/03.jpeg')
        st.image(image, width = 120)
    with col4:
        image = Image.open('img_7d/04.jpeg')
        st.image(image, width = 120)

with st.container():
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        image = Image.open('img_7d/05.jpeg')
        st.image(image, width = 120)
    with col2:
        image = Image.open('img_7d/09.jpeg')
        st.image(image, width = 120)
    with col3:
        image = Image.open('img_7d/10.jpeg')
        st.image(image, width = 120)
    with col4:
        image = Image.open('img_7d/12.jpeg')
        st.image(image, width = 120)

st.markdown ('---')

with st.container():
    col1,col2,col3= st.columns(3, gap='large')
    with col1:
        image = Image.open('img_28d/01.jpeg')
        st.image(image, width = 120)
    with col2:
        image = Image.open('img_28d/02.jpeg')
        st.image(image, width = 120)
    with col3:
        image = Image.open('img_28d/03.jpeg')
        st.image(image, width = 120)

with st.container():
    col1,col2,col3= st.columns(3, gap='large')
    with col1:
        image = Image.open('img_28d/04.jpeg')
        st.image(image, width = 120)
    with col2:
        image = Image.open('img_28d/05.jpeg')
        st.image(image, width = 120)
    with col3:
        image = Image.open('img_28d/06.jpeg')
        st.image(image, width = 120)

st.markdown ('---')

with st.container():
    st.markdown('### Compressão Diametral - :two::eight: Dias')
    col1,col2,col3= st.columns(3, gap='large')
    with col1:
        image = Image.open('img_28d/07.jpeg')
        st.image(image, width = 120)
    with col2:
        image = Image.open('img_28d/08.jpeg')
        st.image(image, width = 120)
    with col3:
        image = Image.open('img_28d/09.jpeg')
        st.image(image, width = 120)

with st.container():
    col1,col2,col3= st.columns(3, gap='large')
    with col1:
        image = Image.open('img_28d/10.jpeg')
        st.image(image, width = 120)
    with col2:
        image = Image.open('img_28d/11.jpeg')
        st.image(image, width = 120)
    with col3:
        image = Image.open('img_28d/12.jpeg')
        st.image(image, width = 120)
