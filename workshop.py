import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Manipulation and Visualization", page_icon=":shark:", layout="wide")

st.title("Data Manipulation and Visualization")

df_citizen = pd.DataFrame()

file = st.file_uploader("Choose a file", type="csv")
if file is not None:
    # # afficher le nom du fichier
    st.write(f"Nom du fichier téléchargé : {file.name}")
    # # afficher le fichier en objet de type 'bytes'
    # bytes_data = file.getvalue()
    # st.write("Contenu du fichier (en objet de type 'bytes') :")
    # st.write(bytes_data)
    df_citizen = pd.read_csv(file)
    
st.write(df_citizen.head())
st.write(f'Nombre de lignes dans le fichier : {df_citizen.shape[0]}')
st.write(df_citizen.describe())

colonne = st.selectbox('Sélectionnez une colonne :', ('id', 'name', 'age', 'gender', 'city'), index=1)
valeur = st.text_input('Entrez une valeur :', value="Tilda")
donnees_filtrees = df_citizen[df_citizen[colonne] == valeur]
st.write(donnees_filtrees)


st.subheader("Histogram")

col1, col2 = st.columns(2)

with col1:
    nombre_lignes = st.slider("Sélectionnez le nombre de lignes à afficher :", max_value=df_citizen.shape[0])
with col2:
    colonne = st.selectbox("Sélectionnez l'axe des x :", ('id', 'name', 'age', 'gender', 'city'), index=2)
figure = plt.figure()
plt.hist(df_citizen[colonne][:nombre_lignes], bins=20)
plt.xlabel(colonne)
st.pyplot(figure)


st.subheader("Chart")

type_graphe = st.selectbox("Sélectionnez le type de graphique à utiliser :", ('ligne', 'barre', 'nuage de points'))

if type_graphe == 'ligne':
    x_axis = st.selectbox("Sélectionnez l'axe des x :", ('id', 'name', 'age', 'gender', 'city'), key="x_axis")
    y_axis = st.selectbox("Sélectionnez l'axe des y :", ('id', 'name', 'age', 'gender', 'city'), index=2)
    figure = plt.figure()
    plt.plot(df_citizen[x_axis], df_citizen[y_axis])
    st.pyplot(figure)

elif type_graphe == 'barre':
    x_axis = st.selectbox("Sélectionnez l'axe des x :", ('id', 'name', 'age', 'gender', 'city'), key="x_axis")
    y_axis = st.selectbox("Sélectionnez l'axe des y :", ('id', 'name', 'age', 'gender', 'city'), index=2)
    figure = plt.figure()
    plt.bar(df_citizen[x_axis], df_citizen[y_axis])
    st.pyplot(figure)

else: # si l'utilisateur sélectionne "nuage de points"
    x_axis = st.selectbox("Sélectionnez l'axe des x :", ('id', 'name', 'age', 'gender', 'city'), key="x_axis")
    y_axis = st.selectbox("Sélectionnez l'axe des y :", ('id', 'name', 'age', 'gender', 'city'), index=2)
    figure = plt.figure()
    plt.scatter(df_citizen[x_axis], df_citizen[y_axis])
    st.pyplot(figure)
