# Import relevant packages

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='JBOKIRXPVJF8G5R9',output_format='pandas')

# Create the first contract by retrieving intraday data for the chosen stock

data,meta_data= ts.get_intraday(symbol='BHP.AX',interval='1min',outputsize='full')
latest=data.tail(1)
spot_price1=latest.iloc[0]['4. close']

# Specify the conditions of the contract

contract_size=1000 
strike_price1=40
prem1=0.25

# Total profit for the first contract

net_put = (spot_price1-strike_price1-prem1)*contract_size

# Create the second contract by retrieving intraday data for the chosen stock

data,meta_data= ts.get_intraday(symbol='MQG.AX',interval='1min',outputsize='full')
latest=data.tail(1)
spot_price2=latest.iloc[0]['4. close']

# Specify the conditions of the contract

contract_size=1000
strike_price2=129.4
prem2=0.65

# Total profit for the second contract

net_call = (spot_price2-strike_price2-prem2)*contract_size

print(int(net_call))
print(int(net_put))

if net_call-net_put > 0:
    print("John is winning")
else:
    print("Jack is winning")
