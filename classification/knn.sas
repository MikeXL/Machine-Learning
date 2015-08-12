proc surveyselect data=iris  out=iris2  
                  samprate=0.7  method=srs  outall;
run;

proc discrim data=iris2(where=(selected=1))   
             test=iris2(where=(selected=0))
             testout=iris2testout
             method=NPAR k=5
             listerr crosslisterr; 
      class Species; 
      var SepalLength SepalWidth PetalLength PetalWidth; 
      title2 'Using KNN on Iris Data'; 
run; 
proc freq data=iris2testout;
     table Species*_INTO_;
run;

