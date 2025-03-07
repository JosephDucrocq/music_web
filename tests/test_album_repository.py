from lib.album_repository import *
from lib.album import *

def test_all_albums(db_connection):
    db_connection.seed('seeds/albums.sql')
    repository = AlbumRepository(db_connection)
    assert repository.all() == [Albums(1, 'Meteora', 2003, 1), Albums(2, 'IDK', 2025, 2)]

def test_create(db_connection):
    db_connection.seed('seeds/albums.sql')
    repository = AlbumRepository(db_connection)
    album = Albums(None, 'Test', 2025, 2)
    repository.create(album)
    assert repository.all() == [Albums(1, "Meteora", 2003, 1), Albums(2, "IDK", 2025, 2), Albums(3, "Test", 2025, 2)]

def test_find_a_record(db_connection):
    db_connection.seed("seeds/albums.sql") 
    repository_find = AlbumRepository(db_connection)
    result = repository_find.find(1)
    assert result == Albums(1, 'Meteora', 2003, 1)