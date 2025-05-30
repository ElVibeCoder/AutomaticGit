# 📤 UploadDaily — App para Subir Archivos a GitHub Automáticamente

Bienvenido/a. Este proyecto te permite subir un archivo `readme.txt` a tu repositorio de GitHub con una app web muy simple hecha en Flask, y además automatizar esa subida para que se haga una vez al día sin que tengas que intervenir.

Ideal para aprender a integrar Python + GitHub + automatización.

---

## 🎯 ¿Qué hace esta app?

- Muestra una página web donde puedes subir un archivo `.txt`
- El archivo se sube automáticamente a la carpeta `txt/` de tu repositorio en GitHub
- Si el archivo ya existe, lo actualiza
- Incluye un script automático para hacer el upload **una vez al día** sin abrir el navegador

---

## 🧰 Requisitos

Asegúrate de tener esto instalado en tu computadora:

- ✅ [Python 3.12+](https://www.python.org/downloads/)
- ✅ `pip` funcionando
- ✅ Un repositorio propio (como `UploadDaily`)
- ✅ Un **token personal de GitHub** con permisos para ese repo (classic, repo)

---

## 🛠 Instalación paso a paso

### 1. Clona el repositorio (o crea una carpeta)

```bash
git clone https://github.com/Hakired/UploadDaily.git
cd UploadDaily

### 2. Instala los paquetes necesarios

- ✅ pip install flask PyGithub schedule


### 3. Edita el app.py para añadir el Token y Ejecuta la app
- ✅ python auto_upload.py
