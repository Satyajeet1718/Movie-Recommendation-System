import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class MovieRecommender:
    def __init__(self, credits_path, movies_path):
        self.credits_df = pd.read_csv(credits_path)
        self.movies_df = pd.read_csv(movies_path)
        self.df = self._prepare_data()
        self.cosine_sim = self._calculate_cosine_similarity()

    def _prepare_data(self):
        movies_df = self.movies_df.merge(self.credits_df, on='title')
        movies_df = movies_df[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        movies_df.dropna(inplace=True)
        movies_df['combined_features'] = movies_df['overview'] + movies_df['genres'] + movies_df['keywords'] + movies_df['cast'] + movies_df['crew']
        return movies_df

    def _calculate_cosine_similarity(self):
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['combined_features'].values.astype('U'))
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        return cosine_sim

    def recommend_movies(self, movie_title, n=10):
        if movie_title not in self.df['title'].values:
            return []
        idx = self.df[self.df['title'] == movie_title].index[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        movie_indices = [i[0] for i in sim_scores[1:n+1]]
        return self.df['title'].iloc[movie_indices].tolist()
