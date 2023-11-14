# binance-spot-bollinger-calculator
Calculating bollinger values using Binance API

In this study, you can calculate the current bollinger data of the trading pair you want on the Binance spot exchange.

1- Download "bollinger_band.py"
</br>
2- Add <import bollinger_band> to the beginning of the your code page
</br>
3- You can call Bollinger data in your page as follows.
</br>
      <p style="text-indent:20px;">response = bollinger_band.binance("BTCUSDT", "15m")</p>
      </br>
      print(response)
      </br>
      print (response["UPPER"])
      </br>
      print (response["MIDDLE"])
      </br>
      print (response["LOWER"])
      </br>
      </br>

NOT: You can use example.py file for example.
