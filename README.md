

# Gold-Price-Prediction
This repository contains code for a project that uses machine learning to predict future gold prices based on historical data. The project is implemented in Python, using the Scikit-learn library for machine learning and Pandas library for data manipulation. The data used for this project is sourced from Kaggle's historical gold prices dataset.

# Dependencies<br>
The following dependencies are required to run this project:<br>

Python 3<br>
Pandas<br>
NumPy<br>
Scikit-learn<br>
joblib<br>

# Gold Price Prediction
 given some information about dataset like:<br>
 
 1. Date<br>
 2. SPX<br>
 3. GLD<br>
 4. USO<br>
 5. SLV<br>
 6. EUR/USD<br>

 # How  did I do?

<h3>The dataset I am using for the Gold Price Prediction task is downloaded from Kaggle. Now let’s start with this task by importing the necessary Python libraries and dataset:<br></h3>
import numpy as np<br>
import pandas as pd<br>
import seaborn as sns<br>

![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/2b02c8d6-9dea-4433-a43d-6b735050f2ce)
![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/e298d15b-d880-4e41-9fa8-b59721e73a55)

<h2>Now before moving forward, let’s have a look at whether this dataset contains any null values or not:</h2>

![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/6ff87214-7789-4283-b113-a0a9921247d7)

<h2>The dataset is ready to use because there are no null values in the data.</h2>

# Gold Price Prediction Model
<h2>Now let’s move to the task of training a machine learning model for predicting the gold price. Here, I will first start by splitting the data into training and test sets:</h2>

![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/1d89b313-f261-475d-9812-c2725ad37c2a)
![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/4dcdb006-036c-43e1-b12e-6a03cf65cd5b)

<h2>Here I have used three models that is linear reg , random forest and gradient boosting regressor</h2>

![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/3b803992-958b-4013-89b4-4917d1fd877f)
<h2>out of which random forests score is more that is 98%</h2>

# result

![image](https://github.com/Sanketarali/Gold-Price-Prediction/assets/110754364/30027835-9ea2-4b2b-9121-55ca2292b066)








