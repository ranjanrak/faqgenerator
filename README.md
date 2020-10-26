# FaqGenerator

Simple FAQ generator for Kite connect Forum. We use this package periodically to look at latest frequently asked question on [Connect API Public Forum](https://kite.trade/forum/) and update [our FAQ page accordingly](https://kite.trade/forum/discussion/8019/faqs-on-pykiteconnect-specific-to-python-client#latest).<br/>
It accepts below two field from user:<br/>
`pages` -- number of recent pages to look for questions to generate FAQs <br/>
`match_factor` -- % text matching for each question

# Installation
``` 
git clone https://github.com/ranjanrak/FaqGenerator.git
```
# Usage
```
from forum_faq import FaqGenerator

forum_input = FaqGenerator(pages=3, match_factor=80)
faq_list = forum_input.question_match()
```
#### Response
```
[['Historical Option Chain 10 min interval data from where we get', 'Historical data', 'Historical API'], 
['Invalid API Key or Access Token - Historical Data', 'Wrong data in historical Api', 'Access Token', 'Historical data Api Limit', 'incorrect api key or access token'], 
['if condition error while placing order', 'Limit Order placing'], 
['raise error.ReactorNotRestartable()', 'WEBSOCKET STREAMING ERROR - ReactorNotRestartable'], 
['Stoploss order - InputException', 'InputException in API call kiteConnect.placeOrder for a VARIETY_CO order'], 
['Websocket API issue', 'Is there anyone who is using Azure data analytics service for websocket api?', 'Issue with Websockets API'], 
['Historical api returning none', 'Historical data returning null'], 
['ERROR:kiteconnect.ticker:Connection error: 1006', 'ERROR:kiteconnect.ticker:Connection closed: 1006 - connection was closed uncleanly (WebSocket connec'], 
['Login URL  {"status":"error","message":"The user is not enabled on the app.","data":null,"error_type', 'Error: the user is not enabled on the app.'], 
['Historical Data for Futures', 'Python Client is failing to get CONTINUOUS historical data for instrument'], 
['Kite Connect WebSocket Connection', 'Connection error Websocket'], 
['Historical API not working', 'Historical API not working']]
```
