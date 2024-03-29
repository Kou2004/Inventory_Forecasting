# Inventory_Forecasting
This project is a group project of team Terox , under the TinkerQuest24 hackathon, where we have made a Inventory Management App with demand forecasting. Here the forecasting part is done by me.
# Approach
The objective of the App to do the forecasting of the number of the booking of the patients with of different tests of different locations. For this , what I have done that:
1. Split the dataset first on the basis of the prefix of the Test_Code (Because many category of tests are occuring under this test, and adequate amount of data is available to make the forecasting of the data). After that I split the dataset further on the basis of the test_names.
2. Then see the trend of each smaller dataset with booking_date and collection_date wise, I found almost similar trend and seasonility across all the smaller datasets, so for a longer timestamp I have considered the booking date as my date_time_stamp.
3. First I have used SARIMA on the overall bookings of the whole source dataset, because as there are 90 days data, it will have the more probablity of capturing the all trends ,seasonality of the time series data.
4. I have used the ACF, PACF, ADfuller & Kpss tests, differencing, Auto ARIMA to find the optimal values of the P,Q,D in the SARIMA.
5. After that applied prophet model to get more accurate forecasting on the dataset.Also use Box_Cox_transformation to reduce the variance of the data and hyperparameter tuning according to the problem.
# Why prophet is prefered over ARIMA?
1. Generally ARIMA is useful for short term prediction, but in our problem, data is given upto 2nd Feb 2024, So I have to give around forecasting of the 50 days in future. In this case , as ARIMA uses the previous timestamp errors and values to forecast the future data, the variance of the data reduces continously and it gives us constant results which is not a good thing. Also it is unable to capture the trend , seasonility and outliers (high variance data) of the data.
2. On the other hand prophet is very robust model, which captures the trend of the data very well. In our case as trend is contiously decreasing, If I use ARIMA, it can give me negative results, but in prophet we can use the **growth** hyperparameter to set the lower value . Also in some smaller datasets , there are some timestamps missing, so in that case also prophet can handle this missing values accordingly.
3. Using Box_Cox_transformation ,reducing the variance of the data, we can handle the outliers of the data, and in such a way prophet can make more accurate prediction.
4. In future , if more data is feeded, we can train the model prophet on a regular interval basis to capture the seasonality and trend ,some sort of holiday effects of the number of bookings of the patients.
# Prophet_Model Pipeline:

![WhatsApp Image 2024-03-28 at 22 12 57_8070ea2d](https://github.com/Kou2004/Inventory_Forecasting/assets/145743404/934613a8-77a7-486f-b65f-e2db8fc481c6)


# Results:
Get a average MAE of 5.26 of all the smaller datasets. 
# improvements :
Feeding more data on the model, training the model on the regular interval basis, Some more testing with hyper-parameters of the prophet model.


