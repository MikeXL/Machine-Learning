library(rpart)
tree <- rpart(Species ~ Petal.Length + Petal.Width + Sepal.Length + Sepal.Width, data=iris)
tree
plot(tree)
text(tree)

fancyRpartPlot(tree)
