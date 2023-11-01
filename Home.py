import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='🏠 Home',
    )

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
st.write('## Ensaio de Compressão Simples')

st.markdown(
    """
    O Dashboard de do Ensaio de Compressão Simples do Grupo 1 foi construído
    para verificar os desenvolvimento da resistência dos corpos de prova ensaiados
    ao longo do tempo e com os esforços aplicados de forma axial e diametral.
    
    Este Dashboard contém:
    1. Métricas do Ensaio de Compressão.
    2. Gráficos 
    3. Métricas de Dispersão

    """
)