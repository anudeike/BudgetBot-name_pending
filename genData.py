import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(7)


def generatePrices(n, vol=0.06, init_price=10):
    prices = [init_price]
    for x in range(1,n):
        rnd = np.random.rand()
        vol = 0.02
        old_price = prices[x-1]
        change_percent = 2 * vol * rnd
        if (change_percent > vol):
            change_percent -= (2 * vol)
        change_amount = old_price * change_percent
        prices.append(old_price + change_amount)

    return prices


    # rnd = np.random.rand()  # generate number, 0 <= x < 1.0
    # volatility = 0.06
    # old_price = 50
    # change_percent = 2 * volatility * rnd
    # if (change_percent > volatility):
    #     change_percent -= (2 * volatility)
    # change_amount = old_price * change_percent
    # new_price = old_price + change_amount

#plot data
def plotData(data):
    y = [x for x in range(len(data))]
    plt.scatter(y, data)

#plot the data in seaborn
def snsScatterPlot(df):
    sns.scatterplot(df["time in days"], df["Amount Spent"]).plot()


def snsRegPlot(df, lab, color='blue'):
    sns.regplot(df["time in days"], df["Amount Spent"], color, label=lab).plot()


stock_prices = generatePrices(100)
#plotData(stock_prices)

#turn into a dataframe
df = pd.DataFrame(data=stock_prices, columns=["Amount Spent"])
df["time in days"] = [x for x in range(100)]
print(df)
#snsScatterPlot(df)
plt.title("Historical Purchases Summary")
snsRegPlot(df, 'Transportation', color='blue')

#=====GENERATE OTHER TYPE============#
# # Entertainment
ent_cost = generatePrices(100)
plotData(ent_cost)
df = pd.DataFrame(data=ent_cost, columns=["Amount Spent"])
df["time in days"] = [x for x in range(100)]
snsRegPlot(df, 'Entertainment', color='orange')

# Entertainment
gro_cost = generatePrices(100)
plotData(gro_cost)
df = pd.DataFrame(data=gro_cost, columns=["Amount Spent"])
df["time in days"] = [x for x in range(100)]
snsRegPlot(df, 'Groceries', color='red')

#
util_cost = generatePrices(100)
plotData(util_cost)
df = pd.DataFrame(data=util_cost, columns=["Amount Spent"])
df["time in days"] = [x for x in range(100)]
snsRegPlot(df, 'Utilities', color='purple')

#add the legend and descriptions
plt.legend(loc='upper left')

plt.show()