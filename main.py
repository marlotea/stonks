from api.alpha_vantage_api import fetch_stock_data
from strategies.sma_strategy import sma_strategy
from utils.data_handler import save_data_to_csv
from config import API_KEY


def main():
    
    # Fetch stock data\
    symbols = ['AAPL', 'NVDA', 'AMZN', 'MSFT', 'TSLA', 'META', 'AMD']
    
    for symbol in symbols:
    
        print(f"Fetching data for {symbol}...")
        stock_data = fetch_stock_data(symbol, API_KEY)
    
        # Extract the closing prices for analysis
        closing_prices = [float(data['4. close']) for date, data in stock_data.items()]
    
        # Run the trading strategy
        print("Applying trading strategy...")
        signals = sma_strategy(closing_prices)
    
    
if __name__ == "__main__":
    main()
