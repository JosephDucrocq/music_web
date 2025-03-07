from lib.album import *

def test_constructs():
    album = Albums(1, 'Meteora', 2003, 1)
    assert album.id == 1
    assert album.title == 'Meteora'
    assert album.release_year == 2003
    assert album.artist_id == 1

def test_compare():
    album1 = Albums(1, "WTF", 2003, 1)
    album2 = Albums(1, "WTF", 2003, 1)
    assert album1 == album2

def test_convert_to_string():
    album = Albums(1, "WTF", 2003, 1)
    assert str(album) == "Album(1, WTF, 2003, 1)"