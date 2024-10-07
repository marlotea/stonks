def calculate_sma(data, window_size):
    """
    Calculate the Simple Moving Average (SMA) over the given window size
    
    Args:
        data (list): List of data retrieved from API
        window_size (int): window size
        
    Returns:
        list: List of SMA values
    """
    sma = []
    for i in range(len(data)):
        if i >= window_size:
            sma.append(sum(data[i-window_size:i]) / window_size)
        else:
            sma.append(None)  # Not enough data to calculate SMA
    return sma

def sma_strategy(data, short_window=50, long_window=200):
    """
    Produces signals using SMA values
    
    Args:
        data (list): list of stock data retrieved from API
        short_window (int) default 50: short window
        long_window (int) default 200: long window
        
    Returns:
        list: List of signals ['Buy', 'Sell', 'Hold']
    """
    short_ma = calculate_sma(data, short_window)
    long_ma = calculate_sma(data, long_window)
    signals = []
    for i in range(len(data)):
        if short_ma[i] and long_ma[i]:
            if short_ma[i] > long_ma[i]:
                signals.append('Buy')
            elif short_ma[i] < long_ma[i]:
                signals.append('Sell')
            else:
                signals.append('Hold')
    return signals