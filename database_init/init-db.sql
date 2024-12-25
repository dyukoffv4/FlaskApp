CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    mail VARCHAR(255),
    pass VARCHAR(255),
    name VARCHAR(255),
    score INTEGER
);

INSERT INTO users (mail, pass, name, score) VALUES ('net998art@gmail.com', 'admin', 'admin', 0);