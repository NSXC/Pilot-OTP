CREATE TABLE userinfo ( 
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                account_creation_date DATETIME NOT NULL,
                expiration_date DATETIME NOT NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                role VARCHAR(30) NOT NULL
                )
-- database make 

-- Table structure for table == auto
 CREATE TABLE IF NOT EXISTS purchases (
                  id INTEGER PRIMARY KEY,
                  product_type TEXT,
                  one_time_code TEXT
                  )

--SQLITE