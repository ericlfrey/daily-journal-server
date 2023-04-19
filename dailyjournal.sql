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

INSERT INTO `moods` VALUES (null, 'Happy');
INSERT INTO `moods` VALUES (null, 'Sad');
INSERT INTO `moods` VALUES (null, 'Angry');
INSERT INTO `moods` VALUES (null, 'Ok');

INSERT INTO `entries` VALUES (null, 'Javascript', 'I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.', 1 , 'Wed Sep 15 2021 10:10:47 ');
INSERT INTO `entries` VALUES (null, 'Python', "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake", 4 , 'Wed Sep 15 2021 10:11:33 ');
INSERT INTO `entries` VALUES (null, 'Python', "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks", 3 , 'Wed Sep 15 2021 10:13:11 ');
INSERT INTO `entries` VALUES (null, 'Javascript', 'Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.', 2 , 'Wed Sep 15 2021 10:14:05 ');

SELECT
    e.id,
    e.concept,
    e.entry,
    e.mood_id,
    e.date
FROM entries e
WHERE e.entry LIKE '%java%' OR e.concept LIKE '%java%'

SELECT
      e.id,
      e.concept,
      e.entry,
      e.mood_id,
      e.date,
      m.label mood
  FROM entries e
  JOIN moods m
      ON m.id = e.mood_id

SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date,
            m.label mood
        FROM entries e
        JOIN moods m
            ON m.id = e.mood_id
        WHERE e.id = 1
