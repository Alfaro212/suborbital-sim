
# 🚀 Suborbital Rocket Simulator

Este es un simulador interactivo de vuelo suborbital creado con [Streamlit](https://streamlit.io/). Puedes ejecutarlo localmente o desplegarlo como una app web.

---

## ✅ Requisitos

- Python 3.7 o superior
- Paquetes: `streamlit`, `numpy`, `matplotlib`, `plotly`

Instala los paquetes con:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar Localmente

```bash
streamlit run suborbital_rocket_simulator.py
```

La app se abrirá automáticamente en tu navegador (`http://localhost:8501`).

---

## 📦 Crear un archivo .exe (opcional)

Si deseas convertir esta app en un `.exe` para Windows:

```bash
pip install pyinstaller
pyinstaller --onefile suborbital_rocket_simulator.py
```

El ejecutable aparecerá en la carpeta `dist/`.

---

## ☁️ Publicar en Streamlit Cloud

1. Sube este proyecto a un repositorio en GitHub.
2. Ve a [streamlit.io/cloud](https://streamlit.io/cloud).
3. Conecta tu cuenta GitHub.
4. Elige tu repositorio y despliega tu app.

---

## 📄 Archivos incluidos

- `suborbital_rocket_simulator.py` – Script principal
- `requirements.txt` – Lista de dependencias
- `README.md` – Este archivo

