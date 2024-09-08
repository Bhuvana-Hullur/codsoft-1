import numpy as np
from scipy import spatial


user_preferences = {
    'User1': {'Movie1': 4, 'Movie2': 3, 'Movie3': 5, 'Movie4': 2},
    'User2': {'Movie1': 3, 'Movie2': 5, 'Movie3': 4, 'Movie5': 1},
    'User3': {'Movie2': 4, 'Movie3': 5, 'Movie4': 3, 'Movie5': 2},
    'User4': {'Movie1': 5, 'Movie2': 4, 'Movie3': 3, 'Movie4': 1}
}


def calculate_similarity(user1, user2):
    
    preferences1 = user_preferences[user1]
    preferences2 = user_preferences[user2]

    
    common_movies = set(preferences1.keys()) & set(preferences2.keys())

    
    if len(common_movies) == 0:
        return 0
    else:
        vector1 = [preferences1[movie] for movie in common_movies]
        vector2 = [preferences2[movie] for movie in common_movies]
        return 1 - spatial.distance.cosine(vector1, vector2)


def get_recommendations(user, N):
    
    similarities = {other_user: calculate_similarity(user, other_user) for other_user in user_preferences if other_user != user}

    
    similar_users = sorted(similarities, key=similarities.get, reverse=True)[:N]

    
    recommended_movies = {}
    for similar_user in similar_users:
        for movie, rating in user_preferences[similar_user].items():
            if movie not in user_preferences[user]:
                recommended_movies[movie] = recommended_movies.get(movie, 0) + rating * similarities[similar_user]

   
    return sorted(recommended_movies, key=recommended_movies.get, reverse=True)[:N]


user = 'User4'
N = 3
recommended_movies = get_recommendations(user, N)
print("Recommended movies for", user, ":", recommended_movies)