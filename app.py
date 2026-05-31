import streamlit as st
import requests

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

# Strength
st.subheader("🟢 Strength")

strength = st.selectbox(
    "What is the strongest aspect?",
    [
        "Sustainability",
        "Technology",
        "Growth Strategy",
        "Customer Focus",
        "Clear Vision Statement",
        "Other"
    ]
)

other_strength = ""

if strength == "Other":
    other_strength = st.text_input("Please specify:")

# Gap
st.subheader("🔴 Gap or Missing Component")

gap = st.text_area(
    "Write a gap or missing component:"
)

# Suggestion
st.subheader("🟡 Suggestion for Improvement")

suggestion = st.text_area(
    "Write your suggestion:"
)

st.divider()

# Submit
if st.button("Submit Feedback"):

    final_strength = other_strength if strength == "Other" else strength

    data = {
        "strength": final_strength,
        "gap": gap,
        "suggestion": suggestion
    }

    try:

        response = requests.post(
            "https://script.google.com/macros/s/AKfycbxmRF05xGNh3isBPX44OVSH3rmxYyQY4roSrpfq99pKYytmjelNJk_9ACPLevtLny4q/exec",
            json=data,
            timeout=10
        )

        if response.status_code == 200:
            st.success("✅ Thank you for your feedback!")
        else:
            st.error("❌ Failed to submit feedback.")

    except Exception as e:
        st.error(f"❌ Error: {e}")

st.divider()

st.caption("Eco Fuel © Sustainable Healthy Food Delivery")
