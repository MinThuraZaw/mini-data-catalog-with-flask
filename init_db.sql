CREATE TABLE IF NOT EXISTS tables (
    id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(255) NOT NULL,
    database_name VARCHAR(255) NOT NULL,
    description TEXT
);
