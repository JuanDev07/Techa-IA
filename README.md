# Título

Este proyecto es una aplicación web construida con Flask que predice la potencia de un panel solar basado en la temperatura, radiación solar y tipo de panel ingresados por el usuario. Utiliza un modelo de aprendizaje automático previamente entrenado y almacenado en `modelo.pkl`, y un escalador en `escalador.pkl` para normalizar los datos.

## Características

- **Predicción de potencia** para tipos de paneles solares (CIGS, HIT, m-Si).
- **Interfaz de usuario** simple construida en HTML con Flask.
- **Escalado de entrada** utilizando un escalador previamente ajustado.
- **Integración de modelo** de machine learning utilizando pickle.

## Estructura del Proyecto

```plaintext
├── app.py               # Código principal de la aplicación Flask
├── modelo.pkl           # Modelo binarizado para predicción
├── escalador.pkl        # Escalador binarizado para normalizar los datos de entrada
├── requirements.txt     # Archivo con las dependencias del proyecto
├── templates/
│   └── index.html       # Plantilla HTML para la interfaz de usuario
└── README.md            # Documentación del proyecto

## Requisitos

- Python 3.7 o superior
- Flask
- Pandas
- Numpy
- Pickle4 (para la carga del modelo)

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. ** Descarga 

3. ** Crea y active un entorno virtual:**
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   
4. **Instala las dependencias:**
    pip install -r requirements.txt

## Uso

1. **Ejecuta la aplicación:**
     python app.py

2. **Abre el navegador** 
     http://127.0.0.1:5000 para acceder a la interfaz (Control + click)

3. **Usa la interfaz para ingresar los datos de predicción**
  la temperatura (en grados Celsius)
  radiación  (en W/m²)
  tipo de panel (Selecciona entre CIGS, HIT o m-Si)

## Notas

Para desarrollo local, la aplicación se ejecuta en modo debug, por lo que cualquier cambio en el código se reflejará en tiempo real.

**Para desactivar el entorno virtual venv**
deactivate/Control + C parar el debug

**Datos de los paneles:**
CIGS: Miasolé FLEX–02 120 N, area:  0.94 m2
HIT: Panasonic VBHN330SJ47, 1.67 m2
m-Si: Znshine solar ZX55(17.8)M, area: 0.43 m2

**Donde los usuarios pueden encontrar ayuda sobre su proyecto**
bootcampgrupo4@gmail.com

**Autores del proyecto**
Cristian Alejandro Beltran Hernandez
David Montoya Ledesma
John Fredy Toro Suaza
Juan Rojas Mesa
Lina Maria Rojas López
Samuel Agudelo Quiróz
