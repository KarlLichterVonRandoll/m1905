"""
    净额成交量 obv
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
import datetime as dt


def dmy2ymd(dmy):
    # 把日月年字符串转为年月日字符串
    dmy = str(dmy, encoding='utf-8')
    d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = d.strftime('%Y-%m-%d')
    return ymd


dates, closing_prices, volumes = np.loadtxt(
    'aapl.csv', delimiter=',',
    usecols=(1, 6, 7), unpack=True,
    dtype='M8[D], f8, f8', converters={1: dmy2ymd})

# 绘制 obv 柱状图
diff_closing_price = np.diff(closing_prices)
sign_closing_price = np.sign(diff_closing_price)

obvs = volumes[1:] * sign_closing_price

mp.figure('On-Balance Volume', facecolor='lightgray')
mp.title('On-Balance Volume', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('OBV', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
dates = dates[1:].astype(md.datetime.datetime)
mp.bar(dates, obvs, 1.0, color='dodgerblue',
       edgecolor='white', label='OBV')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()

