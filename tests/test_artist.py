from lib.artist import Artist


def test_artist_constructs():
    artist = Artist(1, "Test Artist")
    assert artist.id == 1
    assert artist.name == "Test Artist"


def test_artists_format_nicely():
    artist = Artist(1, "Test Artist")
    assert str(artist) == "Artist(1, Test Artist)"


def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist")
    artist2 = Artist(1, "Test Artist")
    assert artist1 == artist2