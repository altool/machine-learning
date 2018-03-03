import csv
import numpy
from sklearn.svm import SVR
import matplotlib.pyplot as plot

dates = []
prices = []

def getData(fileName):
    with open(fileName, 'r') as cv:
        csvFileReader = csv.reader(cv)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))

    return

# Builds the predictive model and graph
def predictPrice(dates, prices, x):
    dates = numpy.reshape(dates, (len(dates), 1)) # TODO check this
    svrLength = SVR(kernel='linear', C=1e3)
    svrPoly = SVR(kernel='poly', C=1e3, degree=2)
    svrRadioBasisFunction = SVR(kernel='rbf', C=1e3, gamma=0.1)

    svrLength.fit(dates, prices)
    svrPoly.fit(dates, prices)
    svrRadioBasisFunction.fit(dates, prices)

    plot.scatter(dates, prices, color='black', label='Data')
    plot.plot(dates, svrRadioBasisFunction.predict(dates), color='red', label='RBF model')
    plot.plot(dates, svrLength.predict(dates), color='green', label='Linear model')
    plot.plot(dates, svrPoly.predict(dates), color='orange', label='Polynomial model')
    plot.xlabel('Date')
    plot.ylabel('Price')
    plot.title('Support Vector Regression')
    plot.legend()
    plot.show()

    return svrRadioBasisFunction.predict(x)[0], svrLength.predict(x)[0], svrPoly.predict(x)[0]

getData('../aapl.csv')

predictedPrice = predictPrice(dates, prices, 29)
print(predictedPrice)
