# 🎬 Movie Recommendation System 
 This Projects implements a Movie Recommendation System with a Hybrid approch,It Combines **Collaborative Filtering (CF)** and **Content Based Filtering (CBF)** , Leveraging the 1M data set from Movie Lens.

## Project Overview 
The movie recommendation system that leverages a hybrid approach, combining Collaborative Filtering (CF) and Content-Based Filtering (CBF) to provide personalized movie recommendations. The system uses a weighted formula, **Final Recommendation = α * CF + (1-α) * CBF**, where the parameter **α** balances the contributions of both methods to optimize recommendation accuracy and relevance.

## Objectives 
1) Build a robust recommendation system that integrates user-user or item-item similarity (CF) with content-based features (CBF) to address limitations of individual approaches.



2) Enhance recommendation quality by leveraging user preferences and movie attributes.



3) Allow flexibility in tuning the hybrid model through the α parameter to adapt to different user needs or dataset characteristics.

## Methodology
1) ### Collaborative Filtering (CF)
   - Utilizes user-item interactions,Ratings to identify patterns and similarities.
   - Employs a algorithm **Single Value Decomposition(SVD)** (Matrix Factorization)  to predict user preferences based on similar users which relies on a user-item rating matrix.
  
2) ### Content Based Filtering (CBF)
   - Recommends movies based on the genres and the movie title.
   - Uses feature extraction by **TF-IDF** for genres and title then calculate the similarity measures by **cosine similarity** to match movies to user profiles.

3) ## Hybrid Model
   - Combines CF and CBF scores using **Final Recommendation = α * CF + (1-α) * CBF**, where **α (0 ≤ α ≤ 1)** is a tunable parameter.
   - Tunning α,experimentally determined to balance personalization (CF) and content relevance (CBF). For example, higher α emphasizes user similarity, while lower α prioritizes movie features.

## Structure 
```Bash
📁 Data/
│   ├── movies.dat          # Raw movie data ( MovieLens movie details)
│   ├── ratings.dat        # Raw user ratings data
│   ├── users.dat          # Raw user information data
│   ├── CF_data.csv        # Preprocessed data for collaborative filtering
│   ├── merged_movielens.csv # Merged and cleaned dataset 
📁 notebooks/
│   ├── EDA.ipynb          # Notebook for exploratory data analysis
│   ├── preprocessing.ipynb # Notebook for data cleaning and preprocessing
│   ├── CF.ipynb           # Notebook for collaborative filtering implementation
│   ├── cbf.ipynb          # Notebook for content-based filtering implementation
📁 Scripts/
│   ├── hybrid_model.py    # Script for the hybrid recommendation model
│   ├── app.py            # Script for the application interface
📄 Requirements.txt         # List of required Python packages
📄 README.md               # Project documentation 
```

## Tools and Libraries
- Python
- Pandas/Numpy
- Scikit-learn
- Surprise
- Streamlit

## Challenges
**Cold Start Problem** was mitigated by implementing CBF 

## Future Improvements
- Developing a more sophisticated model by incoparting deep learning techniques
- Integrating additional data sources
- Scalling it for a real-time behaviour


  

  
![Screenshot 2025-05-23 172118](https://github.com/user-attachments/assets/f832c86b-abd5-434f-ac7a-2550e3fdaa6e)





     
