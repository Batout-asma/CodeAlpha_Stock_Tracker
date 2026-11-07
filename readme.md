# Stock Portfolio Tracker

A simple stock tracker made with Python.

You enter the stock names and the quantity you own, and the program calculates your total investment using a fixed list of prices. You can also save the result to a text file.

## Available stocks

| Stock | Price |
|-------|-------|
| AAPL  | $180  |
| TSLA  | $250  |
| GOOG  | $140  |
| MSFT  | $330  |

## How to run

1. Install Python 3
2. Download `stock_tracker.py`
3. Open a terminal in the folder and run:

```
python stock_tracker.py
```

## How to use

- Type a stock name (for example `AAPL`) and press Enter
- Type the quantity
- Repeat for as many stocks as you want
- Type `done` to finish
- The program shows each line and the total investment
- Type `y` to save the result in `portfolio.txt`

## Example

```
Stock name: AAPL
Quantity: 3
Stock name: TSLA
Quantity: 2
Stock name: done

AAPL x 3 = $540
TSLA x 2 = $500
Total investment: $1040
```

## Concepts used

dictionary, input/output, basic arithmetic, file handling

Made for the CodeAlpha Python Programming Internship.
