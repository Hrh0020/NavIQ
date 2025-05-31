import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="NavIQ Dashboard", layout="wide")

# Custom CSS styling for high-finance look
st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .main > div {
            padding-top: 2rem;
        }
        .block-container {
            padding: 2rem 3rem;
        }
        .sidebar .sidebar-content {
            background-color: #0A2342;
            color: white;
        }
        .sidebar .sidebar-content a {
            color: white;
        }
        .metric-label {
            color: #1E3A8A;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("NavIQ")
st.sidebar.markdown("---")
st.sidebar.markdown("**Dashboard**")
st.sidebar.markdown("**Analytics**")
st.sidebar.markdown("**Settings**")

# Main dashboard
st.title("NavIQ Dashboard")

# Top metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Net Asset Value", value="$248,400")

with col2:
    st.metric(label="Premium Earned", value="$6,740")

with col3:
    st.metric(label="Capital Deployment", value="82%")

# Action Button
st.markdown("""
    <style>
        .stButton button {
            background-color: #00BFFF;
            color: white;
            border-radius: 12px;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #009ACD;
        }
    </style>
""", unsafe_allow_html=True)

st.button("Update Portfolio Data")
