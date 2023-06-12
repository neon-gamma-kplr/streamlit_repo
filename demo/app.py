import streamlit as st
import numpy as np
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pydeck as pdk

# Titre
st.title("Mon application Streamlit avec Markdown")

# Sous-titre
st.subheader("Exemple d'utilisation du Markdown")

# afficher du texte formaté en Markdown (ici texte en gras avec deux astérisques (**) et en italique avec un astérisque (*))
st.markdown("Voici un **texte en gras** et un *texte en italique*.")

# afficher une liste à puces en Markdown
st.markdown("""
Voici une liste à puces :
- élément 1
- élément 2
- élément 3
""")

# afficher une liste numérotée en Markdown
st.markdown(""" Voici une liste numérotée :
1. élément 1
2. élément 2
3. élément 3
""")

# afficher une citation en Markdown
st.markdown("> Voici une citation.")

# afficher une ligne horizontale en Markdown
st.markdown("---")

# afficher une image en Markdown
st.markdown("![Alt texte](https://img.freepik.com/photos-premium/adorable-mignon-chat-potele-rendu-3d_784625-1053.jpg)")

# pour afficher un lien en Markdown (pas de "!" contrairement à une image)
st.markdown("[Cliquez ici pour aller sur Google](https://www.google.com)")

# widget pour créer un bouton qui peut être cliqué pour déclencher une action
st.button("Clique sur ce bouton")

# widget pour créer un curseur (slider) pour sélectionner une valeur numérique dans une plage donnée
st.slider("test", min_value=50, max_value=200, value=72, step=10)
st.slider("test_sans_labels", 50, 200, 72, 10)

# widget pour créer une liste déroulante (dropdown list) pour sélectionner une option dans une liste donnée
option = st.selectbox('How would you like to be contacted?', ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

# widget pour créer une liste déroulante avec la possibilité de sélectionner plusieurs options dans une liste donnée
option_multiselect = st.multiselect('How would you like to be contacted?', ['Email', 'Home phone', 'Mobile phone'])
st.write('You selected:', option_multiselect)

# widget pour créer une zone de texte où l'utilisateur peut entrer du texte
st.text_input("Entrez votre texte :", value="Salut !", max_chars=25)
st.text_input("Entrez votre mot de passe :", value="Salut !", max_chars=10, type="password")
st.text_input("Entrez votre texte :", max_chars=10, placeholder="Ecrivez ici", disabled=True)
st.text_input("Entrez votre texte :", max_chars=10, placeholder="Ecrivez ici", label_visibility="hidden", key="test_hidden")
st.text_input("Entrez votre texte :", max_chars=10, placeholder="Ecrivez ici", label_visibility="collapsed", key="test_collapsed")

# widget pour créer une zone de saisie pour entrer une valeur numérique
st.number_input("Entrez un nombre :", min_value=14, max_value=26, value=20, step=3)

# widget pour créer une zone de texte à plusieurs lignes où l'utilisateur peut entrer du texte
st.text_area("Donnez votre avis sur le film :", height=500)

# widget pour créer un calendrier où l'utilisateur peut sélectionner une date
st.date_input("Quand souhaitez-vous partir ?", min_value=datetime.date(2019, 7, 5), max_value=datetime.date(2025, 7, 7))

# widget pour un sélecteur d'heure où l'utilisateur peut sélectionner une heure
st.time_input("A quelle heure partez-vous ?", step=100)

# widget pour créer un bouton pour télécharger un fichier
st.file_uploader("Choisissez le fichier à télécharger (en .pdf ou .txt seulement)", type=["pdf", "txt"])
st.file_uploader("Choisissez les fichier à télécharger", accept_multiple_files=True)

# widget pour créer une case à cocher (checkbox) où l'utilisateur peut sélectionner ou désélectionner une option
st.checkbox("J'ai testé les checkbox")
st.checkbox("J'ai testé les checkbox", value=True)


df_citizen = pd.read_csv("demo/Citizen_DATA.csv")
# ces deux instructions affichent la même chose
df_citizen
st.write(df_citizen)

# widget pour tracer un graphique en ligne avec des données numériques
# st.line_chart(df_citizen, x='age', y='gender')
# st.line_chart(df_citizen, x='age', y='name')
# st.line_chart(df_citizen, x='age', y='city')
st.line_chart(df_citizen[:20], y='age')

# widget pour tracer un graphique de zone (aire) avec des données numériques
# st.area_chart(df_citizen, x='age', y='gender')
# st.area_chart(df_citizen, x='age', y='name')
# st.area_chart(df_citizen, x='age', y='city')
st.area_chart(df_citizen[:20], y='age')

# widget pour tracer un graphique à barres avec des données numériques
st.bar_chart(df_citizen[:20], y='age')

# widget pour tracer n'importe quel graphique matplotlib (créé avec la librairie pyplot) dans Streamlit
figure, axes = plt.subplots()
axes.plot(df_citizen['id'][:20], df_citizen['gender'][:20])
st.pyplot(figure)

# widget pour tracer un graphique interactif à l'aide de Plotly
fig = px.scatter(x=df_citizen['id'][:20], y=df_citizen['age'][:20])
st.plotly_chart(fig)

# widget pour tracer un graphique avec des spécifications Vega-Lite
st.vega_lite_chart(df_citizen, spec={
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'id', 'type': 'quantitative'},
        'y': {'field': 'age', 'type': 'quantitative'},
        'size': {'field': 'id', 'type': 'quantitative'},
        'color': {'field': 'age', 'type': 'quantitative'},
    },
})

# permet de tracer des cartes interactives 3D à l'aide de la bibliothèque Pydeck (objet(s) Layer Pydeck en entrée)
# layer = pdk.Layer('ScatterplotLayer', df_citizen, get_position=['id', 'age'])
# st.pydeck_chart(layer)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")