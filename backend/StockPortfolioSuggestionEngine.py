import datetime
import math
from flask import Flask
from flask import request
from pandas import DataFrame
import yfinance as yf
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


index_investing = ["IVV","FXAIX","SWPPX"]
ethical_investing = ["TSLA", "NEE", "GE"]
quality_investing = ["MSFT", "NKE", "CRM"]
growth_investing = ["AMZN", "SHOP", "EFC"]
value_investing = ["PAG", "CVS", "OMF"]



@app.route("/stocksuggestion", methods=['POST'])
def stock_investment():
    Investment = request.json['amount']
    Investing_Strategy = request.json['strategies'].split(",")
    return stocks_invest(Investing_Strategy, Investment)


def stocks_invest(Investing_Strategy, Investment):
    result = []
    if(len(Investing_Strategy) > 1):
        investment_strategy1 = int(Investment) / 2
        investment_strategy2 = int(Investment) / 2
        response_for_strategy1 = []
        response_for_strategy2 = []
        suggested_stocks = []
        

        if(Investing_Strategy[0] == "Index Investing" or Investing_Strategy[0] == "Ethical Investing" or Investing_Strategy[0] == "Growth Investing" or Investing_Strategy[0] == "Quality Investing" or Investing_Strategy[0] == "Value Investing"):
            if Investing_Strategy[0] == "Ethical Investing":
                    suggested_stocks.append((ethical_investing[0]))
                    suggested_stocks.append((ethical_investing[1]))
                    suggested_stocks.append((ethical_investing[2]))
            elif Investing_Strategy[0] == "Growth Investing":
                    suggested_stocks.append((growth_investing[0]))
                    suggested_stocks.append((growth_investing[1]))
                    suggested_stocks.append((growth_investing[2]))
            elif Investing_Strategy[0] == "Index Investing":
                    suggested_stocks.append((index_investing[0]))
                    suggested_stocks.append((index_investing[1]))
                    suggested_stocks.append((index_investing[2]))
            elif Investing_Strategy[0] == "Quality Investing":
                    suggested_stocks.append((quality_investing[0]))
                    suggested_stocks.append((quality_investing[1]))
                    suggested_stocks.append((quality_investing[2]))
            elif Investing_Strategy[0] == "Value Investing":
                    suggested_stocks.append((value_investing[0]))
                    suggested_stocks.append((value_investing[1]))
                    suggested_stocks.append((value_investing[2]))

            response_for_strategy1 = (investment_breakdown(suggested_stocks))
            stock_dict = {}
            stock_unit = {}
            
            for i in response_for_strategy1:
                stock_dict[i['companyName']] = i['currentPrice']
                stock_unit[i['companyName']] = 0
            flag = 'true'
            while investment_strategy1 >= 0 and flag == 'true':
                
                flag = 'false'
                for i in stock_dict:
                    
                    if investment_strategy1 >= stock_dict.get(i):
                       investment_strategy1 = investment_strategy1 - stock_dict.get(i)
                       stock_unit[i] = stock_unit.get(i)+1
                       flag = 'true'
                    else :
                        for i in stock_dict:
                            if investment_strategy1 > stock_dict.get(i)  :
                                flag = 'true'
            for i in response_for_strategy1:
                if stock_unit[i['companyName']] > 0:
                    company_stock_data = {}
                    company_stock_data['CompantName'] = i['companyName']
                    company_stock_data['CurrentPrice'] =(i['currentPrice'])
                    company_stock_data['PercentageChange']=(i['percentage_change'])
                    company_stock_data['ValueChange']=(i['value_change'])
                    company_stock_data['UnitsYouCanBuy'] = stock_unit[i['companyName']]
                    company_stock_data['AmountYouInvest'] = stock_unit[i['companyName']]*i['currentPrice']
                    company_stock_data['Strategy'] = Investing_Strategy[0]
                    ticker = yf.Ticker(i['ticker'])
                    data = DataFrame(ticker.history(period = '5d'))
                    temp_data = data.T
                    dataList = [datetime.datetime.date(cols) for cols in temp_data.columns]
                    historical_data = []
                    historical_dates = dataList
                    for i in range(0,len(data['Open'])):
                        if(math.isnan(data['Open'][i])):
                            historical_data.append(0)
                        else:    
                            historical_data.append(data['Open'][i])


                    company_stock_data['HistoricalData'] = historical_data   
                    company_stock_data['HistoricalDates'] = historical_dates
                    result.append(company_stock_data) 
                     
            print(result)            
                
        if(Investing_Strategy[1] == "Index Investing" or Investing_Strategy[1]  == "Ethical Investing" or Investing_Strategy[1]  == "Growth Investing" or Investing_Strategy[1]  == "Quality Investing" or Investing_Strategy[1]  == "Value Investing"):
            suggested_stocks = []
            if Investing_Strategy[1]  == "Ethical Investing":
                    suggested_stocks.append((ethical_investing[0]))
                    suggested_stocks.append((ethical_investing[1]))
                    suggested_stocks.append((ethical_investing[2]))
            elif Investing_Strategy[1] == "Growth Investing":
                    suggested_stocks.append((growth_investing[0]))
                    suggested_stocks.append((growth_investing[1]))
                    suggested_stocks.append((growth_investing[2]))
            elif Investing_Strategy[1]  == "Index Investing":
                    suggested_stocks.append((index_investing[0]))
                    suggested_stocks.append((index_investing[1]))
                    suggested_stocks.append((index_investing[2]))
            elif Investing_Strategy[1]  == "Quality Investing":
                    suggested_stocks.append((quality_investing[0]))
                    suggested_stocks.append((quality_investing[1]))
                    suggested_stocks.append((quality_investing[2]))
            elif Investing_Strategy[1]  == "Value Investing":
                    suggested_stocks.append((value_investing[0]))
                    suggested_stocks.append((value_investing[1]))
                    suggested_stocks.append((value_investing[2]))
            stock_dict = {}
            stock_unit = {}
            response_for_strategy2 = (investment_breakdown(suggested_stocks))
           
            for i in response_for_strategy2:
                stock_dict[i['companyName']] = i['currentPrice']
                stock_unit[i['companyName']] = 0   
            flag = 'true'
            while investment_strategy2 >= 0 and flag == 'true':
                flag = 'false'
                for i in stock_dict:
                    if investment_strategy2>= stock_dict.get(i):
                       investment_strategy2 = (investment_strategy2) - stock_dict.get(i)
                       stock_unit[i] = stock_unit.get(i)+1
                       flag = 'true'
                    else :
                        for i in stock_dict:
                            if investment_strategy2 > stock_dict.get(i)  :
                                flag = 'true'


            for i in response_for_strategy2:
                if stock_unit[i['companyName']] > 0:
                    company_stock_data = {} 
                    company_stock_data['CompantName'] = i['companyName']
                    company_stock_data['CurrentPrice'] =(i['currentPrice'])
                    company_stock_data['PercentageChange']=(i['percentage_change'])
                    company_stock_data['ValueChange']=(i['value_change'])
                    company_stock_data['UnitsYouCanBuy'] = stock_unit[i['companyName']]
                    company_stock_data['AmountYouInvest'] = stock_unit[i['companyName']]*i['currentPrice']
                    ticker = yf.Ticker(i['ticker'])
                    company_stock_data['Strategy'] = Investing_Strategy[1]
                    data = DataFrame(ticker.history(period = '5d'))
                    temp_data = data.T
                    dataList = [datetime.datetime.date(cols) for cols in temp_data.columns]
                    historical_data = []
                    historical_dates = dataList
                    for i in range(0, len(data['Open'])):
                        if(math.isnan(data['Open'][i])):
                            historical_data.append(0)
                        else:    
                            historical_data.append(data['Open'][i])
                    company_stock_data['HistoricalData'] = historical_data
                    company_stock_data['HistoricalDates'] = historical_dates    
                    result.append(company_stock_data)  
            print(result)
    else:
        investment_strategy1 = int(Investment)        
        response_for_strategy1 = []
        suggested_stocks = []
        

        if(Investing_Strategy[0] == "Index Investing" or Investing_Strategy[0] == "Ethical Investing" or Investing_Strategy[0] == "Growth Investing" or Investing_Strategy[0] == "Quality Investing" or Investing_Strategy[0] == "Value Investing"):
            if Investing_Strategy[0] == "Ethical Investing":
                    suggested_stocks.append((ethical_investing[0]))
                    suggested_stocks.append((ethical_investing[1]))
                    suggested_stocks.append((ethical_investing[2]))
            elif Investing_Strategy[0] == "Growth Investing":
                    suggested_stocks.append((growth_investing[0]))
                    suggested_stocks.append((growth_investing[1]))
                    suggested_stocks.append((growth_investing[2]))
            elif Investing_Strategy[0] == "Index Investing":
                    suggested_stocks.append((index_investing[0]))
                    suggested_stocks.append((index_investing[1]))
                    suggested_stocks.append((index_investing[2]))
            elif Investing_Strategy[0] == "Quality Investing":
                    suggested_stocks.append((quality_investing[0]))
                    suggested_stocks.append((quality_investing[1]))
                    suggested_stocks.append((quality_investing[2]))
            elif Investing_Strategy[0] == "Value Investing":
                    suggested_stocks.append((value_investing[0]))
                    suggested_stocks.append((value_investing[1]))
                    suggested_stocks.append((value_investing[2]))

            response_for_strategy1 = (investment_breakdown(suggested_stocks))
            stock_dict = {}
            stock_unit = {}

            for i in response_for_strategy1:
                stock_dict[i['companyName']] = i['currentPrice']
                stock_unit[i['companyName']] = 0   
            flag = 'true'
            while investment_strategy1 >= 0 and flag == 'true':
                
                flag = 'false'
                for i in stock_dict:
                    
                    if investment_strategy1 >= stock_dict.get(i):
                       investment_strategy1 = investment_strategy1 - stock_dict.get(i)
                       stock_unit[i] = stock_unit.get(i)+1
                       flag = 'true'
                    else :
                        for i in stock_dict:
                            if investment_strategy1 > stock_dict.get(i)  :
                                flag = 'true'

            for i in response_for_strategy1:
                if stock_unit[i['companyName']] > 0:
                    company_stock_data = {}
                    company_stock_data['CompantName'] = i['companyName']
                    company_stock_data['CurrentPrice'] =(i['currentPrice'])
                    company_stock_data['PercentageChange']=(i['percentage_change'])
                    company_stock_data['ValueChange']=(i['value_change'])
                    company_stock_data['UnitsYouCanBuy'] = stock_unit[i['companyName']]
                    company_stock_data['AmountYouInvest'] = stock_unit[i['companyName']]*i['currentPrice']
                    ticker = yf.Ticker(i['ticker'])
                    company_stock_data['Strategy'] = Investing_Strategy[0]
                    data = DataFrame(ticker.history(period = '5d'))
                    temp_data = data.T
                    dataList = [datetime.datetime.date(cols) for cols in temp_data.columns]
                    historical_data = []
                    historical_dates = dataList
                    for i in range(0, len(data['Open'])):
                        if(math.isnan(data['Open'][i])):
                            historical_data.append(0)
                        else:    
                            historical_data.append(data['Open'][i])
                    company_stock_data['HistoricalData'] = historical_data   
                    company_stock_data['HistoricalDates'] = historical_dates
                    result.append(company_stock_data) 

            print(result)                 

   
    resultdict={}
    resultdict['result']=result
    return resultdict


def investment_breakdown(suggested_stocks):

    final_quote = []
    for ticker in suggested_stocks:
        stock = yf.Ticker(ticker)

        data = DataFrame(stock.history(period='1mo'))

        currentData = data.iloc[-1, :]
        previousData = data.iloc[-2, :]
        previousClose = float(previousData[3])
        currentValue = float(currentData[3])
        json_response={}
        value_change = round((currentValue-previousClose), 2)
        percentage_change = round(float((value_change/previousClose)*100), 2)
        value_change = ('+ ' + str(value_change)
                        ) if value_change >= 0 else str(value_change)
        percentage_change = ('+ ' + str(percentage_change) +
                             '%') if percentage_change >= 0 else str(percentage_change) + '%'
        
        json_response['companyName'] = stock.info['longName']
        json_response['currentPrice'] = currentValue
        json_response['ticker']=ticker
        json_response.update([('value_change', value_change), ('percentage_change', percentage_change)] )
        final_quote.append(json_response)

    return final_quote


if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(host="0.0.0.0", debug=True)
