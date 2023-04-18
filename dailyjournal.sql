CREATE TABLE `moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

CREATE TABLE `entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
	`mood_id`	INTEGER NOT NULL,
	`date`	VARCHAR(50) NOT NULL,
  FOREIGN KEY(`mood_id`) REFERENCES `moods`(`id`)
);
