-- init script for demodb database
\c demodb demodb
create table myinittable(init timestamp);
insert into myinittable values (now());
