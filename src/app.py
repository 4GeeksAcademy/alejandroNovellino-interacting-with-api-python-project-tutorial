import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def best_tracks(artist_id):
    con = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                                client_secret=client_secret))
    response = con.artist_top_tracks(artist_id)
    return response['tracks'] if response else []

def procesado(tracks):
    data = []
    for track in tracks:
        minutes = track["duration_ms"] // (1000 * 60)
        seconds = (track["duration_ms"] // 1000) % 60
        duration_minutes = track["duration_ms"] / (1000 * 60)
        data.append({
            "name": track["name"],
            "popularity": track["popularity"],
            "duration_minutes": duration_minutes,
            "formatted_duration": f"{minutes}:{seconds:02}"
        })
    return data


load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')      
artist_id = "788HzQOFhN3mcDo0InBqbJ"
tracks = best_tracks(artist_id)
processed_tracks = procesado(tracks)
tracks_df = pd.DataFrame.from_records(processed_tracks)
tracks_df.sort_values(["popularity"], inplace=True)
print(tracks_df.head(5))
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=tracks_df, x="popularity", y="duration_minutes", color="r")
plt.title("Duracion y Popularidad")
plt.ylabel("Duración en minutos")
plt.xlabel("Popularidad")
plt.grid(True, which='both', linestyle='-.', linewidth=0.5)
plt.tight_layout()
plt.savefig("scatter_plot.png")