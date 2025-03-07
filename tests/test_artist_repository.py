from lib.artist_repository import ArtistRepository
from lib.artist import Artist


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/artists.sql") 
    repository = ArtistRepository(db_connection) 

    artists = repository.all() 

    # Assert on the results
    assert artists == [
        Artist(1, "Pixies"),
        Artist(2, "ABBA"),
        Artist(3, "Taylor Swift"),
        Artist(4, "Nina Simone"),
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(3)
    assert artist == Artist(3, "Taylor Swift")


def test_create_record(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "The Beatles"))

    result = repository.all()
    assert result == [
        Artist(1, "Pixies"),
        Artist(2, "ABBA"),
        Artist(3, "Taylor Swift"),
        Artist(4, "Nina Simone"),
        Artist(5, "The Beatles"),
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Artist(1, "Pixies"),
        Artist(2, "ABBA"),
        Artist(4, "Nina Simone"),
    ]