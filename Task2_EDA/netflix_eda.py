import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("netflix_titles.csv")
data_clean = data.dropna(subset=['country', 'rating'])

# ── Graph 1: Movies vs TV Shows ──────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
type_counts = data['type'].value_counts()
bars = ax.bar(type_counts.index, type_counts.values,
              color=['#E50914', '#221F1F'], width=0.4, edgecolor='black')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 50,
            str(int(bar.get_height())),
            ha='center', fontsize=11, fontweight='bold')

ax.set_title("Movies vs TV Shows on Netflix", fontsize=14, fontweight='bold')
ax.set_xlabel("Type", fontsize=12)
ax.set_ylabel("Number of Titles", fontsize=12)
ax.set_ylim(0, type_counts.max() + 500)
plt.tight_layout()
plt.show()

# ── Graph 2: Top 10 Countries ────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))
top_countries = data_clean['country'].value_counts().head(10)
colors = ['#E50914' if i == 0 else '#B0B0B0' for i in range(len(top_countries))]
bars = ax.bar(top_countries.index, top_countries.values,
              color=colors, edgecolor='black')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 10,
            str(int(bar.get_height())),
            ha='center', fontsize=9)

ax.set_title("Top 10 Countries by Netflix Content", fontsize=14, fontweight='bold')
ax.set_xlabel("Country", fontsize=12)
ax.set_ylabel("Number of Titles", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ── Graph 3: Content Added Per Year (Chronological) ──────────
fig, ax = plt.subplots(figsize=(12, 5))
year_counts = data['release_year'].value_counts().sort_index()
year_counts = year_counts[year_counts.index >= 2010]  # Focus on recent years

ax.plot(year_counts.index, year_counts.values,
        color='#E50914', linewidth=2.5, marker='o', markersize=5)
ax.fill_between(year_counts.index, year_counts.values, alpha=0.15, color='#E50914')

ax.set_title("Netflix Content by Release Year (2010–Present)",
             fontsize=14, fontweight='bold')
ax.set_xlabel("Release Year", fontsize=12)
ax.set_ylabel("Number of Titles", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# ── Graph 4: Top 10 Genres (Fixed with explode) ───────────────
fig, ax = plt.subplots(figsize=(12, 5))
genres = data['listed_in'].str.split(', ').explode()
top_genres = genres.value_counts().head(10)
colors_g = ['#E50914' if i == 0 else '#4A90D9' for i in range(len(top_genres))]
bars = ax.bar(top_genres.index, top_genres.values,
              color=colors_g, edgecolor='black')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 10,
            str(int(bar.get_height())),
            ha='center', fontsize=9)

ax.set_title("Top 10 Individual Genres on Netflix", fontsize=14, fontweight='bold')
ax.set_xlabel("Genre", fontsize=12)
ax.set_ylabel("Number of Titles", fontsize=12)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.show()

# ── Graph 5: Pie Chart (Improved) ────────────────────────────
fig, ax = plt.subplots(figsize=(7, 7))
type_counts = data['type'].value_counts()
ax.pie(type_counts.values,
       labels=type_counts.index,
       autopct='%1.1f%%',
       colors=['#E50914', '#F5A623'],
       startangle=90,
       explode=(0.05, 0),
       wedgeprops={'edgecolor': 'white', 'linewidth': 2})

ax.set_title("Netflix Content Distribution", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()