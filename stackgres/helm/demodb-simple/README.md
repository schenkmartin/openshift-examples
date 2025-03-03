# demodb-simple-0.1.0
This is a simple HELM chart for creating a Stackgres PostgrSQL cluster.

It allows to configure 3 different things:

* minio S3 connection details - for WAL and database backups
* Main PostgreSQL configuration - Version, profile and database cluster size
* Custom database initialization - Create an user, a new database belonging to the user and execute SQL inside this database (single command for now)

Other values are default.



## Example values.yaml

A complete ` values.yaml`  for using all options looks like:

```
---
minio:
  url: http://192.168.122.1:9000
  bucket: stackgres-pg-backup
  accesskey: Rmej79BX1p44nexPTjpN
  secretkey: gfmR2O4MhyHIZC5xZ81dbgERPO3uuGzxjBeOmpMV
sgcluster:
  version: 16
  profile: development
  disksizegb: 20
init:
  username: "app01"
  password: "secret"
  userobjects:
    database: "mydb"
    initsql: "CREATE TABLE mytable01 (init timestamp);"
```



# TODO

## custom init

* Password must not be displayed in clear text
* Allow multiline text input or usage of a configmap containing the key: initsql ?

