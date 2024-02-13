DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS messaging;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS email;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE messaging (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sender_id INTEGER NOT NULL,
  receiver_id INTEGER NOT NULL,
  message TEXT NOT NULL,
  FOREIGN KEY (sender_id) REFERENCES user (id),
  FOREIGN KEY (receiver_id) REFERENCES user (id)
);

CREATE TABLE payments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  amount INTEGER NOT NULL,
  message TEXT NOT NULL
);

CREATE TABLE test (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE email (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email_subject TEXT NOT NULL,
  email_body TEXT NOT NULL
);