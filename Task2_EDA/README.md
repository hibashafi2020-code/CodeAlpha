# Netflix Exploratory Data Analysis (EDA)

## Project Overview

This project is part of the **CodeAlpha Data Analytics Internship (June 2026)**.

The objective of this project is to perform Exploratory Data Analysis (EDA) on the Netflix Titles dataset to uncover meaningful trends through data cleaning, analysis, and visualization.

---

## Dataset

**Source:** [Netflix Titles Dataset – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

The dataset contains information about Netflix movies and TV shows, including:

* Type of content (Movie / TV Show)
* Country of origin
* Release year
* Content rating
* Genres
* Cast and directors

---

## Technologies Used

| Tool       | Purpose                              |
| ---------- | ------------------------------------ |
| Python 3.x | Core programming language            |
| Pandas     | Data loading, cleaning, and analysis |
| Matplotlib | Data visualization                   |
| NumPy      | Numerical computations               |

---

## How to Run

1. Clone this repository.

2. Install the required libraries:

```bash
pip install pandas matplotlib numpy
```

3. Place `netflix_titles.csv` in the project folder.

4. Run the Python script:

```bash
python netflix_eda.py
```

---

## Data Preprocessing

The following preprocessing steps were performed:

* Loaded the dataset using Pandas.
* Identified and handled missing values in the `country` and `rating` columns.
* Cleaned the dataset for better analysis.
* Split the multi-label `listed_in` column into individual genres using `.explode()` for accurate genre analysis.

---

## Visualizations

The project includes the following visualizations:

1. Movies vs TV Shows — Bar Chart
2. Top 10 Countries by Netflix Content — Bar Chart
3. Netflix Content by Release Year (2010–Present) — Line Chart
4. Top 10 Individual Genres — Bar Chart
5. Netflix Content Distribution — Pie Chart

---

## Key Insights

* Movies make up approximately **69.6% of Netflix's library**, making them nearly **2.3 times more common** than TV Shows.
* The **United States** contributes the highest amount of Netflix content, followed by **India** and the **United Kingdom**.
*
