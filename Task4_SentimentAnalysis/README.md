# 🎬 IMDB Movie Reviews — Sentiment Analysis

## 📌 Project Overview
This project performs sentiment analysis on IMDB movie reviews using 
Natural Language Processing (NLP). The goal is to classify reviews as 
Positive, Negative, or Neutral and extract meaningful patterns through 
data visualization.

This project was completed as part of the **CodeAlpha Data Analytics Internship (June 2026)**.

---

## 📂 Dataset
**Source:** [IMDB Dataset of 50K Movie Reviews – Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

| Property | Details |
|----------|---------|
| Total Reviews | 50,000 |
| Positive Reviews | 25,000 |
| Negative Reviews | 25,000 |
| Missing Values | None |
| Balance | Perfectly balanced dataset |

---

## 🛠 Technologies Used
| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Pandas | Data loading and manipulation |
| NLTK (VADER) | Sentiment scoring |
| Matplotlib | Data visualization |
| WordCloud | Word frequency visualization |
| Re (Regex) | Text cleaning |

---

## 🔄 Project Workflow

**Step 1 — Load & Explore**
Load the dataset and examine structure, shape, and class distribution.

**Step 2 — Clean Text**
- Remove HTML tags (e.g. `<br />`)
- Remove punctuation and numbers
- Convert all text to lowercase

**Step 3 — Apply VADER**
Calculate compound sentiment score for each review using NLTK's VADER analyzer.

**Step 4 — Classify Sentiment**
- Positive → score ≥ 0.05
- Negative → score ≤ −0.05
- Neutral → score between −0.05 and 0.05

**Step 5 — Visualize**
Generate bar chart, donut chart, and word clouds.

**Step 6 — Evaluate**
Compare VADER predictions against actual IMDB labels using a crosstab matrix.

---

## 📊 Visualizations

1. **VADER Sentiment Distribution** — Bar chart of review counts per class
2. **VADER Sentiment Breakdown** — Donut chart of percentage distribution
3. **Positive Review Word Cloud** — Most frequent words in positive reviews
4. **Negative Review Word Cloud** — Most frequent words in negative reviews

---

## 📈 Key Insights
- VADER classified **65.1%** of reviews as Positive, **33.8%** as Negative,
  and only **1.1%** as Neutral
- **VADER Accuracy: 68.97%** when compared against actual dataset labels
- VADER was more accurate on positive reviews (**21,200 correct**) 
  than negative reviews (**13,285 correct**)
- Most common positive words: *great, good, best, love, story, character*
- Most common negative words: *bad, horrible, worst, boring, terrible*
- Only **542 out of 50,000** reviews were classified as neutral — 
  showing that movie reviews tend to carry strong opinions

---

## ▶️ How to Run

Install required libraries:
```bash
pip install pandas matplotlib nltk wordcloud
```

Run the project:
```bash
python sentiment_analysis.py
```

---

## 👩‍💻 Author
**Hiba Fathima**
CodeAlpha Data Analytics Intern — June 2026
GitHub: https://github.com/hibashafi2020-code
LinkedIn: *(Add after setup)*