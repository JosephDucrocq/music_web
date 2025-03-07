import os
from flask import *
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist import *
from lib.artist_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection) 
    album = Albums(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return 'Album created', 200

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection) 
    return "".join(f'{album}' for album in repository.all())

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection) 
    return "".join(f'{artist}' for artist in repository.all())

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'])
    repository.create(artist)
    return 'Artist created', 200

@app.route('/displayalbums', methods=['GET'])
def get_albums_web():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)


@app.route('/albums/<int:id>', methods=['GET'])
def get_single_album_and_artist(id):
    connection = get_flask_database_connection(app)
    repository_albums = AlbumRepository(connection)
    album = repository_albums.find(id)
    repository_artists = ArtistRepository(connection)
    artist = repository_artists.find(id)
    if album:
        return render_template('single_album.html', album=album, artist=artist)
    else:
        return 'Album not found', 404
    
@app.route('/artists/<int:id>', methods=['GET'])
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    repository_artists = ArtistRepository(connection)
    artist = repository_artists.find(id)
    if artist:
        return render_template('single_artist.html', artist=artist)
    else:
        return 'Artist not found', 404
    
@app.route('/displayartists', methods=['GET'])
def get_artists_web():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists.html', artists=artists)

@app.route('/albums/new', methods=['GET'])
def get_album_new():
    return render_template('newalbum.html')    
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
