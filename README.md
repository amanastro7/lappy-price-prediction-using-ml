# PRICE💰 PREDICTION OF LAPTOPS👨‍💻 USING MACHINE LEARNING🤖
![Display Image](https://github.com/amanastro7/lappy-price-prediction-using-ml/blob/main/images/gh_laptops.jpeg)



## WEB APP 🖥️
You Can Check The Deployed App On [Streamlit](https://amanastro7-lappy-price-prediction-using-ml-lappy-6ilv4i.streamlit.app/).

Here's a screenshot of the same:

![STREAMLIT SCREENSHOT](https://github.com/amanastro7/lappy-price-prediction-using-ml/blob/main/images/lappy_st.png)

Also Deployed On [HuggingFace Space](https://huggingface.co/spaces/amanastro07/sms-email-spam-clsfr)
(but it loads painfully slow as it is running on CPU).

Here's a screenshot of the same:

![HUGGING FACE SPACE SCREENSHOT]()



## SUMMARY 📝
The LAPTOP PRICE PREDICTOR is a machine learning web application that is designed predict the price of a laptop based on various specs such as processor type, memory size, storage capacity, screen resolutions, etc. The model was trained using a random forest regressor, which is a type of ensemble learning algorithm that uses multiple decision trees to make predictions. The training data included a range of laptop prices and features, and the model was able to learn the relationships between these variables. Once trained, the model was able to make good predictions on new data, allowing users to have a better understanding of how much they should expect to pay for a laptop with certain specifications.



## DATASET 📁
The dataset used for this project was found on [Kaggle](https://www.kaggle.com/datasets/mohidabdulrehman/laptop-price-dataset). The dataset is about laptops configuration with prices containing 1303 laptop data with 12 columns Company Name, Type Name, Laptop Size in (inches), Screen Resolution, CPU, RAM, Memory, GPU, Operating System And Price in INR.



## MACHINE LEARNING MODEL USED ⚙️🛠️

A random forest is a type of supervised machine learning algorithm that can be used for both classification and regression tasks. It is an ensemble model, which means that it is composed of multiple individual decision trees that work together to make predictions.

In a random forest regressor, each decision tree in the ensemble is trained to make predictions based on a random subset of the features in the dataset. The final prediction made by the random forest is the average of the predictions made by each decision tree.

Here's a simple example of how a random forest regressor might work:

First, the dataset is split into a training set and a test set.
Next, a number of decision trees are trained on the training set.
For each decision tree, a random subset of the features is selected and used to make predictions.
The predictions made by each decision tree are combined, and the final prediction is the average of all the individual predictions.
Here's a diagram illustrating the process:

![Random Forest Regressor](https://github.com/amanastro7/lappy-price-prediction-using-ml/blob/main/images/Random_forest_diagram_complete.png)

One of the main benefits of using a random forest is that it can reduce overfitting, which is a problem that can occur when a model is too complex and has too many parameters. By training multiple decision trees and averaging their predictions, the random forest is able to "smooth out" the predictions and make more accurate and stable predictions.


## MODEL SCORES 📊📉
The Dataset was trained on various regression algorithms like **LinearRegression, Ridge, Lasso, KNeighborsRegressor, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, ExtraTreesRegressor, SVR and XGBRegressor**.

The **RANDOM FOREST ALGORITHM** gave us a better metrics >>> **R<sup>2</sup> SCORE of the model was 0.88** and **MAE (Mean Absolute Error) was 0.16**.



## VIDEO DEMO OF THE WE APP
https://github.com/amanastro7/lappy-price-prediction-using-ml/blob/main/images/lappypred_vid_st.mp4
