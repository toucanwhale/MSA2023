import requests
import time
from bs4 import BeautifulSoup

def export_data(list_of_stocks):
    export_file = open("stocks.csv", "w")
    #write a header row in the csv file
    for key in list_of_stocks[0]:

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
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    symbols_list = {"GOOGL","IBM","SBUX","AMC","NFLX","TSLA","BA"}
    list_of_stock_dictionaries = []

    for symbol in symbols_list:
        url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch"
        #request the page
        response = requests.get(url, headers=headers)

        #parse html and create a beautiful soup object
        soup = BeautifulSoup(response.text, 'html.parser')


        stock_dictionary = {}
        stock_dictionary['symbol'] = symbol

        counter = 1
        #loop through the cells in the table
        for cell in soup.find_all('td'):
            #odd iterations are keys, so set key on oddnumbered iterations
            if counter % 2 != 0:
                key = cell.text
            else:
                #enter key, value info into the dictionary on even iterations
                stock_dictionary[key] = cell.text


            #increment counter
            counter += 1            
        
        #append stock dictionary to the list of dictionaries
        list_of_stock_dictionaries.append(stock_dictionary)

        time.sleep(2)

    for stock in list_of_stock_dictionaries:
        print(list_of_stock_dictionaries)
        export_data()


        



main()