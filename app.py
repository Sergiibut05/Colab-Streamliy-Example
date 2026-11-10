import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Dashboard de Visualización", layout="wide")
st.title("📊 Comparativa de Visualización: Matplotlib vs Seaborn")
st.markdown("Esta aplicación de Streamlit muestra cómo renderizar los mismos 5 tipos de gráficas utilizando **Matplotlib** y **Seaborn**.")

# Configuración del estilo global de Seaborn
sns.set_theme(style="whitegrid")

# --- Generación de Datos Sintéticos ---
@st.cache_data
def generar_datos():
    np.random.seed(42)
    
    # 1. Serie temporal (Líneas)
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    ventas = [120, 135, 128, 150, 180, 175, 210, 205, 190, 220, 240, 260]
    df_lineas = pd.DataFrame({'Mes': meses, 'Ventas': ventas})
    
    # 2. Categorías (Barras)
    categorias = ['Electrónica', 'Hogar', 'Moda', 'Deportes', 'Juguetes']
    promedio = [450, 320, 580, 290, 410]
    df_barras = pd.DataFrame({'Categoría': categorias, 'Promedio': promedio})
    
    # 3. Distribución (Histograma)
    tiempos = np.random.normal(loc=250, scale=30, size=500)
    df_hist = pd.DataFrame({'Tiempo_ms': tiempos})
    
    # 4. Dispersión (Scatter)
    horas = np.random.uniform(1, 10, 80)
    notas = 4 + 0.55 * horas + np.random.normal(0, 0.8, 80)
    df_scatter = pd.DataFrame({'Horas': horas, 'Nota': np.clip(notas, 0, 10)})
    
    # 5. Boxplot
    deptos = np.repeat(['I+D', 'Ventas', 'Marketing', 'RRHH'], 40)
    sueldos_base = {'I+D': 45, 'Ventas': 38, 'Marketing': 35, 'RRHH': 32}
    sueldos = [sueldos_base[d] + np.random.normal(0, 5) for d in deptos]
    df_box = pd.DataFrame({'Departamento': deptos, 'Sueldo_k': sueldos})
    
    return df_lineas, df_barras, df_hist, df_scatter, df_box

df_lineas, df_barras, df_hist, df_scatter, df_box = generar_datos()

# Selector en el Sidebar
st.sidebar.header("Opciones de Visualización")
modo_vista = st.sidebar.radio("Modo de vista:", ["Lado a Lado (Comparativa)", "Por Pestañas de Gráfica"])

if modo_vista == "Lado a Lado (Comparativa)":
    st.subheader("1. Gráfico de Líneas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matplotlib**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.plot(df_lineas['Mes'], df_lineas['Ventas'], marker='o', color='#1f77b4', linewidth=2)
        ax.set_title('Ventas Mensuales')
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        st.markdown("**Seaborn**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.lineplot(data=df_lineas, x='Mes', y='Ventas', marker='o', color='#1f77b4', ax=ax)
        ax.set_title('Ventas Mensuales')
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    st.subheader("2. Gráfico de Barras")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matplotlib**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.bar(df_barras['Categoría'], df_barras['Promedio'], color='#2ca02c', alpha=0.85)
        ax.set_title('Ventas por Categoría')
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        st.markdown("**Seaborn**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.barplot(data=df_barras, x='Categoría', y='Promedio', palette='Greens_d', ax=ax)
        ax.set_title('Ventas por Categoría')
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    st.subheader("3. Histograma")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matplotlib**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.hist(df_hist['Tiempo_ms'], bins=25, color='#ff7f0e', edgecolor='black', alpha=0.75)
        ax.set_title('Tiempos de Respuesta')
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        st.markdown("**Seaborn**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.histplot(data=df_hist, x='Tiempo_ms', bins=25, kde=True, color='#ff7f0e', ax=ax)
        ax.set_title('Tiempos de Respuesta (+ KDE)')
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    st.subheader("4. Gráfico de Dispersión (Scatter)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matplotlib**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.scatter(df_scatter['Horas'], df_scatter['Nota'], color='#9467bd', alpha=0.8)
        ax.set_title('Estudio vs Nota')
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        st.markdown("**Seaborn**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.scatterplot(data=df_scatter, x='Horas', y='Nota', color='#9467bd', s=70, ax=ax)
        ax.set_title('Estudio vs Nota')
        st.pyplot(fig)
        plt.close(fig)

    st.divider()

    st.subheader("5. Diagrama de Caja (Boxplot)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matplotlib**")
        datos_box = [df_box[df_box['Departamento'] == d]['Sueldo_k'] for d in df_box['Departamento'].unique()]
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.boxplot(datos_box, labels=df_box['Departamento'].unique(), patch_artist=True,
                   boxprops=dict(facecolor='#d62728', alpha=0.7))
        ax.set_title('Sueldos por Departamento')
        st.pyplot(fig)
        plt.close(fig)
    with col2:
        st.markdown("**Seaborn**")
        fig, ax = plt.subplots(figsize=(6, 3.5))
        sns.boxplot(data=df_box, x='Departamento', y='Sueldo_k', palette='Reds', ax=ax)
        ax.set_title('Sueldos por Departamento')
        st.pyplot(fig)
        plt.close(fig)

else:
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Líneas", "Barras", "Histograma", "Scatter", "Boxplot"])
    
    with tab1:
        st.subheader("Gráfico de Líneas")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(data=df_lineas, x='Mes', y='Ventas', marker='o', color='#1f77b4', ax=ax)
        st.pyplot(fig)
        plt.close(fig)
        
    with tab2:
        st.subheader("Gráfico de Barras")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(data=df_barras, x='Categoría', y='Promedio', palette='Greens_d', ax=ax)
        st.pyplot(fig)
        plt.close(fig)
        
    with tab3:
        st.subheader("Histograma")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(data=df_hist, x='Tiempo_ms', bins=25, kde=True, color='#ff7f0e', ax=ax)
        st.pyplot(fig)
        plt.close(fig)
        
    with tab4:
        st.subheader("Gráfico de Dispersión")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(data=df_scatter, x='Horas', y='Nota', color='#9467bd', s=70, ax=ax)
        st.pyplot(fig)
        plt.close(fig)
        
    with tab5:
        st.subheader("Diagrama de Caja")
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.boxplot(data=df_box, x='Departamento', y='Sueldo_k', palette='Reds', ax=ax)
        st.pyplot(fig)
        plt.close(fig)
