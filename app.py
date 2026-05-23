import streamlit as st
import pandas as pd

st.set_page_config(page_title="Eco Fuel Feedback", page_icon="🌱")

st.title("🌱 Eco Fuel Live Feedback")

st.subheader("🟢 Strength")
strength = st.selectbox(
    "Select the strongest aspect:",
    ["Sustainability", "Technology", "Growth", "Customer Focus"]
)

st.subheader("🔴 Gap")
gap = st.selectbox(
    "Select a missing component:",
    ["Employees", "Markets", "Technology", "Public Image"]
)

st.subheader("🟡 Suggestion")
suggestion = st.selectbox(
    "Select a suggestion:",
    ["Expand to GCC", "Add employee focus", "Improve technology", "Increase sustainability"]
)

if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
