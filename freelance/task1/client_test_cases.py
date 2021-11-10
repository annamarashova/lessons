"""
В этом файле содержатся тестовые данные, которые прислал клиент в качестве примеров.

SOURCE_TEXT_i -- пример текста сообщения в исходном формате из source channel
DESTINATION_TEXT_i -- текст сообщения в формате destination channel, который мы должны создать
"""

# ==== Пример сообщения 1 ====

SOURCE_TEXT_1 = """
Capital.com DeFi Signal

Synthetix (SNXUSD) Trade Signal (INTRA DAY)

Instrument: SNX/USD
My opinion: Buy Stop
Entry price: $11.25
Stop: $10.85
Target: $12.04
Our risk setting: 1%
RRR: 1:2

NB: We will close this pending trade if not triggered within 10 hours.

In order to place this trade with Capital.com you can open an account here: https://go.currency.com/visit/?bta=35304&nci=5721&utm_campaign=cryptosignals&afp=defisignals
"""

DESTINATION_TEXT_1 = """
🔥 SNXUSD - BUY STOP $11.25

🟢 TP $12.04
❌ SL $10.85

👉 close if not triggered within 10 hours
"""

# ================

# ==== Пример сообщения 2 ====

SOURCE_TEXT_2 = """
Bitcoin Trade Signal (Swing Trade)

Instrument: BTC/USD
My opinion: Buy Limit
Entry price: $65000
Stop: $63500
Target: $68000
My risk setting: 0.5%
RRR: 1:2

NB: I will close this pending trade if not triggered within 8 hours.
"""

DESTINATION_TEXT_2 = """
🔥 BTCUSD - BUY LIMIT $65000

🟢 TP $68000
❌ SL $63500

👉 close if not triggered within 8 hours
"""

# ================

# ==== Пример сообщения 3 ====

SOURCE_TEXT_3 = """
Capital.com DeFi Signal

0x (ZRXUSD) Trade Signal (INTRA DAY)

Instrument: ZRX/USD
My opinion: Buy (Instant Execution)
Entry price: $1.39
Stop: $1.27
Target: $1.63
Our risk setting: 1%
RRR: 1:2

In order to place this trade with Capital.com you can open an account here: https://go.currency.com/visit/? bta=35304&nci=5721&utm_campaign=cryptosignals&afp=defisignals
"""

DESTINATION_TEXT_3 = """
🔥 ZRXUSD - BUY $1.39

🟢 TP $1.63
❌ SL $1.27
"""

# ================

# ==== Пример сообщения 4 ====

SOURCE_TEXT_4 = """
Solana Trade Signal (Swing Trade)

Instrument: SOL/USD
My opinion: Buy (Market Execution)
Entry price: $230
Stop: $215
Target: $260
My risk setting: 1%
RRR: 1:2

NB: We will close this pending trade if not triggered within 8 hours.
"""

DESTINATION_TEXT_4 = """
🔥 SOLUSD - BUY $230

🟢 TP $260
❌ SL $215

👉 close if not triggered within 8 hours
"""
