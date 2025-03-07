DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO artists (name) VALUES ('Pixies');
INSERT INTO artists (name) VALUES ('ABBA');
INSERT INTO artists (name) VALUES ('Taylor Swift');
INSERT INTO artists (name) VALUES ('Nina Simone');