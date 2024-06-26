from windrose import WindroseAxes
import numpy as np
import streamlit as st
import pandas as pd

st.title(":blue[Generación de rosa de viento]")
st.write("_(Elaborado por el Equipo de Recursos Hídricos :droplet:)_")

division_angule = np.linspace(0, 2 * np.pi, 16, endpoint=False)
directions = ['E', 'ENE', 'NE', 'NNE', 'N', 'NNW', 'NW', 'WNW','W', 'WSW', 'SW', 'SSW', 'S', 'SSE', 'SE', 'ESE']

#I stayed here
if 'graph1' not in st.session_state or 'graph2' not in st.session_state or 'graph3' not in st.session_state:    
    # Create wind speed and direction variables
    valores_random = np.random.random(500)
    
    ax1 = WindroseAxes.from_ax()
    ax1.bar(valores_random*360, valores_random*20, bins=8, normed=True, opening=0.8)
    ax1.set_legend()
    ax1.set_xticks(division_angule)
    ax1.set_xticklabels(directions)
    st.session_state['graph1']=ax1.figure
    
    ax2 = WindroseAxes.from_ax()
    ax2.box(valores_random*360, valores_random*20, bins=8, normed=True)
    ax2.set_legend()
    ax2.set_xticks(division_angule)
    ax2.set_xticklabels(directions)
    st.session_state['graph2']=ax2.figure
    
    ax3 = WindroseAxes.from_ax()
    ax3.contourf(valores_random*360, valores_random*20, bins=8, normed=True)
    ax3.set_legend()
    ax3.set_xticks(division_angule)
    ax3.set_xticklabels(directions)
    st.session_state['graph3']=ax3.figure
    
col1, col2, col3 = st.columns(3)

with col1:
    st.header('Opción A')
    st.pyplot(st.session_state['graph1'])
    
with col2:
    st.header('Opción B')
    st.pyplot(st.session_state['graph2'])
with col3:
    st.header('Opción C')
    st.pyplot(st.session_state['graph3'])
    
uploaded_file = st.sidebar.file_uploader(":blue[Seleccione su archivo Excel:]")

station_number = st.sidebar.text_input(':blue[Coloque el número de estaciones:]')
    
add_selectbox = st.sidebar.selectbox(
    ':blue[¿Qué tipo de rosa de viento le gustaría generar?]',
    ('','A', 'B', 'C')
)

station_label = []
for label in range(1,int(station_number)+1):
    station_label.append('estacion_{}'.format(label))

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, delimiter=';')
    st.subheader("Aquí se muestran los gráficos generados :point_down::")
    station_display = st.selectbox('Escoja la estación para visualizar la rosa de viento:',station_label)
    
    if add_selectbox=='A':    
        ax4 = WindroseAxes.from_ax()
        ax4.bar(dataframe['dv_{}'.format(station_label.index(station_display)+1)], dataframe['vv_{}'.format(station_label.index(station_display)+1)], normed=True, opening=0.8, edgecolor='white')
        ax4.set_legend()
        ax4.set_xticks(division_angule)
        ax4.set_xticklabels(directions)
        st.pyplot(ax4.figure)
        
    elif add_selectbox=='B':
        ax5 = WindroseAxes.from_ax()
        ax5.box(dataframe['dv_{}'.format(station_label.index(station_display)+1)], dataframe['vv_{}'.format(station_label.index(station_display)+1)], bins=8, normed=True)
        ax5.set_legend()
        ax5.set_xticks(division_angule)
        ax5.set_xticklabels(directions)
        st.pyplot(ax5.figure)
        
    elif add_selectbox=='C':
        ax6 = WindroseAxes.from_ax()
        ax6.contourf(dataframe['dv_{}'.format(station_label.index(station_display)+1)], dataframe['vv_{}'.format(station_label.index(station_display)+1)], bins=8, normed=True)
        ax6.set_legend()
        ax6.set_xticks(division_angule)
        ax6.set_xticklabels(directions)
        st.pyplot(ax6.figure)



