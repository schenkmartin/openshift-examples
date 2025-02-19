-- init script for demodb database
create table myinittable(init timestamp);
insert into myinittable values (now());
