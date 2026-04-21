# 📌 Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 📌 Load dataset
df = pd.read_csv("netflix_titles.csv")

# 📌 Show first 5 rows
print("\nFirst 5 rows:\n", df.head())

# 📌 Dataset info
print("\nDataset Info:\n")
df.info()

# 📌 Missing values
print("\nMissing Values:\n", df.isnull().sum())

# 📌 Data Cleaning
df.fillna("Unknown", inplace=True)

# -------------------------------
# 📊 1. Movies vs TV Shows
plt.figure()
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# -------------------------------
# 📊 2. Top 10 Genres
genres = df['listed_in'].str.split(',', expand=True).stack()
plt.figure()
genres.value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.savefig("top_genres.png")
plt.show()

# -------------------------------
# 📊 3. Top 10 Countries
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries Producing Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("top_countries.png")
plt.show()

# -------------------------------
# 📊 4. Content Growth Over Years
plt.figure()
df['release_year'].value_counts().sort_index().plot()
plt.title("Content Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("content_growth.png")
plt.show()

# -------------------------------
# 📊 5. Ratings Distribution
plt.figure()
df['rating'].value_counts().head(10).plot(kind='bar')
plt.title("Top Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("ratings.png")
plt.show()

print("\n✅ Analysis Complete! All graphs saved as images.")