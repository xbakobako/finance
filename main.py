# 任意のファイルに記載して実行
import yfinance as yf
import matplotlib.pyplot as plt

# 例: 銘柄コード "MSFT" (Microsoft) の株価を表示
ticker_symbol = "MSFT"
start_date = "2022-01-01"
end_date = "2023-01-01"

# yfinance を使ってデータを取得
df = yf.download(ticker_symbol, start=start_date, end=end_date)

# グラフ表示
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], label="Close Price")
plt.title(f"{ticker_symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()