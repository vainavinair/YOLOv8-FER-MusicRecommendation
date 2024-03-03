from pandas import read_csv


def get_song(emotion):
    songs_dataset = read_csv("D:/Study/College/SEM-6/Research/code/dataset/SongDataset2/songCount.csv", encoding="latin1")
    if emotion=='surprise':
        emotion= 'Surpise'
    filtered_songs = songs_dataset[songs_dataset['Mood'].str.lower() == emotion.lower()]
    filtered_songs = filtered_songs.sort_values(by='totalListenCount', ascending=False)
    # Recommend the top N songs
    top_n = 5  # Number of songs to recommend
    top_n_songs = filtered_songs.head(top_n)
    # print(top_n_songs)
    return top_n_songs