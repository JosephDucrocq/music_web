import pytest
from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/albums.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ("Album(1, Meteora, 2003, 1)Album(2, IDK, 2025, 2)")

def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/albums.sql')
    post_response = web_client.post('/albums', data={'title': 'New', 'release_year': '2004', 'artist_id': '1'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == "Album created"
    
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
        "Album(1, Meteora, 2003, 1)Album(2, IDK, 2025, 2)Album(3, New, 2004, 1)"
    )

def test_get_artists(db_connection, web_client):
    db_connection.seed('seeds/artists.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ("Artist(1, Pixies)Artist(2, ABBA)Artist(3, Taylor Swift)Artist(4, Nina Simone)")

def test_post_artists(db_connection, web_client):
    db_connection.seed('seeds/artists.sql')
    post_response = web_client.post('/artists', data={'name': 'New'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == "Artist created"
    
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == (
        "Artist(1, Pixies)Artist(2, ABBA)Artist(3, Taylor Swift)Artist(4, Nina Simone)Artist(5, New)"
    )

def test_get_albums_web(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums.sql')
    page.goto(f'http://{test_web_address}/displayalbums')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Meteora',
        'IDK'
    ], use_inner_text=True)

def test_get_single_album_and_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums.sql')
    db_connection.seed('seeds/artists.sql')
    page.goto(f'http://{test_web_address}/albums/1')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Release year: 2003\n',
        'Artist: Pixies'
    ], use_inner_text=True)

def test_visit_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums.sql')
    db_connection.seed('seeds/artists.sql')
    page.goto(f'http://{test_web_address}/displayalbums')
    page.click("text='Meteora'")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Meteora')

def test_get_a_single_artist(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums.sql')
    db_connection.seed('seeds/artists.sql')
    page.goto(f'http://{test_web_address}/artists/1')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Artist ID: 1\n', 
        'Artist: Pixies'
    ], use_inner_text=True)

def test_get_artists_web(page, test_web_address, db_connection):
    db_connection.seed('seeds/artists.sql')
    page.goto(f'http://{test_web_address}/displayartists')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone'
    ], use_inner_text=True)

def test_create_new_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums.sql')
    page.goto(f'http://{test_web_address}/albums')
    page.click("text='Add a new album'")
    page.fill('input[name=title]', 'Hybrid Theory')
    page.fill('input[name=artist]', 'Linkin Park')
    page.click('text="Submit"')