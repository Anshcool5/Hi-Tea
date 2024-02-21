drop table if exists users;

CREATE TABLE users (
    id int,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    postalc CHAR(7),
    primary key (id)
);