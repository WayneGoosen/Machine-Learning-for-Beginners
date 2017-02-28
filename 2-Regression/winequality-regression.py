import csv
from sklearn import linear_model

with open('./Dataset/winequality-red.csv', 'rb') as csvfile:
  winereader = csv.reader(csvfile, delimiter=';', quotechar='"')
  for row in winereader:
    print row

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(wine_X_train, wine_y_train)


