import requests
import time
from bs4 import BeautifulSoup

def openfile():
    counter = 0
    #set empty dictionary
    filestockdictionary = {}
    #read the stock_list file
    stockfile = open('stock_list.csv', "r")
    #sort data into key, value pairs
    for line in stockfile:
        #skip header line
        counter += 1
        if counter != 1:
            #split symbol from name
            keys_values = line.split(",", 1)
            #set symbol to key and name to the value 
            filestockdictionary[keys_values[0]] = (keys_values[1].strip())

    return filestockdictionary



def export_data(list_of_stocks):
    export_file = open("stocks.csv", "w")

    #write a header row in the csv file
    header_row = ""
    for key in list_of_stocks[0]:
        header_row += key+","

    export_file.write(f"{header_row}\n")

    #loop through list of stocks
    for stock in list_of_stocks:
        stock_record = ""
        #write stock indicators to the file
        for indicator, value in stock.items():
            stock_record += value+","
        #write record to file
        export_file.write(f"{stock_record}\n")
    
    export_file.close()
    
    return


def main():
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
    
    #symbols_list = ["GOOGL", "IBM", "SBUX", "AMC", "NFLX", "TSLA", "BA", "CSCO", "INTC", "ORCL", "JNJ", "WMT"]
    symbols_list = []

    #run the program to read additional stocks from file
    stockdictionary = openfile()
    #loop for each key value pair
    for stock in stockdictionary:
        #add key (symbol) to the existing list and avoid repeating stocks
        #if stock not in symbols_list: (only needed if you un-comment the existing symbol list)
            symbols_list.append(stock)

    list_of_stock_dictionaries = []
    
    for symbol in symbols_list:
        print(f"Requesting data for {stockdictionary[symbol]}: {symbol} stock")
        url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch'

        #request the page
        response = requests.get(url, headers=headers)

        #parse html and create a bueatiful soup object
        soup = BeautifulSoup(response.text, 'html.parser')

        stock_dictionary = {}
        stock_dictionary['symbol'] = symbol

        counter = 1
        #loop through the cell in the table
        for cell in soup.find_all('td'):
            #odd iterations are keys. Set key on odd numbered iterations
            if counter % 2 != 0:
                key = cell.text
            else:
                #enter key, value info in to the dictionary on even iterations
                value = cell.text.replace(",", "")
                stock_dictionary[key] = value
            #increment counter
            counter += 1
        
        #append stock dictionary to the list of dictionaries
        list_of_stock_dictionaries.append(stock_dictionary)

        #time.sleep(2)
    
    export_data(list_of_stock_dictionaries)

main()
