// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © ImM4nd4R

//@version=5
strategy("FibCrossOver", overlay=true)

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © ImM4nd4R

//@version=5
//indicator("Fib Crossover",overlay=true)

ema8 = ta.ema(close,8)
ema13 = ta.ema(close,13)
ema21 = ta.ema(close,21)
ema34 = ta.ema(close,34)
plot(ema8,title="ema8",color=color.green)
plot(ema13,title="ema13",color=color.black)
plot(ema21, title="ema21",color=color.orange)
plot(ema34, title="ema34",color=color.purple)


long = ta.crossover(ema13, ema21) and (ema21 > 0.95 * ema34) and (ema8 > ema13)
short = ta.crossunder(ema13,ema21)

plotshape(long, color = color.blue)

start = timestamp(2010,01,01,0,0)

if time >= start
    strategy.entry("LE", strategy.long, 10, when = long)
    strategy.close("LE", when = short)
