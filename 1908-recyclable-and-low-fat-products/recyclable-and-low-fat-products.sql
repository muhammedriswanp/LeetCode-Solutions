-- Write your PostgreSQL query statement below
-- CREATE TABLE products(
--    product_id  INTEGER PRIMARY KEY ,
--    low_fats    CHAR(1) NOT NULL,
--    recyclable  CHAR(1) NOT NULL
-- );

-- INSERT INTO products(product_id,low_fats,recyclable ) VALUES
-- (0,'Y','N'),(1,'Y','Y'),(2,'N','Y'),(3,'Y','Y'),(4,'N','N');

SELECT product_id FROM Products WHERE low_fats= 'Y' AND recyclable='Y';