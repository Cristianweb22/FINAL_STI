from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors


# Declare the APP server instance
app = Flask(__name__)
# Enable CORS policies
CORS(app)

# Variables Globales ===================================================
df_prod = pd.read_csv('starbucks.csv', delimiter=';')
prod_knn = pd.DataFrame(df_prod.iloc[:,2:len(df_prod.columns)-1])
p_copy = prod_knn.copy()


# GET Endpoint =============================================================================
@app.route("/main", methods=["GET"])
def index():
  global p_copy
  cal_Q = 0
  fat_Q = 0
  carb_Q = 0
  fib_Q = 0
  prot_Q = 1
  bak = 1
  bow = 1
  hbf = 1
  parf = 1
  sal = 1
  sdwc = 1
  swee = 1
  p_copy['bakery']*= bak
  p_copy['bowl']*= bow
  p_copy['hot-breakfast']*= hbf
  p_copy['parfait']*= parf
  p_copy['salad']*= sal
  p_copy['sandwich']*= sdwc
  p_copy['sweet']*= swee
  p_copy['calories']*= cal_Q
  p_copy['fat']*= fat_Q
  p_copy['carb']*= carb_Q
  p_copy['fiber']*= fib_Q
  p_copy['protein']*= prot_Q

  # Filtrar segun tipos de alimentos que el usuario desea
  for idx, row in p_copy.iterrows():
    x = row.iloc[-5:].mean()
    if x == 0:
        p_copy = p_copy.drop(idx, axis = 0)
        
  # Normalizar p_copy para poder comparar
  norm_df = (p_copy - p_copy.min())/(p_copy.max() - p_copy.min())
  norm_df = norm_df.fillna(0)

  # Añadir el nuevo item a norm_df
  new_row = pd.DataFrame({'calories': [cal_Q], 'fat' : [fat_Q], 'carb' : [carb_Q], 'fiber' : [fib_Q], 'protein' : [prot_Q], 'bakery' : [bak], 'bowl' : [bow], 'hot-breakfast' : [hbf], 'parfait' : [parf],'salad' : [sal], 'sandwich' : [sdwc], 'sweet' : [swee]})
  norm_df = norm_df.append(new_row,ignore_index=True)

  # Ahora hay que sacar los indices y distancias de la tabla norm_df
  k3 = int(np.rint(np.sqrt(len(norm_df))))
  norm_neigh = NearestNeighbors(n_neighbors=k3, metric='cosine', algorithm='brute').fit(norm_df)
  distances, indices = norm_neigh.kneighbors(norm_df)

  # ahora ya tengo el "proto pedido" segun los coeficientes escogidos por el usuario. Debo acceder a distances y indices segun el protopedido y encontrar el knn
  meal_index = len(norm_df)-1
  p_names = df_prod['id']
  meal_neigh = [(p_names[idx], distances[meal_index][j]) for j, idx in enumerate(indices[meal_index])]

  message = []
  for v in meal_neigh:
    message.append(df_prod.iloc[v[0],1])
  return (message)




# POST Endpoint ================================================================
@app.route('/post_endpoint', methods=['POST'])
def create_data():
    # Get the data from the POST endpoint
    data = request.get_json()
    if not data:
        return (jsonify({'error': 'No data provided'}), 400)

    # cal_Q = data[0]
    # fat_Q = data[1]
    # carb_Q = data[2]
    # fib_Q = data[3]
    # prot_Q = data[4]
    # bak = data[5]
    # bow = data[6]
    # hbf = data[7]
    # parf = data[8]
    # sal = data[9]
    # sdwc = data[10]
    # swee = data[11]
    # p_copy['bakery']*= bak
    # p_copy['bowl']*= bow
    # p_copy['hot-breakfast']*= hbf
    # p_copy['parfait']*= parf
    # p_copy['salad']*= sal
    # p_copy['sandwich']*= sdwc
    # p_copy['sweet']*= swee
    # p_copy['calories']*= cal_Q
    # p_copy['fat']*= fat_Q
    # p_copy['carb']*= carb_Q
    # p_copy['fiber']*= fib_Q
    # p_copy['protein']*= prot_Q

    # # Filtrar segun tipos de alimentos que el usuario desea
    # for idx, row in p_copy.iterrows():
    #   x = row.iloc[-5:].mean()
    #   if x == 0:
    #       p_copy = p_copy.drop(idx, axis = 0)
          
    # # Normalizar p_copy para poder comparar
    # norm_df = (p_copy - p_copy.min())/(p_copy.max() - p_copy.min())
    # norm_df = norm_df.fillna(0)

    # # Añadir el nuevo item a norm_df
    # new_row = pd.DataFrame({'calories': [cal_Q], 'fat' : [fat_Q], 'carb' : [carb_Q], 'fiber' : [fib_Q], 'protein' : [prot_Q], 'bakery' : [bak], 'bowl' : [bow], 'hot-breakfast' : [hbf], 'parfait' : [parf],'salad' : [sal], 'sandwich' : [sdwc], 'sweet' : [swee]})
    # norm_df = norm_df.append(new_row,ignore_index=True)

    # # Ahora hay que sacar los indices y distancias de la tabla norm_df
    # k3 = int(np.rint(np.sqrt(len(norm_df))))
    # norm_neigh = NearestNeighbors(n_neighbors=k3, metric='cosine', algorithm='brute').fit(norm_df)
    # distances, indices = norm_neigh.kneighbors(norm_df)

    # # ahora ya tengo el "proto pedido" segun los coeficientes escogidos por el usuario. Debo acceder a distances y indices segun el protopedido y encontrar el knn
    # meal_index = len(norm_df)-1
    # p_names = df_prod['id']
    # meal_neigh = [(p_names[idx], distances[meal_index][j]) for j, idx in enumerate(indices[meal_index])]

    # message = []
    # for v in meal_neigh:
    #   message.append(df_prod.iloc[v[0],1])
      
    return (jsonify({'response': 'ok all good', 'data' : data}), 201)

# Execute the app instance
# The app will run locally in: http://localhost:5001/ after execution
if __name__ == "__main__":
  app.run(debug=True, port=5001)