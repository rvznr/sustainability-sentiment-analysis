import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

df = pd.read_csv("reddit_posts.csv")

sentiment_counts = df["Sentiment"].value_counts()

sns.set_style("whitegrid")
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})

plt.figure(figsize=(9, 6))
colors = ["#2ecc71", "#95a5a6", "#e74c3c"]
ax = sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=colors)

total = sum(sentiment_counts.values)
for i, value in enumerate(sentiment_counts.values):
    percentage = f"{(value / total) * 100:.1f}%"
    ax.text(i, value + 5, f"{value} ({percentage})", ha="center", fontsize=12, fontweight="bold")

plt.xlabel("Sentiment", fontsize=14, fontweight="bold")
plt.ylabel("Number of Posts", fontsize=14, fontweight="bold")
plt.title("Reddit Sentiment Analysis: Sustainability", fontsize=16, fontweight="bold")
plt.ylim(0, max(sentiment_counts.values) * 1.1)
plt.show()

plt.figure(figsize=(7, 7))
explode = (0.05, 0.05, 0.05)
df["Sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    explode=explode,
    wedgeprops={"edgecolor": "black", "linewidth": 1.2},
    textprops={"fontsize": 12, "weight": "bold"}
)

plt.title("Sentiment Distribution on Reddit", fontsize=16, fontweight="bold")
plt.ylabel("")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
sentiment_trend = df.groupby(df["Date"].dt.date)["Sentiment"].value_counts().unstack()
sentiment_trend.plot(kind="line", figsize=(10, 5), marker="o")
plt.title("Sentiment Trends Over Time")
plt.ylabel("Number of Posts")
plt.show()

positive_words = " ".join(df[df["Sentiment"] == "Positive"]["Title"])
negative_words = " ".join(df[df["Sentiment"] == "Negative"]["Title"])

plt.figure(figsize=(10, 5))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(positive_words)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Positive Posts")
plt.show()

plt.figure(figsize=(10, 5))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(negative_words)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Negative Posts")
plt.show()

df.groupby("Sentiment")["Upvotes"].mean().plot(kind="bar", color=["#2ecc71", "#95a5a6", "#e74c3c"])
plt.title("Average Upvotes by Sentiment")
plt.ylabel("Average Upvotes")
plt.show()