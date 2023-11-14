import bollinger_band

response = bollinger_band.binance("BTCUSDT", "15m")

print(response)
print (response["UPPER"])
print (response["MIDDLE"])
print (response["LOWER"])
