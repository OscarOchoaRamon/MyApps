from windrose import WindroseAxes
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import streamlit as st
import pandas as pd
import os


# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file, delimiter=';')
#     st.write(dataframe)

st.title("Generación de Rosa de viento")

# Create wind speed and direction variables
ws = np.random.random(500) * 6
wd = np.random.random(500) * 360

ax1 = WindroseAxes.from_ax()
ax1.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
ax1.set_legend()

ax2 = WindroseAxes.from_ax()
ax2.box(wd, ws, bins=np.arange(0, 8, 1))
ax2.set_legend()

ax3 = WindroseAxes.from_ax()
ax3.contourf(wd, ws, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax3.set_legend()

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Opción A')
    st.pyplot(ax1.figure)
    
with col2:
    st.header('Opción B')
    st.pyplot(ax2.figure)
with col3:
    st.header('Opción C')
    st.pyplot(ax3.figure)
    
uploaded_file = st.sidebar.file_uploader("Choose a file")
    
add_selectbox = st.sidebar.selectbox(
    '¿Qué tipo de rosa de viento te gustaría generar?',
    ('','A', 'B', 'C')
)

def save_df_to_folder(folder_path):
    """Saves dataframe to the provided folder."""
    if not os.path.isdir(folder_path):
        st.error('The provided folder does not exist. Please provide a valid folder path.')
        return
    ruta2=folder_path.replace('\\', '/')
    ruta3=ruta2.replace("'", "")
    os.chdir(ruta3)
    
ruta = st.text_input('Coloque la ruta donde se guardarán las imágenes')
if st.button('Save Dataframe'):
    save_df_to_folder(ruta)

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, delimiter=';')
    st.write(dataframe)
    
    if add_selectbox=='A':    
        ax4 = WindroseAxes.from_ax()
        ax4.bar(dataframe['dv'], dataframe['vv'], normed=True, opening=0.8, edgecolor='white')
        ax4.set_legend()
        plt.savefig('imagenA.png')
        
    elif add_selectbox=='B':
        ax5 = WindroseAxes.from_ax()
        ax5.box(dataframe['dv'], dataframe['vv'], bins=np.arange(0, 8, 1))
        ax5.set_legend()
        plt.savefig('imagenB.png')
        
    elif add_selectbox=='C':
        ax3 = WindroseAxes.from_ax()
        ax3.contourf(dataframe['dv'], dataframe['vv'], bins=np.arange(0, 8, 1), cmap=cm.hot)
        ax3.set_legend()
        plt.savefig('imagenC.png')


        



