from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo
with open('modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('escalador.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los parámetros ingresados por el usuario
    temperatura = float(request.form['temperatura'])
    radiacion = float(request.form['radiacion'])
    tipo_panel = request.form['tipo_panel']

    # Convertir el tipo de panel en formato compatible con el modelo
    tipo_panel_map = {'CIGS': 0, 'HIT': 1, 'm-Si': 2}
    panel_code = tipo_panel_map[tipo_panel]

    # Crear los datos de entrada para el modelo
    X_imput= np.array([[temperatura, radiacion, panel_code]])

    # Convertir la entrada en un DataFrame con los mismos nombres de columnas
    X_imput_df = pd.DataFrame(X_imput, columns=['Irradiance', 'Tamb', 'Panel'])

    # Escalar los datos de entrada
    X_imput_escalado = scaler.transform(X_imput_df)

    # Realizar la predicción
    potencia_predicha = modelo.predict(X_imput_escalado)[0]

    return render_template('index.html', potencia=potencia_predicha, tipo_panel=tipo_panel)

if __name__ == '__main__':
    app.run(debug=True)


