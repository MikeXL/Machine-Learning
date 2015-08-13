Coursera Practical Machine Learning Writeup
===

##Introduction


##Variable selection and Model building

```
var.selected <- c()
fit <- knn(classe ~ var.selected, data = train)
```


##Validation
in sample error = .329
out sample error = .341

##Considerations




🖖

___________________          _-_
\==============_=_/ ____.---'---`---.____
            \_ \    \----._________.----/
              \ \   /  /    `-_-'
          __,--`.`-'..'-_
         /____          ||
              `--.____,-'


[1]: http://mikexl.github.io/machine-learning/coursera-pml.html
[2]: http://groupware.les.inf.puc-rio.br/har
[3]: https://class.coursera.org/predmachlearn-031/human_grading/view/courses/975200/assessments/4/submissions/36
