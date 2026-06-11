# Netflix Exploratory Data Analysis (EDA)

## Project Overview

This project is part of the **CodeAlpha Data Analytics Internship (June 2026)**.

The objective of this project is to perform Exploratory Data Analysis (EDA) on the Netflix Titles dataset to discover meaningful patterns and trends through data cleaning, analysis, and visualization.

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

| Tool       | Purpose                   |
| ---------- | ------------------------- |
| Python 3.x | Core programming language |
| Pandas     | Data loading and analysis |
| Matplotlib | Data visualization        |
| NumPy      | Numerical computations    |

---

## How to Run

1. Clone this repository.
2. Install the required libraries:

```bash
pip install pandas matplotlib numpy
```

3. Place `netflix_titles.csv` in the project folder.
4. Run the script:

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

The project includes:

1. Movies vs TV Shows — Bar Chart
2. Top 10 Countries by Netflix Content — Bar Chart
3. Netflix Content by Release Year (2010–Present) — Line Chart
4. Top 10 Individual Genres — Bar Chart
5. Netflix Content Distribution — Pie Chart

---

## Key Insights

* Movies make up approximately **69.6% of Netflix's library**, making them nearly **2.3 times more common** than TV Shows.
* The **United States** contributes the highest amount of Netflix content, followed by **India** and the **United Kingdom**.
* Netflix content production increased significantly after **2015**, with major growth observed during **2018–2020**.
* International content and documentary-related categories are among the most prominent genres available on Netflix.
* Netflix hosts content from diverse regions around the world, reflecting its global expansion strategy.

---

## Conclusion

This Exploratory Data Analysis project demonstrates practical skills in:

* Data cleaning
* Handling missing values
* Exploratory data analysis
* Data visualization
* Extracting meaningful business insights

The analysis highlights Netflix's content distribution, growth trends, and international expansion through effective visual storytelling. This project showcases the application of Python and data analytics techniques to a real-world dataset.

---

## Project Outcomes

Through this project, the following objectives were achieved:

* Cleaned and prepared real-world data for analysis.
* Explored trends in Netflix's content library.
* Created professional visualizations for better understanding.
* Derived actionable insights from the dataset.
* Strengthened practical skills in Python, Pandas, and Matplotlib.

---

## Author

**Hiba Fathima**

CodeAlpha Data Analytics Intern — June 2026

GitHub: https://github.com/hibashafi2020-code
