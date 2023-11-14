# binance-spot-bollinger-calculator
Calculating bollinger values using Binance API

In this study, you can calculate the current bollinger data of the trading pair you want on the Binance spot exchange.

1- Download "bollinger_band.py"
</br>
2- Add <import bollinger_band> to the beginning of the your code page
3- You can call Bollinger data in your page as follows.
      response = bollinger_band.binance("BTCUSDT", "15m")
      print(response)
      print (response["UPPER"])
      print (response["MIDDLE"])
      print (response["LOWER"])

NOT: You can use example.py file for example.
