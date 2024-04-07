from pandas import read_csv, merge


def get_song(emotion,username):
    songs_dataset = read_csv("app/static/songCount.csv", encoding="latin1")
    user_dataset = read_csv("app/static/user_data.csv", encoding="latin1")

    user_data = user_dataset[user_dataset['UserName'] == username]

    if emotion=='surprise':
        emotion= 'Surpise'
    filtered_songs = songs_dataset[songs_dataset['Mood'].str.lower() == emotion.lower()]
    filtered_songs = filtered_songs.sort_values(by='totalListenCount', ascending=False)

    user_filtered_songs = merge(filtered_songs, user_data[['SongID','UserName']], on='SongID', how='inner')
    user_filtered_songs = user_filtered_songs.drop_duplicates(subset='SongID')

    # Recommend the top N songs
    top_n = 5  # Number of songs to recommend
    top_n_songs = user_filtered_songs.head(top_n)

    # print(top_n_songs[['SongID', 'UserName', 'totalListenCount']])
    return top_n_songs


# if __name__ == '__main__':
#     songs = get_song('Neutral', 'user2')
