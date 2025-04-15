from strategy import SimpleStrategy
from telegram import send_telegram_message
import backtrader as bt
import pandas as pd

TG_TOKEN = "7868623358:AAHrGBKlcp_Wcs2vpbC44YMVWHgowCNlykA"
TG_CHAT_ID = "6384032796"

df = pd.read_csv("btc_5m_180d.csv")
df["datetime"] = pd.to_datetime(df["datetime"])
df.set_index("datetime", inplace=True)
data = bt.feeds.PandasData(dataname=df)

cerebro = bt.Cerebro()
cerebro.addstrategy(SimpleStrategy)
cerebro.adddata(data)
cerebro.broker.setcash(10000)
cerebro.broker.setcommission(commission=0.001)

result = cerebro.run()
final_value = cerebro.broker.getvalue()
message = f"[단순 전략 백테스트 결과]\nBTC/USDT: ${final_value:.2f}"
send_telegram_message(TG_TOKEN, TG_CHAT_ID, message)
