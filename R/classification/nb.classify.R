library(e1071)

naiveBayes(Species ~ Sepal.Length + Sepal.Width, data=iris )
