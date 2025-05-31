import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# --- App Branding & Styling ---
st.set_page_config(page_title="NavIQ | Portfolio Dashboard", layout="wide")

NAVIQ_ACCENT = "#10305C"  # Deep institutional blue
CARD_BG = "#181C22"       # Slightly lighter than Streamlit's dark for stat cards
CARD_TEXT = "#FFFFFF"     # White text for dark cards

# --- Custom CSS to fix stat cards for dark mode ---
st.markdown(f"""
    <style>
        /* Sidebar */
        [data-testid="stSidebar"] {{
            background: {NAVIQ_ACCENT} !important;
        }}
        /* Main background */
        .stApp {{
            background-color: #121418;
        }}
        /* Stat Cards */
        .stat-card {{
            border-radius: 0.75rem;
            background: {CARD_BG};
            color: {CARD_TEXT} !important;
            box-shadow: 0 2px 8px 0 rgba(16,48,92,.13);
            padding: 1.5rem;
            margin-bottom: 1.25rem;
            font-family: 'Inter', 'Lato', 'Roboto', sans-serif;
        }}
        /* White card for charts */
        .white-card {{
            border-radius: 0.75rem;
            background: #fff;
            box-shadow: 0 2px 8px 0 rgba(16,48,92,.08);
            padding: 1.5rem;
            margin-bottom: 2rem;
        }}
        /* Table tweaks */
        .stDataFrame tbody tr {{
            background-color: #161B22 !important;
            color: #fff !important;
        }}
        /* Remove Streamlit footer */
        footer {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown(f"<h2 style='color:#fff;letter-spacing:2px;margin-bottom:2rem;'>NavIQ</h2>", unsafe_allow_html=True)
    st.markdown("##### Portfolio Dashboard")
    st.markdown("---")
    st.write(" ")
    st.write(" ")
    st.caption("High Finance Portfolio Intelligence")
    st.write(" ")

# --- Portfolio Value & Allocation Data (April 2025) ---
portfolio_value = 6934.31
cash_equiv = 4950.00 + 472.31
equities = 1603.00
options = 1.28 / 100 * portfolio_value

alloc_labels = ['Cash & Equiv', 'Equities', 'Options']
alloc_vals = [cash_equiv, equities, options]

# --- Stat Cards ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div class='stat-card'><b>Portfolio Value</b><br><span style='font-size:2rem;color:{CARD_TEXT};'>${portfolio_value:,.2f}</span></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='stat-card'><b>Cash %</b><br><span style='font-size:2rem;color:{CARD_TEXT};'>{round((cash_equiv/portfolio_value)*100, 1)}%</span></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='stat-card'><b>Equity %</b><br><span style='font-size:2rem;color:{CARD_TEXT};'>{round((equities/portfolio_value)*100, 1)}%</span></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='stat-card'><b>Options %</b><br><span style='font-size:2rem;color:{CARD_TEXT};'>{round((options/portfolio_value)*100, 1)}%</span></div>", unsafe_allow_html=True)

st.write(" ")

# --- Allocation Donut Chart in White Card ---
with st.container():
    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    alloc_fig = go.Figure(data=[go.Pie(
        labels=alloc_labels,
        values=alloc_vals,
        hole=.7,
        marker=dict(colors=[NAVIQ_ACCENT, "#f1f5fa", "#ADB9C6"])
    )])
    alloc_fig.update_layout(
        showlegend=True,
        legend=dict(orientation="h", y=-0.2),
        margin=dict(l=40, r=40, t=10, b=10),
        height=320,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, Lato, sans-serif", size=14, color="#222")
    )
    st.plotly_chart(alloc_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Portfolio Value Over Time (Mock Data) ---
hist_df = pd.DataFrame({
    "Month": ["Feb", "Mar", "Apr"],
    "Portfolio Value": [3016.95, 3107.65, 6934.31]
})
st.markdown('<div class="white-card">', unsafe_allow_html=True)
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(
    x=hist_df["Month"], y=hist_df["Portfolio Value"],
    mode='lines+markers', line=dict(width=3, color=NAVIQ_ACCENT)
))
line_fig.update_layout(
    title="Portfolio Value Over Time",
    xaxis_title=None, yaxis_title=None,
    height=320,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=40, r=40, t=40, b=10),
    font=dict(family="Inter, Lato, sans-serif", size=14, color="#222")
)
st.plotly_chart(line_fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Open Positions Table ---
st.markdown("### Open Positions")
positions = pd.DataFrame([
    {"Ticker": "NCLH", "Type": "Equity", "Qty": 100, "Price": 16.03, "Value": 1603.00, "Status": "Held"},
    {"Ticker": "KEY 5/23 Put $14", "Type": "Short Put", "Qty": 1, "Price": -30.00, "Value": -30.00, "Status": "Open"},
    {"Ticker": "KHC 5/9 Put $28.5", "Type": "Short Put", "Qty": 1, "Price": -28.00, "Value": -28.00, "Status": "Open"},
    {"Ticker": "RIOT 5/9 Put $7", "Type": "Short Put", "Qty": 1, "Price": -33.00, "Value": -33.00, "Status": "Open"},
])
st.dataframe(positions, use_container_width=True, hide_index=True)

# --- Recent Activity (Simple Feed) ---
st.markdown("### Recent Activity")
activity = [
    "04/24 Sold KHC 5/9 Put $28.5",
    "04/24 Sold RIOT 5/9 Put $7",
    "04/25 Sold KEY 5/23 Put $14",
    "04/21 $1,500 Deposit",
    "04/17 $2,500 Deposit",
    "04/03 Assigned NCLH 100 shares @ $19.50",
]
for act in activity:
    st.write(f"- {act}")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("NavIQ © 2025 | High Finance Portfolio Intelligence")
