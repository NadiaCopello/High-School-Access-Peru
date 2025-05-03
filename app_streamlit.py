import streamlit as st

st.set_page_config(page_title="Acceso a Escuelas", layout="wide")

# Pestañas
tab1, tab2, tab3 = st.tabs(["📊 Descripción de los datos", "🗺️ Mapas estáticos", "🌍 Mapas dinámicos"])

# === TAB 1 ===
with tab1:
    st.header("Descripción de los datos")
    st.markdown("""
    - **Unidad de análisis:** Instituciones educativas públicas por distrito.
    - **Fuentes de datos:** 
        - Listado de IIEE (`listado_iiee.xls`)
        - Shape de distritos (`DISTRITOS.shp`)
    - **Preprocesamiento realizado:** Limpieza de nombres, filtrado por nivel educativo y georreferenciación.
    """)

# === TAB 2 ===
with tab2:
    st.header("Mapas estáticos")
    st.write("Aquí se mostrarán los mapas estáticos con GeoPandas.")
    st.image("img/mapa_primaria.png", caption="Mapa de escuelas primarias por distrito", use_column_width=True)

# === TAB 3 ===
with tab3:
    st.header("Mapas dinámicos con Folium")
    st.write("Aquí se mostrarán los mapas interactivos.")

    