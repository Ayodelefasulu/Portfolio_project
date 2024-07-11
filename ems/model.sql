-- This database schema contains all tables such as
-- user, profile, `transaction`, activities, buyData, buyAirtime, payUtility, fundWallet, admin, adminActivities

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS profile;
DROP TABLE IF EXISTS `transaction`;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS buy_data;
DROP TABLE IF EXISTS buy_airtime;
DROP TABLE IF EXISTS pay_utility;
DROP TABLE IF EXISTS fund_wallet;
DROP TABLE IF EXISTS admin;
DROP TABLE IF EXISTS admin_activities;


CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  phonenumber TEXT NOT NULL,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);


CREATE TABLE `transaction` (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  transaction_type TEXT NOT NULL,
  amount REAL NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(user_id) REFERENCES user(id)
);


CREATE TABLE profile (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER UNIQUE NOT NULL,
  firstname TEXT,
  lastname TEXT,
  email TEXT UNIQUE,
  phonenumber TEXT,
  FOREIGN KEY(user_id) REFERENCES user(id)
);


CREATE TABLE activities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  activity TEXT NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(user_id) REFERENCES user(id)
);


CREATE TABLE buy_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  `transaction_id` INTEGER UNIQUE NOT NULL,
  data_plan TEXT NOT NULL,
  phonenumber TEXT NOT NULL,
  amount REAL NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(`transaction_id`) REFERENCES `transaction(id)`
);


CREATE TABLE buy_airtime (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  `transaction_id` INTEGER UNIQUE NOT NULL,
  phonenumber TEXT NOT NULL,
  amount REAL NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(`transaction_id`) REFERENCES `transaction(id)`
);


CREATE TABLE pay_utility (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  `transaction_id` INTEGER UNIQUE NOT NULL,
  utility_type TEXT NOT NULL,
  account_number TEXT NOT NULL,
  amount REAL NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(`transaction_id`) REFERENCES `transaction(id)`
);


CREATE TABLE fund_wallet (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  `transaction_id` INTEGER UNIQUE NOT NULL,
  amount REAL NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(`transaction_id`) REFERENCES `transaction(id)`
);


CREATE TABLE admin (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE admin_activities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  admin_id INTEGER NOT NULL,
  activity TEXT NOT NULL,
  created DATETIME DEFAULT CURRENT_created,
  FOREIGN KEY(admin_id) REFERENCES admin(id)
);
