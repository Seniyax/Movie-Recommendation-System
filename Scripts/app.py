import streamlit as st
from hybride_model import hybrid_model

st.title("🎬 Movie Recommendation System")

user_id = st.number_input("Enter User ID:", min_value=1, max_value=6040, value=1)
alpha = st.slider("Adjust Hybrid Weight (CF vs CBF)", 0.0, 1.0, 0.5)
top_n = st.slider("Number of Recommendations", 1, 20, 5)

if st.button("Get Recommendations"):
    recommendations = hybrid_model(user_id, alpha, top_n)
    st.subheader("Recommended Movies:")
    st.table(recommendations)
