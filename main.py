import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("netflix_titles.csv")

data_type = data["type"].value_counts()
sns.set_style("whitegrid")
plt.pie(data_type,labels = data_type.index,startangle = 60,autopct = "%.1f%%",wedgeprops={'linewidth': 1},)
plt.title("Netflix Movie and TV Show Ratio")

data_listed = data["listed_in"].value_counts().head(15)
print(f"Top 15 Categories: {data_listed} ")

plt.figure(figsize=(3,5))
data_listed.plot(kind = "barh",color = "blue")
plt.title("Top 15 Genres")

data = data.dropna(subset=["country","type"])
data["country"] = data["country"].str.split(",")
data = data.explode("country")
data["country"] = data["country"].str.strip()
top_countries = data["country"].value_counts().head(10)
print(f"Top 10 Countries: {top_countries}")

data_top = data[data["country"].isin(top_countries.index)]
country_type = data_top.groupby(["country","type"]).size().reset_index(name = "count")
print(country_type)

plt.figure(figsize=(7,5))
sns.barplot(data = country_type, x = "country", y = "count", hue = "type",palette = "dark:orange")
plt.title("Top 10 Countries by Netflix Content Type")
plt.xlabel("Country")
plt.ylabel("Count")
plt.legend(title = "Type")
plt.show()

drop_rating = data.dropna(subset=["rating"])
plt.figure(figsize=(10,5))
sns.countplot(data = drop_rating, x = "rating", order=data["rating"].value_counts().index,color = "orange")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.show()

drop_director = data["director"].dropna()
top_director = drop_director.value_counts().head(10)
print(f"Top 10 Directors: {top_director} ")
plt.figure(figsize =(10,5))
top_director.plot(kind = "bar",color = "orange")
plt.title("Top 10 Directors")
plt.xlabel("Directors")
plt.xticks(rotation = 25)
plt.show()







