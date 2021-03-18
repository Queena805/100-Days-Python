import requests
import json
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "AFLOZNBVC1OF9PKM"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "7e87e380533149249c832b2ade4b7a08"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API_KEY


}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
# print(json.dumps(data,sort_keys=True, indent=2))

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

yesterday_price = data["Time Series (60min)"]["2021-03-17 20:00:00"]["4. close"]
# print(f"The yesterday price is {yesterday_price}")

#TODO 2. - Get the day before yesterday's closing stock price

the_day_before_yesterday_price = data["Time Series (60min)"]["2021-03-16 20:00:00"]["4. close"]
# print(f"The day before yesterday price is {the_day_before_yesterday_price}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_price) - float(the_day_before_yesterday_price))
# print(the_difference)



#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = (difference / (float(yesterday_price))) * 100



#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").





    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_parameters = {
    "q": COMPANY_NAME,
    "from": "2021-03-17",
    "sortBy": "publisedAt",
    "apikey": NEWS_API_KEY

}




get_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
get_news.raise_for_status()
news = get_news.json()
print(json.dumps(news,sort_keys=True, indent=2))



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

news_article =[]
for article in news["articles"][0:3]:
    news_article.append(article)


print(news_article)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

news_list = [[new_item["title"],new_item["description"]] for new_item in news_article]
print(news_list)


#TODO 9. - Send each article as a separate message via Twilio.
MY_EMAIL = "jingnasong805@gmail.com"
PASSWORD= "Sjn18275771142"

if percentage_difference > 5:
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        for article in news_list:
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="paulvulf@gmail.com",
                                msg=f"Subject: Today\'s News: {article[0]}\n{article[1]}")



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

