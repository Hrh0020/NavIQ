import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="NavIQ", layout="wide")
st.title("📊 NavIQ Portfolio Dashboard")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Main Dashboard", "Performance", "Research"])

# Sample NAV data for portfolio value chart
nav_data = pd.DataFrame({
    "Month": ["Feb 2025", "Mar 2025", "Apr 2025"],
    "NAV": [5000, 8300, 11000]
})

# Sample tracker data
tracker = pd.DataFrame([
    {"Month": "Feb 2025", "Gross_Premium": 83, "Capital_Deployed": 5200, "Realized_Losses": 0},
    {"Month": "Mar 2025", "Gross_Premium": 322, "Capital_Deployed": 7700, "Realized_Losses": 50},
    {"Month": "Apr 2025", "Gross_Premium": 380, "Capital_Deployed": 9500, "Realized_Losses": 56.10},
])

tracker["Gross_Yield_%"] = (tracker["Gross_Premium"] / tracker["Capital_Deployed"]) * 100
tracker["Net_Premium"] = tracker["Gross_Premium"] - tracker["Realized_Losses"]
tracker["Net_Yield_%"] = (tracker["Net_Premium"] / tracker["Capital_Deployed"]) * 100

# Main Dashboard view
if page == "Main Dashboard":
    st.subheader("📈 Portfolio Value Over Time")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=nav_data["Month"],
        y=nav_data["NAV"],
        mode='lines+markers',
        line=dict(width=3, shape='spline'),
        marker=dict(size=8),
        name="NAV"
    ))
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis_title="Month",
        yaxis_title="Portfolio Value ($)",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧾 Monthly Performance Snapshot")
    st.dataframe(tracker.style.format({
        "Gross_Premium": "$ {:.2f}",
        "Capital_Deployed": "$ {:.0f}",
        "Realized_Losses": "$ {:.2f}",
        "Gross_Yield_%": "{:.2f}%",
        "Net_Premium": "$ {:.2f}",
        "Net_Yield_%": "{:.2f}%"
    }), use_container_width=True)

# Placeholder tabs for expansion
elif page == "Performance":
    st.subheader("📊 Detailed Sleeve & Ticker Analytics Coming Soon")
elif page == "Research":
    st.subheader("🔬 Research Terminal (AI integration planned)")

