# dashboard.py
import streamlit as st
from config import REINVESTMENT_PERCENTAGE, KILL_SWITCH

st.set_page_config(page_title="Guardian AI Trader", layout="centered", initial_sidebar_state="expanded")

st.title("💹 Guardian AI Trader Dashboard")

# Theme toggle (dark mode)
dark_mode = st.toggle("🌙 Dark Mode", value=True)

# Slider to control reinvestment
reinvest = st.slider("Reinvestment %", 0, 100, REINVESTMENT_PERCENTAGE)

# Kill switch
kill = st.checkbox("🛑 Kill Switch", value=KILL_SWITCH)

st.info(f"Reinvestment set to: {reinvest}%")
st.warning("Kill switch is ON!" if kill else "Kill switch is OFF")

# Growth projection (mock example)
import matplotlib.pyplot as plt

growth = [100]
for i in range(1, 10):
    growth.append(growth[-1] * (1 + reinvest / 100 * 0.01))

fig, ax = plt.subplots()
ax.plot(growth, marker="o")
ax.set_title("Projected Growth (Next 10 Days)")
st.pyplot(fig)
