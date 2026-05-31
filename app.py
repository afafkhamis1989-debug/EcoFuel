import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Eco Fuel Live Feedback",
    page_icon="🌱",
    layout="centered"
)

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw48AcG91GmyByC0jwwfp-6ri5NT-b6XPLOmEvIRBl1--KnhpRWehA5B7I14o23ca7a/exec"

st.image("logo.png", width=100)

st.title("🌱 Eco Fuel Live Feedback")
st.markdown("### Part 4 – Gallery Walk Feedback")

st.write("Please provide your feedback about Eco Fuel’s vision and mission statement.")

st.divider()

st.subheader("🟢 Strength")
strength = st.text_area("Write the strongest aspect:")

st.subheader("🔴 Gap or Missing Component")
gap = st.text_area("Write a gap or missing component:")

st.subheader("🟡 Suggestion for Improvement")
suggestion = st.text_area("Write your suggestion:")

st.divider()

if st.button("Submit Feedback"):

    data = {
        "strength": strength,
        "gap": gap,
        "suggestion": suggestion
    }

    response = requests.post(
        SCRIPT_URL,
        json=data,
        timeout=10
    )

    if response.status_code == 200:
        st.success("✅ Thank you for your feedback!")
        st.rerun()
    else:
        st.error("❌ Failed to submit feedback.")

st.divider()

st.subheader("📊 Live Feedback Responses")

try:
    response = requests.get(SCRIPT_URL, timeout=10)

    if response.status_code == 200:
        feedback = response.json()

        if feedback:
            df = pd.DataFrame(feedback)
            df = df.rename(columns={
                "time": "Time",
                "strength": "Strength",
                "gap": "Gap",
                "suggestion": "Suggestion"
            })

            st.dataframe(df, use_container_width=True)
        else:
            st.info("No feedback submitted yet.")
    else:
        st.warning("Could not load feedback responses.")

except Exception as e:
    st.error(f"Error loading feedback: {e}")

st.caption("Eco Fuel © Sustainable Healthy Food Delivery")
