CREATE TABLE player ( 
  firstname VARCHAR(100) NOT NULL, 
  lastname VARCHAR(100) NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO player VALUES (
  'james', 
  'lebron'
);