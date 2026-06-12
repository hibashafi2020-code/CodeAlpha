# Netflix Data Visualization

## Project Overview

This project was developed as part of the **CodeAlpha Data Analytics Internship (June 2026)**.

The objective of this project is to transform the Netflix Titles dataset into meaningful and visually appealing charts that communicate trends, patterns, and insights through effective data storytelling.

Unlike traditional Exploratory Data Analysis, this project focuses on creating professional visualizations that help understand Netflix's content library, growth, distribution, and content strategy.

---

## Dataset

**Source:** [Netflix Titles Dataset – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

The dataset contains information about Netflix movies and TV shows, including:

* Content type (Movie / TV Show)
* Country of origin
* Release year
* Date added to Netflix
* Content rating
* Genres
* Directors
* Duration
* Cast and descriptions

---

## Technologies Used

| Tool       | Purpose                             |
| ---------- | ----------------------------------- |
| Python 3.x | Programming Language                |
| Pandas     | Data manipulation and preprocessing |
| Matplotlib | Data visualization                  |
| Seaborn    | Heatmap visualization               |
| NumPy      | Numerical operations                |

---

## Data Preparation

The dataset was cleaned and prepared before visualization:

* Loaded the dataset using Pandas.
* Removed missing values where necessary.
* Split multi-genre entries using `.explode()` for accurate genre analysis.
* Converted movie durations into numerical values.
* Converted `date_added` into datetime format.
* Extracted month and year for time-series visualization.
* Applied a consistent Netflix-inspired color theme across all charts.

---

## Visualizations

### 1. Netflix Content Growth Over Years

A line chart showing the growth of Netflix's content library over time, including the peak release year.

### 2. Top 10 Countries by Netflix Content

A horizontal bar chart highlighting the countries contributing the highest number of Netflix titles.

### 3. Movies vs TV Shows by Release Year

A stacked bar chart comparing yearly movie and TV show releases.

### 4. Top 15 Individual Netflix Genres

A horizontal bar chart using `.explode()` to correctly analyse multi-genre content.

### 5. Netflix Content Rating Distribution

A donut chart showing the distribution of major Netflix content ratings.

### 6. Top 10 Directors on Netflix

A horizontal bar chart identifying directors with the highest number of Netflix titles.

### 7. Distribution of Netflix Movie Durations

A histogram visualizing the distribution of movie lengths.

### 8. Netflix Content Added by Month and Year

A heatmap illustrating Netflix's content addition trends across different months and years.

---

## Key Insights

* Netflix's content library grew significantly after 2015, peaking in **2018 with 1,145 titles**.
* Movies make up **69.6%** of Netflix content, nearly 2.3x more than TV Shows.
* The **United States** leads with **2,818 titles**, followed by India (972) and the UK (419).
* **International Movies (2,752)** and **Dramas (2,427)** are the top individual genres.
* **TV-MA** is the most common rating, covering **36.7%** of all content.
* Most Netflix movies fall between **80–120 minutes** in duration.
* **Rajiv Chilaka** leads with 19 Netflix titles among all directors.
* Netflix added the highest content volume during **2019–2020**, visible in the heatmap.


---

## Conclusion

This project demonstrates how effective data visualization can transform raw data into meaningful insights.

By combining multiple chart types, proper data preprocessing, and consistent visual styling, the analysis provides a comprehensive overview of Netflix's content trends and growth patterns while showcasing practical data analytics and visualization skills.

---

## Author

**Hiba Fathima**

CodeAlpha Data Analytics Intern — June 2026

GitHub: https://github.com/hibashafi2020-code

LinkedIn: *www.linkedin.com/in/
hiba-fathima-647790320
*
