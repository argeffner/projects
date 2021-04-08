DROP DATABASE IF EXISTS  catdopt;

CREATE DATABASE catdopt;

\c catdopt


-- CREATE TABLE users
-- (
--     username text PRIMARY KEY,
--     password text NOT NULL,
--     email text NOT NULL,
--     UNIQUE (username, password, email)
-- );

-- CREATE TABLE cats
-- (
--     id SERIAL PRIMARY KEY,
--     img text NOT NULL,
--     breed text NOT NULL,
--     username text REFERENCES users (username),
--     UNIQUE (id, img, breed)
-- );

-- CREATE TABLE adopt
-- (
--     cat_id integer, cat_img text, username text,
--     cat_name text NOT NULL,
--     FOREIGN KEY (cat_id) REFERENCES cats (id),
--     FOREIGN KEY (cat_img) REFERENCES cats (img),
--     FOREIGN KEY (username) REFERENCES users (username)  
-- );

-- CREATE TABLE cost
-- (
--     user_id text REFERENCES users(username),
--     price integer NOT NULL   
-- );

