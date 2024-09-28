import webbrowser

def open_url(country: str):
    in_capital = country.title()
    url = f'https://en.wikipedia.org/wiki/{in_capital}#/media/File:Flag_of_{in_capital}.svg'
    webbrowser.open(url)

country = input("Enter the country: ")
open_url(country)
