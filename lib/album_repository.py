from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM albums')
        return [Albums(row['id'], row['title'], row['release_year'], row['artist_id'])
                for row in rows
        ]
    
    def create(self, album):
        self.connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])
        return None
    
    def find(self, album_id):
        rows = self.connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Albums(row["id"], row['title'], row['release_year'], row['artist_id'])