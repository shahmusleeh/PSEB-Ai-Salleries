import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configure page style
st.set_page_config(page_title="Data Science Salaries Dashboard", layout="wide")

# Load the cleaned dataset
@st.cache_data
def load_data():
    # In a deployed setting, make sure 'salaries.csv' is in the same directory
    try:
        df = pd.read_csv('/content/sample_data/salaries.csv')
    except FileNotFoundError:
        df = pd.read_csv('salaries.csv')
    return df

df = load_data()

# Sidebar Navigation & Filters
st.sidebar.header("Dashboard Filters")

# Filter 1: Experience Level
all_experience_levels = sorted(df['experience_level'].unique())
selected_exp = st.sidebar.multiselect(
    "Select Experience Level(s)",
    options=all_experience_levels,
    default=all_experience_levels
)

# Filter 2: Work Year
all_years = sorted(df['work_year'].unique())
selected_years = st.sidebar.multiselect(
    "Select Work Year(s)",
    options=all_years,
    default=all_years
)

# Apply Filters
filtered_df = df[
    (df['experience_level'].isin(selected_exp)) &
    (df['work_year'].isin(selected_years))
]

# Main Page Layout
st.title("💼 Data Science & AI Salaries Explorer")
st.markdown("An interactive dashboard exploring salary trends, experience distributions, and key metrics across the industry.")

# Key Metrics Section
col1, col2, col3 = st.columns(3)
with col1:
    avg_salary = filtered_df['salary_in_usd'].mean() if not filtered_df.empty else 0
    st.metric(label="Average Salary (USD)", value=f"${avg_salary:,.0f}")

with col2:
    median_salary = filtered_df['salary_in_usd'].median() if not filtered_df.empty else 0
    st.metric(label="Median Salary (USD)", value=f"${median_salary:,.0f}")

with col3:
    total_records = len(filtered_df)
    st.metric(label="Total Job Records", value=f"{total_records:,}")

st.markdown("---")

# Visualization Columns
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Distribution of Salaries")
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(filtered_df['salary_in_usd'], kde=True, color='royalblue', bins=30, ax=ax)
        ax.set_title("Distribution of Salaries in USD")
        ax.set_xlabel("Salary in USD")
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

with col_right:
    st.subheader("📈 Salary Trends over Time")
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(8, 5))
        trends = filtered_df.groupby(['work_year', 'experience_level'])['salary_in_usd'].mean().reset_index()
        sns.lineplot(
            data=trends,
            x='work_year',
            y='salary_in_usd',
            hue='experience_level',
            marker='o',
            linewidth=2,
            ax=ax
        )
        ax.set_title("Average Salary Trend by Experience")
        ax.set_xlabel("Work Year")
        ax.set_ylabel("Average Salary (USD)")
        ax.set_xticks(sorted(filtered_df['work_year'].unique()))
        st.pyplot(fig)
    else:
        st.warning("No data available for the selected filters.")

st.markdown("---")

st.subheader("🏷️ Salary Distribution by Experience Level")
if not filtered_df.empty:
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(
        data=filtered_df,
        x='experience_level',
        y='salary_in_usd',
        order=['EN', 'MI', 'SE', 'EX'],
        palette='Set2',
        hue='experience_level',
        legend=False,
        ax=ax
    )
    ax.set_title("Salary Range by Experience Level")
    ax.set_xlabel("Experience Level")
    ax.set_ylabel("Salary (USD)")
    st.pyplot(fig)
else:
    st.warning("No data available to display experience boxplot.")
