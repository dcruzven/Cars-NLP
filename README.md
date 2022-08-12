# Used Car Sale Predictions

# Overview
This project focuses on trying to predict a price range for a used car. Our clients want an estimated price range for a used car. The goal would be to build a predictive model that does that. The data was web-scraped from Cars.com. The data scraped came from 9k used cars in Alabama. Relevent data was scraped, such as year, make, mpg, etc. Reviews of the cars were also aquired. This is all data the average client can look up when buying a used car. The data was very messy and a lot of steps were taken to clean it. This included extracting certain words, turning number details into numeric values for models. The reviews were also cleaned. Many natural language process methods were done to the reviews. This was an attempt to use reviews as a metric to predict price. The final model was not useful, despite the NLP methods.The best model was an XGBoost model. This model used the details of a car to predict price range. A good accuracy scored was recieved to satisfy the clients.
# Business Problem
Average car buyers can have a hard time when looking for used cars. When do they do find a used car they want, they can be unsure about the sale price. Clients want to use car details and reviews found online to get an estimated price range.

Goal is to create a model to recieve details about a car and be able to predict a range of the sale price. The model can be used as a starting point when looking at a car's sale price.

# Data Understanding
Data was gathered from Cars.com. It was web-scraped using the python library BeautifulSoup. The data scraped included a lot of details from the car. The details include, year/make/model/mileage, engine specifications, and the reviews for that model.

A total of ~9k car's data were collected. These were all the used cars within a 200 mile radius of Birmingham, AL.

Using Cars.com gave the basics of a car including a sale price. This is information anyone can look up when looking for a used car, so it is the best information to use in order to predict a sale price range. The reviews were also gathered, it is additional information that could be useful. The review of a car could have an effect on the price, this will be explored.

There were some limitations and problems that the data has. There were only ~9k entries, this is okay but more would have been better. Since it was web-scraped, some information of the cars were not saved. At times the incorrect value would be in the incorrect column. The data also came out very messy so a lot of data cleaning would have to be done. The review portion of the data also has limitations. Although ~9k reviews were colleceted, only a portion (1.8k) were unique. This is because the same model cars also used the same reviews. This would limit how accurate a model can predict a sale price range due to the amount of repeated reviews.S

# Methods
Data cleaning was a big part of the project. In order to model anything, the data has to be clean and usable. Many cleaning methods were used. The first thing was to clean up any text with special characters. This will make the process of getting certian words/numbers from the text easier. Any numerical value had to be converted into an actual numeric value a model can use. The biggest problem after were incorrect values in certain columns. Indicator columns were used in order to get the correct value. Once the data cleaning was done, we could proceed with modeling. 

Two models were created using different metrics. One model used the details of the car. The second model used the car reviews.

The first model was an XGBoost model. This is a good model to use when predicted multiclass problems (The price ranges consisted of three bins). This model used the basic car details to predict prices. Preprocessing steps were taken to prepare the car details. This included scaling, one hot encoding, and creating a pipeline. 

In order to get reviews into a model, a lot of work was done in exploring NLP (Natural Language Processing). Stemming/Lemmantizing was attempted. This is the process of reducing words down to their root/stem. Different vectorizers were also used. Vectorizers give a value to each unique word. This can be the amount of times the words appeared. Sentiment analysis was also explored. This gave the review a positve or negative sentiment in a numeric value. In the end, none of these metrics was able to produce a useful model with good predictions.


# Results
The best prediction scores came from the XGBoost model using car details. The model had accuracy score of 73%. The NLP model was not a useful model (produced an accuracy score of 41%).

# Conclusions
- Model is able to give a good starting price point for clients

    - Clients can be confident the model's prediction can give them a good price range for a used car
- Difficult to incorporate reviews as a metric into predicting car price

    - There were not enough unique reviews to make a good predictions
    - Even when trying different NLP approaches, model did not get any better.
    - It did good for the data it had, but not worth putting into a model

# Future Analysis
- Collect more unique reviews
    - Having more unique reviews will be more useful for the model
- Find a way to better incorporate both models
    - By incorporating two models, one for reviews and one for car details, could produce a more accurate prediction
- Create a better web-scraper/ Collecting more data
    - Having more data is good, in this case more data means different cars from different states/larger radius.

# For More Information

Contact: [David Cruz](mailto:dcruzven20@gmail.com)
