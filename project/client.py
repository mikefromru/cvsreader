import requests
from simple_term_menu import TerminalMenu
from art import *
from tabulate import tabulate


url = 'http://localhost:8000/api/v1/app/csv-file/'

def get(url):
    r = requests.get(url)
    print(r.json())   
    data = r.json()
    print(data)


def post(url):
    files = {'csv_file': open('deals.csv', 'rb')}
    r = requests.post(url, files=files)
    print(r.json())

def main():
    print(text2art('CSVReader'))
    options = [
        "GET request to see data from DB", 
        "Upload the deals.csv file", 
        "Exit"
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        get(url)
    elif menu_entry_index == 1:
        post(url)
    else:
        raise SystemExit()

if __name__ == '__main__':
    main()
