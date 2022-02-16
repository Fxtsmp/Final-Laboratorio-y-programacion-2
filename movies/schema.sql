DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS comments;


/* for loggin and comments control */
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

/* for save the films */
CREATE TABLE films (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  year TEXT NOT NULL,
  director TEXT NOT NULL,
  gender TEXT NOT NULL,
  sinopsis TEXT NOT NULL,
  cover TEXT NOT NULL
);

CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  film_id INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (film_id) REFERENCES films (id),
  FOREIGN KEY (author_id) REFERENCES user (id)
);