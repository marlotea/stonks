# calculates the simple moving average
def calculate_sma(data, window_size):
    sma = []
    for i in range(len(data)):
        if i >= window_size:
            sma.append(sum(data[i-window_size:i]) / window_size)
        else:
            sma.append(None)  # Not enough data to calculate SMA
    return sma

# returns list of signals ['Buy', 'Sell', 'Hold']
def sma_strategy(data, short_window=50, long_window=200):
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