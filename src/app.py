import os  # type: ignore
from dotenv import load_dotenv
import spotipy  # type: ignore
from spotipy.oauth2 import SpotifyClientCredentials  # type: ignore


def get_spotipy_instance() -> spotipy.Spotify:
    """
    Set the configuration of the spotipy instance and returns it.

    Returns:
        The spotipy instance ready to use.
    """

    # load the .env file variables
    load_dotenv()

    # load the variables
    spotipy_client_id: str | None = os.environ.get("CLIENT_ID")
    spotipy_client_secret: str | None = os.environ.get("CLIENT_SECRET")

    # set the spotipy client config
    auth_manager = SpotifyClientCredentials(
        client_id=spotipy_client_id, client_secret=spotipy_client_secret
    )

    # create the spotipy client
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    return spotify


def get_artist_tracks(spotify: spotipy.Spotify, artist_id: str):  # type: ignore
    """
    Get the artist top tracks


    Args:
        spotify (Spotify): Spotipy client
        artist_id (str): Artist ID

    Returns:
        The list of the top 10 artist songs in the US
    """

    # get the top 10 track of an artist
    tracks = spotify.artist_top_tracks(artist_id=artist_id)  # type: ignore

    # list of the only info needed of the tracks
    # (we only need the name of the song, the popularity and the duration (in minutes).)
    tracks_info = []

    for track in tracks["tracks"]:  # type: ignore
        # add just the needed info from the track
        tracks_info.append(  # type: ignore
            {
                "name": track["name"],
                "popularity": track["popularity"],
                "duration": (track["duration_ms"] / 1000) / 60,
            }
        )

    return tracks_info  # type: ignore
