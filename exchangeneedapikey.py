import requests
import json

api_url = "http://api.exchangeratesapi.io/v1/latest?access_key="

currency_type = str(input("Currency type: "))
currency_received = str(input("Type of currency received: "))
amount = int(input( f"How much {currency_type} do you want to exchange ? " ))

result =  requests.get(api_url + currency_type)


result = json.loads(result.text)
print ("1 {0} = {1} {2} ".format(currency_type, result["rates"][currency_received],currency_received))

print (" {0} {1} = {2} {3} ".format(amount, currency_type, amount*result ["rates"][currency_received], currency_received))