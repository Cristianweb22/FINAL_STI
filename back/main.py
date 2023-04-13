from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

# Declare the APP server instance
app = Flask(__name__)
# Enable CORS policies
CORS(app)

df = pd.read_csv('random_data.csv')
names = list(df['Name'])

# GET Endpoint =============================================================================
@app.route("/names", methods=["GET"])
def index():
  global names
  return jsonify({
    "names": names, 
    "columns": list(df.columns)
  })

# POST Endpoint =============================================================================
@app.route('/post_endpoint', methods=['POST'])
def create_data():
    # Get the data from the POST endpoint
    data = request.get_json()
    if not data:
        return (jsonify({'error': 'No data provided'}), 400)
    print(df[df['Name'] == data['person1']])
    return (jsonify({'response': 'ok all good', 'data': data}), 201)

# Execute the app instance
# The app will run locally in: http://localhost:5001/ after execution
if __name__ == "__main__":
  app.run(debug=True, port=5001)