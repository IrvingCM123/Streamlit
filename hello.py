import streamlit as st
import pandas as pd

#######Leer los datos de un archivo###############33
names_link = 'dataset.csv'

@st.cache
def load_data(nrows) :
    data = pd.read_csv(names_link, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1500)
data_load_state.text('Done! (using st.cache)')

st.dataframe(data)

###########Recibir nombre ############################333
st.title('Streamlit - Show name')
def bienvenida(nombre) :
    mymensaje = f'bienvenido/a : {nombre}' 
    return mymensaje

myname = st.text_input('nombre :')
if (myname) :
    mensaje = bienvenida(myname)
    st.write(f"Result : {mensaje} ")


################Contar la cantidad de veces encontrada una palabra ################

st.title('Streamlit - Search names')
def load_data_byname(name) :
    data = pd.read_csv(names_link)
    filtered_data_byname = data[data['name'].str.contains(name)]
    
    return filtered_data_byname

myname = st.text_input('Name :')
if (myname):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0]
    st.write(f"Total names : {count_row} ")
    
    st.dataframe(filterbyname)