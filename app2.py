from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/predict')
def predict():
    stock = request.args.get('stock')

    # Sample data for demonstration purposes
    data = {
        'date': pd.date_range(start='2024-07-01', periods=5).strftime('%Y-%m-%d').tolist(),
        'price': [150, 152, 153, 155, 158]
    }
    df = pd.DataFrame(data)

    # Convert the dataframe to a list of dictionaries
    predicted_data = df.to_dict(orient='records')
    return jsonify(predicted_data)

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)
