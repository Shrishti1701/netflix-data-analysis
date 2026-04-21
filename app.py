# Netflix EDA Dashboard using Streamlit (Netflix Dark Theme UI)
# Run: streamlit run app.py

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# -------------------- NETFLIX STYLE CSS --------------------
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: white;
    }

    .stApp {
        background-color: #000000;
    }

    h1, h2, h3 {
        color: #E50914;
    }

    .css-1d391kg {  /* sidebar */
        background-color: #111111;
    }

    .stMetric {
        background-color: #141414;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #E50914;
    }

    div.stButton > button {
        background-color: #E50914;
        color: white;
        border-radius: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- TITLE --------------------
st.markdown("<h1 style='text-align:center;'>🍿 Netflix Data Dashboard</h1>", unsafe_allow_html=True)

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    return df

netflix_df = load_data()

# -------------------- SIDEBAR FILTERS --------------------
st.sidebar.header("🎛 Filters")

country_filter = st.sidebar.multiselect(
    "Select Country",
    options=netflix_df['country'].dropna().unique()
)

type_filter = st.sidebar.multiselect(
    "Select Type",
    options=netflix_df['type'].unique(),
    default=netflix_df['type'].unique()
)

# Apply filters
filtered_df = netflix_df.copy()

if country_filter:
    filtered_df = filtered_df[filtered_df['country'].isin(country_filter)]

filtered_df = filtered_df[filtered_df['type'].isin(type_filter)]

# -------------------- KPI CARDS --------------------
col1, col2, col3 = st.columns(3)

col1.metric("🎬 Total Titles", len(filtered_df))
col2.metric("🎥 Movies", len(filtered_df[filtered_df['type'] == 'Movie']))
col3.metric("📺 TV Shows", len(filtered_df[filtered_df['type'] == 'TV Show']))

st.markdown("---")

# -------------------- MOVIES VS TV SHOWS --------------------
st.subheader("📊 Movies vs TV Shows")
fig1, ax1 = plt.subplots()
filtered_df['type'].value_counts().plot(kind='bar', ax=ax1, color=['#E50914', '#555555'])
ax1.set_ylabel("Count")
st.pyplot(fig1)

# -------------------- TOP COUNTRIES --------------------
st.subheader("🌍 Top Countries")
country_counts = filtered_df['country'].value_counts().head(10)
fig2, ax2 = plt.subplots()
country_counts.plot(kind='bar', ax=ax2, color='#E50914')
st.pyplot(fig2)

# -------------------- TOP GENRES --------------------
st.subheader("🎭 Top Genres")
if 'listed_in' in filtered_df.columns:
    genres = filtered_df['listed_in'].dropna().str.split(',').explode().str.strip()
    top_genres = genres.value_counts().head(10)

    fig3, ax3 = plt.subplots()
    top_genres.plot(kind='bar', ax=ax3, color='#E50914')
    st.pyplot(fig3)

# -------------------- CONTENT GROWTH --------------------
st.subheader("📈 Content Growth Over Years")
if 'release_year' in filtered_df.columns:
    year_data = filtered_df['release_year'].value_counts().sort_index()

    fig4, ax4 = plt.subplots()
    year_data.plot(ax=ax4, color='#E50914')
    st.pyplot(fig4)

# -------------------- RATINGS --------------------
st.subheader("⭐ Ratings Distribution")
if 'rating' in filtered_df.columns:
    rating_counts = filtered_df['rating'].value_counts().head(10)

    fig5, ax5 = plt.subplots()
    rating_counts.plot(kind='bar', ax=ax5, color='#E50914')
    st.pyplot(fig5)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray;'>Made with ❤️ using Streamlit | Netflix Style Dashboard</p>", unsafe_allow_html=True)

st.toast("Dashboard Loaded Successfully 🚀")