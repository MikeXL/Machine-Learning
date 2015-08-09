fit <- kmeans(c(iris$Sepal.Length, iris$Sepal.Width, iris$Petal.Width, iris$Petal.Length), 3)
iris2 <- data.frame(iris, fit$cluster)
library(ggvis)
iris2 %>% 
	ggvis(~Sepal.Length, ~Sepal.Width, fill = ~fit.cluster)

