CREATE LOGIN admin WITH PASSWORD = 'password123';
GRANT SELECT, INSERT, UPDATE ON users TO admin;

insert into users values(123, 'j', 'j', 123345, 'trg345');