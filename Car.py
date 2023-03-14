import yfinance as yf

# Ustaw nazwy firm, których wartości akcji chcesz odczytać
companies = ['AAPL', 'MSFT', 'AMZN']

# Pobierz dane dla firm z podanymi nazwami
data = yf.download(companies, start='2021-01-01', end='2023-02-16')

# Wyświetl ceny zamknięcia akcji dla każdej firmy
print(data['Close'])
