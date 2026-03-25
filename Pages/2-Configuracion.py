import streamlit as st

st.title("⚙️ Configuración de la Aplicación")

st.write("Administra las preferencias generales del sistema, usuario y apariencia.")

# ------------------------
# CONFIGURACIÓN DE USUARIO
# ------------------------
st.subheader("👤 Perfil de Usuario")

nombre = st.text_input("Nombre de usuario", "Usuario123")
email = st.text_input("Correo electrónico", "usuario@email.com")
password = st.text_input("Contraseña", type="password")

st.divider()

# ------------------------
# CONFIGURACIÓN DE LA APP
# ------------------------
st.subheader("🖥️ Preferencias de la Aplicación")

idioma = st.selectbox("Idioma", ["Español", "Inglés", "Portugués"])
tema = st.radio("Tema visual", ["Claro", "Oscuro", "Pastel"])
notificaciones = st.checkbox("Activar notificaciones", value=True)

st.divider()

# ------------------------
# CONFIGURACIÓN DE DATOS
# ------------------------
st.subheader("📊 Configuración de Datos")

formato = st.selectbox("Formato de exportación", ["CSV", "Excel", "JSON"])
autosave = st.checkbox("Guardar automáticamente", value=True)
frecuencia = st.slider("Frecuencia de guardado (minutos)", 1, 60, 10)

st.divider()

# ------------------------
# PRIVACIDAD
# ------------------------
st.subheader("🔒 Privacidad y Seguridad")

ver_datos = st.checkbox("Permitir visualización de datos personales")
compartir = st.checkbox("Compartir datos para análisis")

st.warning("Recuerda proteger tu información personal.")

st.divider()

# ------------------------
# BOTÓN GUARDAR
# ------------------------
if st.button("💾 Guardar Configuración"):
    st.success("Configuración guardada correctamente")