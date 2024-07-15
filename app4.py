import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes

@app.route('/')
def predict():
    data = pd.read_csv(r'SPY.csv')
    test_data = data.iloc[int(.90*len(data)):,:]
    df = pd.DataFrame(test_data)
    # Convert the dataframe to a list of dictionaries
    predicted_data = df.to_dict(orient='records')
    print(predicted_data)
    return jsonify(predicted_data)

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)