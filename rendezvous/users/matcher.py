from functools import reduce


def match_score(user_json1, user_json2) -> int:
    # The question is if this is biased towards people with a larger artist library.
    # How does one normalise this?

    user1_artists = user_json1["items"]
    user2_artists = user_json2["items"]
    genre_frequencies = dict()

    user1_genres = set()
    for artist in user1_artists:
        for genre in artist["genres"]:
            if genre in genre_frequencies:
                genre_frequencies[genre] += 1
            else:
                genre_frequencies[genre] = 1

            user1_genres.add(genre)

    user2_genres = set()
    for artist in user2_artists:
        for genre in artist["genres"]:
            if genre in genre_frequencies:
                genre_frequencies[genre] += 1
            else:
                genre_frequencies[genre] = 1

            user2_genres.add(genre)

    # Pre: artist is present in both users' listening lists
    user1_artist_names = list(map(lambda a: a["name"], user1_artists))
    user2_artist_names = list(map(lambda a: a["name"], user2_artists))

    def get_artist_score(artst):
        return (len(user1_artist_names) - user1_artist_names.index(artst))\
            + (len(user2_artist_names) - user2_artist_names.index(artst))

    genre_intersect = user1_genres.intersection(user2_genres)
    artist_intersect = set(user1_artist_names).intersection(set(user2_artist_names))

    return reduce(lambda s, gnr: s + genre_frequencies[gnr], genre_intersect, 0)\
        + reduce(lambda s, art: s + get_artist_score(art), artist_intersect, 0)


def find_best_match(user, user_collection):
    max_score = -1
    max_user = None

    for u in user_collection:
        if u != user:
            if (sc := match_score(user, u)) > max_score:
                max_score = sc
                max_user = u

    return max_user
