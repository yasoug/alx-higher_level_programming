-- This script converts  to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- hbtn_0c_0 database, first_table table and `name` field

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
