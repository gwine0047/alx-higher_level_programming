-- scripts creates table second in the database hbtn_0c_0
-- second_table description:
--              id INT
--              name VARCHAR(256)
--                      score INT
--if table exists, script nwon't fail
-- not to use SELECT or SHOW.
-- scripts will create the following records:
--             id = 1, name = "John", score = 10
--             id = 2, name = "Alex", score = 3
--             id =3 , anme = "Bob", score = 14
--             id = 4, name = "George", score = 8
--database name will be passed as an argument

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), SCORE INT);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
(2, "Alex", 3)
(3, "Bob", 14),
(4, "George", 8);