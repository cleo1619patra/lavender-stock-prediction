# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb

# load the data
data = pd.read_csv(r'SPY.csv')
print(data)

# show the data
data['Close'].plot()
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
print('model predictions:')
print(predictions)

# show the models accuracy
accuracy = xgb_model.score(test_data[features], test_data[target])
print('Accuracy:')
print(accuracy)

# plot the presentation and the close price
plt.plot(data['Close'],label='Close price ')
plt.plot(test_data[target].index,predictions,label='predictions')
plt.legend()
plt.show()