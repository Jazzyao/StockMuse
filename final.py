#These are my import packages
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from dateutil import parser
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='darkgrid', palette='Set2')
import datetime
import pandas as pd
# import DataReader to get stock prices
from pandas_datareader.data import DataReader

Stocks= ""


# Generate a word cloud image
wordcloud2 = WordCloud(stopwords=stopwords2, background_color="white").generate(stopwords2)

# Display the generated image:
# the matplotlib way:
plt.figure(figsize=(7,7))
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.show()
