\c postgres;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name UNIQUE VARCHAR(255),
    pass VARCHAR(255),
    win_plays INTEGER,
    all_plays INTEGER
);

INSERT INTO users (name, pass, win_plays, all_plays) VALUES ('admin', 'ST_0192_ter', 0, 0);