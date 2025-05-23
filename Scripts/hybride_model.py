import pandas as pd

def hybrid_model(user_id,alpha = 0.5,top_n = 5):
    cf_score = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\ML\Recommendation System - movie\Data\cf_scores_user_1.csv")
    cbf_score = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\ML\Recommendation System - movie\Data\cbf_scores_user_1.csv")
    Data_set = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\ML\Recommendation System - movie\Data\merged_movielens.csv")
    movies = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\ML\Recommendation System - movie\Data\CF_data.csv")

    hybrid_df = pd.merge(cf_score,cbf_score, on="MovieID")
    hybrid_df["Hybrid_Score"] = alpha * hybrid_df["CF_scores"] + (1 - alpha) * hybrid_df["cbf_score"]

    watched = movies[movies["UserID"] == user_id]["MovieID"].tolist()
    hybrid_df = hybrid_df[~hybrid_df["MovieID"].isin(watched)]

    top_recs = hybrid_df.sort_values(by="Hybrid_Score", ascending=False).head(top_n)
    top_recs = top_recs.merge(movies[["MovieID", "Title"]], on="MovieID")
    return top_recs[["Title", "Hybrid_Score"]]
