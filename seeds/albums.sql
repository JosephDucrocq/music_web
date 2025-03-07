DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INT,
    artist_id INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Meteora', '2003', 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('IDK', '2025', 2);
