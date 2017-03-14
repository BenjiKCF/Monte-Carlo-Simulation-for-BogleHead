import random
import numpy

'''
Fill in the following information
'''
initial_amount = 10000
annual_contribution = 120000
period = 20
inflation = 0.0447 # HK mean from 1981 until 2017

#mean = 0.12
#sd = 0.14

HSI_return = [-27.8,6.7,14.6,31.1,41.4,48.6,15.7,4.5,22.1,-18.0,1.6,51.7,-5.4,-21.5,-14.4,24.6,16.7,4.5,36.5,34.8,-47.4,52.0,5.3,-20.0,22.9,2.9,1.3]

mean = sum(HSI_return) // len(HSI_return)
sd = 0.5997


times = 10000
'''
The End
'''

def annual_return(mean, sd):
    return numpy.random.normal(loc=mean, scale=sd)
# print annual_return(50, 25)

def portfolio(initial_amount, annual_contribution, period, inflation, mean, sd):
    portfolio_value = initial_amount
    portfolio_period = 0
    while portfolio_period < period:
        portfolio_value = portfolio_value * (1 + annual_return(mean, sd))
        portfolio_value += annual_contribution
        portfolio_value = portfolio_value / (1-inflation)
        portfolio_period += 1
    return portfolio_value
# print portfolio(initial_amount, annual_contribution, period, inflation, mean, sd)

def monte_carlo_simulation(initial_amount, annual_contribution, period, inflation, mean, sd, times):
    hm_times = 0
    test_result = []
    while hm_times < times:
        value = portfolio(initial_amount, annual_contribution, period, inflation, mean, sd)
        test_result.append(value)
        hm_times += 1
    return numpy.median(test_result)
print monte_carlo_simulation(initial_amount, annual_contribution, period, inflation, mean, sd, times)
