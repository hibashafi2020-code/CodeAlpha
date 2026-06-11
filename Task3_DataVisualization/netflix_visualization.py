import pandas as pd
import matplotlib.pyplot as plt

# Netflix color theme
NETFLIX_RED = '#E50914'
DARK = '#221F1F'
GRAY = '#B0B0B0'

# Load dataset
data = pd.read_csv("netflix_titles.csv")

# Convert release years into counts
year_counts = data['release_year'].value_counts().sort_index()
year_counts = year_counts[year_counts.index >= 1990]

# Plot Graph 1
plt.figure(figsize=(12,6))

plt.plot(
    year_counts.index,
    year_counts.values,
    color=NETFLIX_RED,
    linewidth=3
)

plt.fill_between(
    year_counts.index,
    year_counts.values,
    color=NETFLIX_RED,
    alpha=0.2
)

plt.title("Netflix Content Growth Over Years",
          fontsize=16,
          fontweight='bold')

plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(axis='y', linestyle='--', alpha=0.5)

peak_year = year_counts.idxmax()
peak_val = year_counts.max()

plt.annotate(
    f'Peak: {peak_year}',
    xy=(peak_year, peak_val),
    xytext=(peak_year - 6, peak_val - 150),
    arrowprops=dict(arrowstyle='->', color='black'),
    fontsize=10,
    fontweight='bold'
)

plt.tight_layout()
plt.show()

# ── Graph 2: Top 10 Countries ─────────────────────────────

fig, ax = plt.subplots(figsize=(12,6))

top_countries = data['country'].dropna().value_counts().head(10)

bars = ax.barh(
    top_countries.index[::-1],
    top_countries.values[::-1],
    color='#E50914',
    edgecolor='black'
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 20,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va='center',
        fontsize=10,
        fontweight='bold'
    )

ax.set_title(
    "Top 10 Countries by Netflix Content",
    fontsize=16,
    fontweight='bold'
)

ax.set_xlabel(
    "Number of Titles",
    fontsize=12
)

ax.set_ylabel(
    "Country",
    fontsize=12
)

ax.grid(axis='x', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# ── Graph 3: Movies vs TV Shows by Year ─────────────────────

data['release_year'] = data['release_year'].astype(int)

content_year = data.groupby(
    ['release_year', 'type']
).size().unstack(fill_value=0)

content_year = content_year[content_year.index >= 2000]

fig, ax = plt.subplots(figsize=(14,6))

content_year.plot(
    kind='bar',
    stacked=True,
    color=['#E50914', '#221F1F'],
    ax=ax
)

ax.set_title(
    "Movies vs TV Shows by Release Year",
    fontsize=16,
    fontweight='bold'
)

ax.set_xlabel(
    "Release Year",
    fontsize=12
)

ax.set_ylabel(
    "Number of Titles",
    fontsize=12
)

plt.xticks(rotation=45, ha='right', fontsize=8)
plt.legend(title="Content Type")
plt.tight_layout()
plt.show()

# ── Graph 4: Top 15 Individual Genres ─────────────────────

fig, ax = plt.subplots(figsize=(12,6))

genres = data['listed_in'].str.split(', ').explode()

top_genres = genres.value_counts().head(15)

bars = ax.barh(
    top_genres.index[::-1],
    top_genres.values[::-1],
    color='#E50914',
    edgecolor='black'
)

for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 20,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va='center',
        fontsize=9,
        fontweight='bold'
    )

ax.set_title(
    "Top 15 Individual Netflix Genres",
    fontsize=16,
    fontweight='bold'
)

ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")

ax.grid(axis='x', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# ── Graph 5: Content Rating Distribution ───────────────────

fig, ax = plt.subplots(figsize=(8,8))

ratings = data['rating'].dropna().value_counts().head(10)

colors = plt.cm.Reds(range(50, 50+20*len(ratings), 20))

wedges, texts, autotexts = ax.pie(
    ratings.values,
    labels=ratings.index,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.8,
    colors=colors
)

# Create donut hole
centre_circle = plt.Circle((0,0),0.55,fc='white')
fig.gca().add_artist(centre_circle)

ax.set_title(
    "Top Netflix Content Ratings",
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout()
plt.show()

# ── Graph 6: Top 10 Directors ───────────────────────────

fig, ax = plt.subplots(figsize=(12,6))

# Remove missing values
directors = data['director'].dropna()

# Count top directors
top_directors = directors.value_counts().head(10)

# Horizontal bar chart
bars = ax.barh(
    top_directors.index[::-1],
    top_directors.values[::-1],
    color='#E50914',
    edgecolor='black'
)

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.1,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va='center',
        fontsize=10,
        fontweight='bold'
    )

# Titles and labels
ax.set_title(
    "Top 10 Directors on Netflix",
    fontsize=16,
    fontweight='bold'
)

ax.set_xlabel(
    "Number of Titles",
    fontsize=12
)

ax.set_ylabel(
    "Director",
    fontsize=12
)

# Grid
ax.grid(axis='x', linestyle='--', alpha=0.4)
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

plt.tight_layout()
plt.show()

# ── Graph 7: Movie Duration Distribution ─────────────────

fig, ax = plt.subplots(figsize=(12,6))

# Select movies only
movies = data[data['type'] == 'Movie'].copy()

# Extract duration in minutes
movies['duration_int'] = movies['duration'].str.extract(r'(\d+)').astype(float)

# Plot histogram
ax.hist(
    movies['duration_int'].dropna(),
    bins=20,
    color='#E50914',
    edgecolor='black'
)

ax.set_title(
    "Distribution of Netflix Movie Durations",
    fontsize=16,
    fontweight='bold'
)

ax.set_xlabel(
    "Duration (Minutes)",
    fontsize=12
)

ax.set_ylabel(
    "Number of Movies",
    fontsize=12
)

ax.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()

# ── Graph 8: Netflix Content Added by Month & Year (Heatmap) ─────────

import seaborn as sns

# Convert date_added to datetime
data['date_added'] = pd.to_datetime(
    data['date_added'].str.strip(),
    errors='coerce'
)

# Extract month and year
data['month_added'] = data['date_added'].dt.month
data['year_added'] = data['date_added'].dt.year

# Create pivot table
heatmap_data = data.pivot_table(
    index='year_added',
    columns='month_added',
    aggfunc='size',
    fill_value=0
)

# Month names
month_names = [
    'Jan','Feb','Mar','Apr',
    'May','Jun','Jul','Aug',
    'Sep','Oct','Nov','Dec'
]

plt.figure(figsize=(14,7))

sns.heatmap(
    heatmap_data,
    cmap='Reds',
    linewidths=0.5,
    linecolor='white',
    cbar_kws={'label':'Number of Titles'}
)

plt.title(
    "Netflix Content Added by Month and Year",
    fontsize=16,
    fontweight='bold'
)

plt.xlabel("Month")
plt.ylabel("Year")

plt.xticks(
    ticks=[x + 0.5 for x in range(12)],
    labels=month_names,
    rotation=0
)

plt.tight_layout()
plt.show()
