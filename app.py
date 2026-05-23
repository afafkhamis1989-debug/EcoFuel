import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Eco Fuel Live Feedback",
    page_icon="🌱",
    layout="centered"
)

# Logo
st.image("logo.png", width=100)

# Title
st.title("🌱 Eco Fuel Live Feedback")

st.markdown("### Part 4 – Gallery Walk Feedback")

st.write(
    "Please provide your feedback about Eco Fuel’s vision and mission statement."
)

st.divider()

# Green Feedback
st.subheader("🟢 Strength")

strength = st.selectbox(
    "What is the strongest aspect?",
    [
        "Sustainability",
        "Technology",
        "Growth Strategy",
        "Customer Focus",
        "Clear Vision Statement"
    ]
)

# Red Feedback
st.subheader("🔴 Gap or Missing Component")

gap = st.text_area(
    "Write a gap or missing component:"
)

# Yellow Feedback
st.subheader("🟡 Suggestion for Improvement")

suggestion = st.text_area(
    "Write your suggestion:"
)

st.divider()

# Submit button
if st.button("Submit Feedback"):

    st.success("✅ Thank you for your feedback!")

    # Create feedback table
    results = pd.DataFrame({
        "Category": ["Strength", "Gap", "Suggestion"],
        "Feedback": [strength, gap, suggestion]
    })

    st.subheader("📊 Submitted Feedback")

    st.dataframe(results, use_container_width=True)

st.divider()

st.caption("Eco Fuel © Sustainable Healthy Food Delivery")
