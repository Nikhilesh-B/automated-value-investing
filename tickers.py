import csv

def returnTickers():
    NASDAQtickers = []
    NYSEtickers = []

    with open('NASDAQ_ticker_names.csv') as nasdaq_file:
        csv_reader = csv.reader(nasdaq_file, delimiter=",")

        for row in csv_reader:
            NASDAQtickers.append(row[0])

    nasdaq_file.close()

    with open('NYSEtickers.csv') as NYSE_file:
        csv_reader = csv.reader(NYSE_file, delimiter=",")

        for row in csv_reader:
            NASDAQtickers.append(row[0])

    NYSE_file.close()


    return NASDAQtickers, NYSEtickers


































