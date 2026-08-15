#pip install streamlit numpy pandas pillow

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title(" Meu Photoshop Matemático") 
st.write("Aplicando Álgebra Linear e Pandas em Imagens Reais!")

# Cria um botão de upload na tela
arquivo = st.file_uploader("Carregue a sua foto aqui:", type=['jpg', 'jpeg', 'png'])

if arquivo is not None:
 # 1. Abre e converte para tons de cinza
 imagem_original = Image.open(arquivo).convert('L')
 
 # 2. Redimensiona para evitar travamentos
 imagem_redimensionada = imagem_original.resize((500, 500))
 
 # 3. Converte a foto em uma Matriz NumPy
 matriz_imagem = np.array(imagem_redimensionada)
 
 st.image(imagem_redimensionada, caption="Sua Foto Original")

 st.subheader(" Painel de Controle Matemático") 
 
 brilho = st.slider("Brilho (Soma de um Escalar)", min_value=-100, max_value=100, value=0)
 contraste = st.slider("Contraste (Multiplicação por Escalar)", min_value=0.0, max_value=3.0, value=1.0)
 
 rotacionar = st.checkbox("Rotacionar 90º (Matriz Transposta)")
 espelhar = st.checkbox("Espelhar Horizontalmente (Inverter Colunas)")
 # Aplicação da Álgebra Linear
 matriz_processada = matriz_imagem * contraste + brilho
 matriz_processada = np.clip(matriz_processada, 0, 255).astype(np.uint8)
 
 if rotacionar:
  matriz_processada = matriz_processada.T
 
 if espelhar:
  matriz_processada = matriz_processada[:, ::-1]
 
  st.image(matriz_processada, caption="Imagem Processada via Matrizes")

  st.subheader(" Raio-X da Imagem com Pandas") 
 
  # Transforma a matriz 2D em 1D
  dados_pixels = matriz_processada.flatten()
 
  # Cria o DataFrame e gera estatísticas
  df_imagem = pd.DataFrame(dados_pixels, columns=['Intensidade do Pixel (0-255)'])
  st.write(df_imagem.describe())
