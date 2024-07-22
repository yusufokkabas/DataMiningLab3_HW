Apply the following data preparation operations and techniques on the sample dataset CollegePlans. 

1.	Remove unimportant attributes which will not use for data mining algorithm.  

2.	Fill in missing values. 
     Possible filling types:
-	Fill with the most repeated value. 
-	Fill with a constant value 
-	Fill with the attribute mean
-	Fill with the value of the most similar record
            Use the first method (the most repeated value).

3.	Correct encoding errors. 
 

4.	Min-Max Normalization   
AverageGrade attribute.  Range [1 – 4]. 

5.	Equal Depth and Smooting by Bin Boundaries Method
 IQ attribute. Bin number: 4.

6.	Fixed k-Interval Discretization 
ParentIncome attribute. k=5.  Very High, High, Medium, Low, Very Low. 

7.	Concept Hierarchy Generation 
Region attribute.     

8.  Remove Noisy Data 
       Impossible, undefined, and abnormal values.        For example    IQ = -4169
       Replace with the most repeated value. 
