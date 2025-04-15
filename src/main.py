import backtrader as bt
import pandas as pd
from strategy import SimpleStrategy
from telegram import send_telegram_message

TG_TOKEN = "7868623358:AAHrGBKlcp_Wcs2vpbC44YMVWHgowCNlykA"
TG_CHAT_ID = "6384032796"

# CSV 파일 불러오기 (예시: 15분봉 기준 바이낸스)
df = pd.read_csv("data/BTC_USDT_15m.csv")
df["datetime"] = pd.to_datetime(df["open_time"])
df.set_index("datetime", inplace=True)

data = bt.feeds.PandasData(dataname=df)

cerebro = bt.Cerebro()
cerebro.addstrategy(SimpleStrategy)
cerebro.adddata(data)
cerebro.broker.set_cash(10000)

# 전략 실행
results = cerebro.run()

if results:
    final_value = cerebro.broker.getvalue()
    profit = final_value - 10000
    percent = (profit / 10000) * 100

    message = f"[단순 전략 백테스트 결과]\nBTC/USDT: ${final_value:.2f} / {percent:.2f}%"
else:
    message = "[단순 전략 백테스트 결과]\n전략 실행 결과 없음 (조건 불충족)"

# 텔레그램 전송
send_telegram_message(TG_TOKEN, TG_CHAT_ID, message)
