import streamlit as st
import pandas as pd

# --- 1. Page Configuration (Must be first) ---
st.set_page_config(
    page_title="Betvis | Market Scanner",
    page_icon="📉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. Hide Streamlit Branding (The Pro Look) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 3. Custom CSS for Dark Grey & Neon Green Branding ---
st.markdown(
    """
    <style>
        /* Main background */
        .stApp {
            background-color: #121212; /* Very dark grey */
            color: #E0E0E0;
        }
        /* Headers */
        h1, h2, h3 {
            color: #00FF7F !important; /* Neon Green */
            font-family: 'Courier New', monospace; /* Terminal vibe */
        }
        /* Sub-headers/Data Labels */
        label, .stMarkdown p {
            color: #B0B0B0 !important;
        }
        /* Metrics/Big Numbers */
        div[data-testid="stMetricValue"] {
            color: #00FF7F !important; /* Neon Green */
        }
        /* Progress bars */
        .stProgress > div > div > div > div {
            background-color: #00FF7F !important;
        }
        /* Custom cards */
        div.css-1r6slb0.e1tzin5v2 {
             background-color: #1E1E1E;
             border: 1px solid #333;
             padding: 20px;
             border-radius: 10px;
        }
        /* Expander headers */
        .streamlit-expanderHeader {
            background-color: #1E1E1E !important;
            color: #00FF7F !important;
            border: 1px solid #333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 4. DUMMY DATA (This will be replaced by your script later) ---
today_steamers = [
    {
        "match": "ZED FC vs Smouha",
        "bet_on": "Smouha (Away)",
        "open_odds": 3.01,
        "current_odds": 1.69,
        "drop_pct": -44,
        "ai_insight": "🧠 **AI Analysis:** Market crash is reacting to confirmed reports that ZED FC is fielding their U21 reserve squad due to league prioritization. Smouha has full motivation for cup qualification. **Value is significant.**"
    },
    {
        "match": "Nice vs Braga (Europa)",
        "bet_on": "Braga (Away)",
        "open_odds": 4.50,
        "current_odds": 2.80,
        "drop_pct": -38,
        "ai_insight": "🧠 **AI Analysis:** Nice has 0 points and is in a domestic relegation battle. They have publicly stated they will rotate heavily. Braga needs the win for seeding. Classic 'Motivation Mismatch'."
    }
]

trap_data = {
    "team": "Real Madrid",
    "market": "Home Win",
    "open": 1.40,
    "drift": 1.75,
    "insight": "Drifting up. Public loves them, but smart money is staying away due to injuries."
}


# --- 5. The Website Layout ---

# Header
st.title("📉 BETVIS")
st.markdown("**The AI-Powered Market Scanner**")
st.caption("Status: Last Updated Today at 08:00 CET 🟢")

st.divider()

# Section 1: The Steamers
st.header("🔥 Today's Top Market Moves")
st.write("These markets are crashing hard. The 'Smart Money' has moved.")

# Loop through the data to create cards
for match in today_steamers:
    with st.expander(f"⚽ {match['match']} | 📉 **{match['drop_pct']}% DROP**", expanded=True):
        
        # Top row: Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Bet On", match["bet_on"])
        with col2:
            st.metric("Opening Odds", f"{match['open_odds']}")
        with col3:
            st.metric("Current Odds", f"{match['current_odds']}")
            
        # Visual Bar
        st.write("Odds Drop Visual:")
        st.progress(abs(match['drop_pct']))

        # AI Analysis
        st.markdown("---")
        st.write(match["ai_insight"])

st.divider()

# Section 2: The Trap
st.header("⚠️ The Public Trap Warning")
st.write("Popular teams where the odds are getting *worse*.")

with st.container():
    # Simple custom styling for a container
    st.markdown(
        f"""
        <div style="background-color: #1E1E1E; padding: 15px; border-radius: 10px; border-left: 5px solid #FF4136;">
            <h3 style="margin:0;">{trap_data['team']} ({trap_data['market']})</h3>
            <p style="color: #FF4136 !important;">Drifted from <b>{trap_data['open']}</b> to <b>{trap_data['drift']}</b></p>
            <p><em>{trap_data['insight']}</em></p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# Footer
st.caption("Betvis is a data tool, not a tipster service. Betting involves risk. None of this is financial advice.")
st.caption("© 2025 Betvis. Based in Stockholm.")
