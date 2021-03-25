DROP DATABASE IF EXISTS  catdopt;

CREATE DATABASE catdopt;

\c catdopt

DROP TABLE IF EXISTS catdopt; 

CREATE TABLE breeds
(
    breed PRIMARY KEY text NOT NULL,
    origin text NOT NULL,
    life_span text NOT NULL,
    description text NOT NULL
);

CREATE TABLE cats
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL PRIMARY KEY,
    img text NOT NULL PRIMARY KEY,
    breed text FOREIGN KEY REFERENCES breeds(breed)
);

CREATE TABLE adopt
(
    adopt_id SERIAL,
    cat_id int FOREIGN KEY REFERENCES cats(id),
    cat_name text FOREIGN KEY REFERENCES cats(name),
    cat_img text FOREIGN KEY REFERENCES cats(img),
    cost int NOT NULL
)

