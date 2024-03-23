# Comparative Analysis Forecasting

This is a very complex dive into forecasting using LSTM, sentiment analysis, transformer layers and Federated Learning.

## LSTM Simple Comparative Analysis Folder

This is the folder that we started off with, comparing a simple LSTM model on how well it does to forecast stock prices based on the closing price, opening price, adjusted volumes, volume etc...

We compared the LSTM model with public forecasting tools like Prophet, and other algorithms like SARIMAX, ARIMA, Simple Exponential Smoothing, etc...

We found that the LSTM model performs better for a short-term forecast than any other model we compared it to. Giving us a 65% trend accuracy.

## Initial Federated Learning

After creating a simple LSTM model for forecasting, we decided to make it more complex in an attempt to increase it's accuracy or precision. 

Integrating the concept of Federated Learning where we average out the weights and baises and send them back to re-run our model with these new weights and basis could increase in our accuracy and precision. Even though it should be noted that the concept of Federated Learning is mainly intended for sharing weights and baises without having to share the data itself.

## Final Complex Forecasting

This is the final complex model we created, which introduced the idea of sentiment analysis and transformer layers. We performed a sentiment analysis on news articles related to those specific stocks (we only used news article headlines for sentiment analysis as we thought it was sufficient). 

The end results show us a significant increase in accuracy and precision of the forecasting and you can see these results for yourself.