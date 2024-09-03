**Introduction**
Many parents aim to set their children in an environment where they can thrive academically, but are unsure of which factors are the most important. This project uses data collected from two Portuguese secondary
schools, and contains 30 features about student, ranging from information about their parent's success, to their interests after high school, to what they spend their time doing outside of school hours. This 
analysis visualizes which features have strong effects on performance, and develops a model predicting student performance based on the given set of features.

**Dataset**
This dataset comes from the uci machine learning repo. 

Cortez, Paulo. “[Pdf] Using Data Mining to Predict Secondary School Student Performance | Semantic Scholar.” Using Data Mining to Predict Secondary School Student Performance, Apr. 2008, www.semanticscholar.org/paper/Using-data-mining-to-predict-secondary-school-Cortez-Silva/61d468d5254730bbecf822c6b60d7d6595d9889c.  

**Results**
This project tests 3 different machine learning models: Linear Regression, SVMs, and Random Forest. The Random forest had the best results, with a RMSE of just under 3 and a MAE of just over two. The grading scale ranges from 0-20 points. 
The greatest indicators of a low score were the number of failed past classes, and if the student received supplemental help. The greatest indicators of a high score were if the student was interested in pursuing a 
higher education, the level of education that their mother has, and how much time they spend studying
