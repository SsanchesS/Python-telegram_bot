CREATE TABLE black_jokes(
  id integer PRIMARY KEY AUTOINCREMENT,
  black_joke TEXT
  );
CREATE TABLE  Memes_pic(
  id integer PRIMARY KEY AUTOINCREMENT,
  Meme_pic TEXT
  ); 
CREATE TABLE  stirlitz(
  id integer PRIMARY KEY AUTOINCREMENT,
  stirlitz_joke TEXT
  ); 
CREATE TABLE users_jokes(
  id integer PRIMARY KEY AUTOINCREMENT,
  joke TEXT,
  author_joke TEXT
  );