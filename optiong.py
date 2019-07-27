from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
ts = TimeSeries(key='JBOKIRXPVJF8G5R9',output_format='pandas')

data,meta_data= ts.get_intraday(symbol='BHP.AX',interval='1min',outputsize='full')
latest=data.tail(1)
spot_price1=latest.iloc[0]['4. close']

contract_size=1000 
strike_price1=40
prem1=0.25
net_put = (spot_price1-strike_price1-prem1)*contract_size
print(int(net_put))

data,meta_data= ts.get_intraday(symbol='MQG.AX',interval='1min',outputsize='full')
latest=data.tail(1)
spot_price2=latest.iloc[0]['4. close']

contract_size=1000
strike_price2=129.4
prem2=0.65
net_call = (spot_price2-strike_price2-prem2)*contract_size
print(int(net_call))

if net_call-net_put > 0:
    print("John is winning")
else:
    print("Jack is winning")
