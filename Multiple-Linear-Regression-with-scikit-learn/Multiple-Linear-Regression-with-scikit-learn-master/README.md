# Multiple-Linear-Regression-with-scikit-learn
Multiple Linear Regression with scikit-learn


Course Objectives:
In this project, I built and evaluated multiple linear regression models using Python. I used scikit-learn to calculate the regression, while using pandas for data management and seaborn for plotting. The data for this project consists of the very popular Advertising dataset to predict sales revenue based on advertising spending through media such as TV, radio, and newspaper.

By the end of this project, I was able to:

- Build univariate and multivariate linear regression models using scikit-learn
- Perform Exploratory Data Analysis (EDA) and data visualization with seaborn
- Evaluate model fit and accuracy using numerical measures such as R² and RMSE
- Model interaction effects in regression using basic feature engineering techniques


Project Structure

- Task 1: Introduction and Overview
 We will  introduce the model we will be building as well the Advertising dataset for this project.


- Task 2: Load the Data

In this task, we will load the very popular Advertising dataset about various costs incurred on advertising by different media such as through TV, radio, newspaper, and the sales for a particular product. Next, we will briefly explore the data to get some basic information about what we are going to be working with.

- Task 3: Relationship between Features and Target

It is good practice to first visualize the data before proceeding with analysis and model building. In this task, we will apply seaborn to create scatter plots of each of the three features and the target. This will allow to make a qualitative observations about the linear or non-linear relationships between the features and the target.

- Task 4: Multiple Linear Regression Model

We will extend the simple linear regression model to include multiple features. Our approach will give each predictor a separate slope coefficient in a single model. This way, we can avoid the drawbacks of fitting a separate simple linear model to each predictor. In this task, we use scikit-learn's LinearRegression( ) estimator to calculate the multiple regression coefficient estimates when TV, radio, and newspaper advertising budgets are used to predict sales revenue. Lastly, we will compare and contrast the coefficient estimates from multiple regression to those from simple linear regression.

- Task 5: Feature Selection

Do all the predictors help to explain the target, or is only a subset of the predictors useful? We will address exactly this question in this task. We will use feature selection to determine which predictors are associated with the response, so as to fit a single model involving only those features. We will use R², the most common numerical measure of model fit and understand its limitations.

- Task 6: Model Evaluation Using Train/Test Split and Model Metrics

Assessing model accuracy is very similar to that of simple linear regression. Our first step will be to split the data into a training set and a testing set using the train_test_split( ) helper function from sklearn.metrics. Next, we will create two separate models, one of which uses all predictors, while the other excludes newspaper. We fit the training set to the estimator and make predictions on the testing set. Model fit and the accuracy of the predictions will be evaluated using R² and RMSE. Visual assessment of our models will involve comparing the residual behaviors and the prediction errors using Yellowbrick. Yellowbrick is an open source, pure Python project that extends the scikit-learn API with visual analysis and diagnostic tools. It is commonly used inside of a Jupyter Notebook alongside pandas data frames.

- Task 7: Interaction Effect (Synergy) in Regression Analysis

From our previous analysis of the residuals, we concluded that we need to incorporate interaction terms due to the non-additive relationship between the features and target. A simple method to extend our model to allow for interaction effects is to include a third feature by taking the product of the other two features in our model. This feature will have its separate slope coefficient which can be interpreted as the increase in the effectiveness of radio advertising for a one unit increase in TV advertising or vice versa.


###CERTIFICATE DETAILS

- Name: Multiple Linear Regression with scikit-learn
- Issuing Organization: Coursera
- Issue Date: May 2020
- Expiration Date: This certification does not expire
- Credential ID: 9XMUAVXTPJWJ
- Credential URL: https://www.coursera.org/account/accomplishments/certificate/9XMUAVXTPJWJ
