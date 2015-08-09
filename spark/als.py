from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS
from numpy import array
from pyspark.mllib.recommendation import Rating

data = sc.textFile("/tmp/test.data")
ratings = data.map(lambda line: Rating(*array([float(x) for x in line.split(',')])))
ratings.take(10)

model = ALS.train(ratings, 10, 20)
testdata = ratings.map(lambda p: (int(p[0]), int(p[1])))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))

predictions.collect()

ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).reduce(lambda x, y: x + y)/ratesAndPreds.count()
print("Mean Squared Error = " + str(MSE))
