import streamlit as st
import pandas as pd



st.header("EIAROB WEB LOGIN", divider="rainbow", text_alignment="center")

#st.menu_button("menu", "hola", type="primary")

# 1. Entrada de usuario
nombre = st.text_input("👤 Usuario", placeholder="Usuario")
correcto = False


contrasenia = st.text_input("🔎︎ Contraseña", placeholder="Contraseña", type="password") 
contrasenia2 = st.text_input("Repite contraseña", placeholder="Contraseña", type="password")
 
if contrasenia2 and contrasenia: 
    if contrasenia != contrasenia2: 
        correcto = False
    else:
        correcto = True



# 2. El boton del login que comprueba lo anterior 
login=st.button("Login", use_container_width=True)

if login:
    if correcto and nombre:
        st.success(f"Bienvenido {nombre}!")
    elif not correcto:
        st.error("Las contraseñas no son iguales")
    else: 
        st.error("Introduce Usuario")
