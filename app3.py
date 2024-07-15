from flask import Flask, render_template, request, jsonify
import pandas as pd
import xgboost as xgb
from datetime import datetime

app = Flask(__name__)

def convert_dates(data):
    for record in data:
        # Assuming the date field is named 'date'
        date_str = record['Date']
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        record['Date'] = date_obj.strftime('%Y-%m-%d')
    return data
def extract_columns(data, columns):
    return [{col: record[col] for col in columns} for record in data]
@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/predict')
def predict():
    stock = request.args.get('stock')
    # load the data
    data = pd.read_csv(r'SPY.csv')

    # show the data
    # Display the plot
    #plt.show()
    # split the data into training and testing
    train_data = data.iloc[:int(.90*len(data)),:]
    test_data = data.iloc[int(.90*len(data)):,:]

    # define the features and target variables
    features = ['Open','Volume']
    target = 'Close'

    # create and train the model
    xgb_model = xgb.XGBRegressor()
    xgb_model.fit(train_data[features], train_data[target])

    # make and show the predictions on the test data
    predictions = xgb_model.predict(test_data[features])

    # show the models accuracy
    accuracy = xgb_model.score(test_data[features], test_data[target])

    data2 = {
        'Date': pd.date_range(start='07/01/2024', periods=5).strftime('%m/%d/%Y').tolist(),
        'Close': [150, 152, 153, 155, 158]
    }
  
    df = pd.DataFrame(test_data)
    # Convert the dataframe to a list of dictionaries
    predicted_data = df.to_dict(orient='records')
    converted_data = convert_dates(predicted_data)
    columns_to_extract = ['Date', 'Close']
    extracted_data = extract_columns(converted_data, columns_to_extract)
    return jsonify(extracted_data)


if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)