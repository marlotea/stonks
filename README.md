# STONKS: Stock Trade Recommendation Program

## Overview

The **Stock Trade Recommendation Program** is a Python-based application designed to analyze historical stock data, apply trading strategies, and generate buy/sell recommendations. This program utilizes the Alpha Vantage API to fetch stock price data and implements a simple moving average (SMA) strategy for decision-making.

## Features

- Fetches daily stock price data from Alpha Vantage.
- Applies a simple moving average strategy to generate buy/sell signals.
- Generates user-friendly trade recommendations.
- Backtests the trading strategy to evaluate performance.
- Saves recommendations to a CSV file for further analysis.

## Prerequisites

Before running the program, ensure you have the following:

- Python 3.x installed on your machine.
- An API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/marlotea/stonks.git
   cd stonks

2. Install the required packages:

    ```bash
    pip install -r requirements.txt

3. Set up your Alpha Vantage API key:

    - Create a file named config.py in the root directory of the project.
    - Add your API key to config.py:
    ```python
    API_KEY = 'your_alpha_vantage_api_key_here'


## Usage

To run the program, use the following command in your terminal:

    ```bash
    python main.py
    ```

## Code Structure

The project is organized as follows:
```bash
stock-trade-recommendation/
│
├── api/
│   └── alpha_vantage_api.py        # Module to fetch stock data from Alpha Vantage
│
├── strategies/
│   └── sma_strategy.py              # Module containing the SMA trading strategy
│
├── recommendations/
│   └── recommendation_engine.py      # Module to generate trade recommendations
│
├── backtesting/
│   └── backtest.py                  # Module for backtesting trading strategies
│
├── utils/
│   └── data_handler.py              # Utility functions for data handling (e.g., saving to CSV)
│
├── config.py                        # Configuration file to store API key
│
├── main.py                          # Main script to run the application
│
└── requirements.txt                 # List of required Python packages
```

## Acknowledgements

Alpha Vantage for providing the stock data API.
Python for being a versatile programming language.


## Contact
For any questions or inquiries, please contact:

Leia Chen - leiahjchen@gmail.com




