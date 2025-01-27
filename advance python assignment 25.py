#!/usr/bin/env python
# coding: utf-8
Q1. What is the distinction between a numpy array and a pandas data frame? Is there a way to convert between the two if there is ?

Ans: Numpy Ndarray provides a lot of convenient and optimized methods for performing several mathematical operations on vectors.

Pandas Dataframe is an in-memory 2-dimensional tabular representation of data. In simpler words, it can be seen as a spreadsheet having rows and columns.

Conversion : Dataframe=pandas.DataFrame(array)



Q2. Identify some of the plotting techniques that are used to produce a stock-market chart ?

Ans: Bar chart, Line Chart, Candlestick chart (using mplfinance module) are used for plotting stock market chart.



Q3. Why is it essential to print a legend on a stock market chart ?

Ans: Legend will help us in comparing different stocks in a stock market chart. Each plot of a Stock chart has a legend, its items representing the series on the plot. In addition, the legend displays information about the points that are currently hovered over or, if none are hovered over, about the last points shown on the plot. The text of a legend item includes the name of a series and, depending on the series type, the value or values of the current or last point. The legend title, enabled by default, shows the current or last date (X-value).


Q4. What is the best way to limit the length of a pandas data frame to less than a year ?

Ans: : We can use start and end parameters for that. In start, we write the date from where we are starting and at the end, we write the end date. SO within this span we can restrict the duration. Also, we can use the parameters like periods i.e for how much times we need the duration and we can also use the frequency parameter for that.


Q5. What is the definition of a 180-day moving average ?

Ans: : The 180-day moving average is represented as a line on charts and represents the average price over the past 180 days. The moving average can give traders a sense regarding whether the trend is up or down, while also identifying potential support or resistance areas. A moving average (MA) is a stock indicator that is commonly used in technical analysis. The reason for calculating the moving average of a stock is to help smooth out the price data over a specified period of time by creating a constantly updated average price. A simple moving average (SMA) is a calculation that takes the arithmetic mean of a given set of prices over the specific number of days in the past; for example, in this case over 180 days.
# In[ ]:




