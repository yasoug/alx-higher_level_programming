-- This script lists all records of the table second_table of the database hbtn_0c_0
-- Doesn’t list rows without a name value
-- Results displays the score and the name (in this order)
-- Records listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
