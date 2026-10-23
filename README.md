# Data Science & AI Salaries Explorer

An interactive Streamlit dashboard for exploring salary patterns across data science and artificial intelligence roles. Compare salaries by experience level and year, inspect distributions, and track changes in average pay over time.

**Live dashboard:** [Open the Streamlit app](https://pseb-ai-salleries-meibnfwpxpwuevrfqctkur.streamlit.app/)

## Features

- **Interactive filters:** Select one or more experience levels and work years.
- **Key metrics:** View average salary, median salary, and the number of matching job records.
- **Salary distribution:** Explore salaries in USD with a histogram and density curve.
- **Salary trends:** Compare average annual salaries across experience levels.
- **Experience comparison:** Use boxplots to inspect salary ranges and variation by seniority.

All metrics and charts update when you change the filters.

## Experience levels

| Code | Level |
| --- | --- |
| `EN` | Entry-level |
| `MI` | Mid-level |
| `SE` | Senior-level |
| `EX` | Executive-level |

## Tech stack

- Python
- Streamlit for the interactive web app
- Pandas and NumPy for data handling
- Matplotlib and Seaborn for charts

## Project files

```text
PSEB-Ai-Salleries/
├── app.py             # Streamlit dashboard
├── salaries.csv       # Salary dataset
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Run locally

1. Clone the repository.

   ```bash
   git clone https://github.com/shahmusleeh/PSEB-Ai-Salleries.git
   cd PSEB-Ai-Salleries
   ```

2. Install the dependencies.

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Start the app.

   ```bash
   streamlit run app.py
   ```

Streamlit will display a local URL in your terminal. Keep `salaries.csv` in the same folder as `app.py`.

## Dataset and analysis

The dashboard reads `salaries.csv` and uses these columns:

- `work_year`: Year of the salary observation
- `experience_level`: Experience category (`EN`, `MI`, `SE`, or `EX`)
- `salary_in_usd`: Salary expressed in US dollars

The charts summarize the observations in the dataset. They are descriptive comparisons, not predictions of future salaries.

## Project context

Developed as a data analysis and dashboard project during the PSEB bootcamp.

**Author:** [Muslih Uddin](https://github.com/shahmusleeh)

**Repository:** [PSEB-Ai-Salleries](https://github.com/shahmusleeh/PSEB-Ai-Salleries)
