import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Movie Name": [
        "Inception", "Avengers", "Interstellar",
        "Titanic", "Joker", "Bahubali",
        "Dangal", "KGF", "Pushpa", "3 Idiots"
    ],

    "Rating": [8.8, 8.0, 8.6, 7.9, 8.4, 8.2, 8.5, 8.3, 7.8, 8.4],

    "Genre": [
        "Sci-Fi", "Action", "Sci-Fi",
        "Romance", "Thriller", "Action",
        "Sports", "Action", "Action", "Comedy"
    ],

    "Revenue": [
        830, 2797, 701,
        2187, 1074, 650,
        300, 250, 350, 400
    ]
}

df = pd.DataFrame(data)
print("Movie Dataset:\n")
print(df)

print("\nHighest Rated Movies:\n")
highest_rated = df.sort_values(by="Rating", ascending=False)
print(highest_rated[["Movie Name", "Rating"]])
print("\nMost Profitable Genres:\n")
genre_revenue = df.groupby("Genre")["Revenue"].sum()
print(genre_revenue)

print("\nTop 5 Movies Based on Rating:\n")
top5 = df.sort_values(by="Rating", ascending=False).head(5)
print(top5[["Movie Name", "Rating"]])

correlation = df["Rating"].corr(df["Revenue"])
print("\nCorrelation between Rating and Revenue:")
print(correlation)

plt.figure(figsize=(8,5))
genre_revenue.plot(kind='bar')
plt.title("Genre vs Revenue")
plt.xlabel("Genre")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Rating"], bins=5)
plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.show()
