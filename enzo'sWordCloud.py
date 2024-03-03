import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib import cm
import os

# Your Spotify API credentials
CLIENT_ID = "your client id goes here" 
CLIENT_SECRET = "your client secret goes here"

# Playlist ID
playlist_id = '3VtimHRIoZ0InHM0gkIBcs'

# Authentication with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get the track titles from the specified playlist
results = sp.playlist_tracks(playlist_id)
track_titles = [track['track']['name'] for track in results['items']]

# Combine track titles into a single string
text = ' '.join(track_titles)

# Load the Spotify logo mask image (make sure spotify.png is in the same folder)
current_dir = os.path.dirname(__file__)  
mask_path = os.path.join(current_dir, 'spotify.png')
spotify_mask = np.array(Image.open(mask_path))

# Spotify-like colormap
spotify_colormap = cm.Greens

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='black', mask=spotify_mask, colormap=spotify_colormap).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
