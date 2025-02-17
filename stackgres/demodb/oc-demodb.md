# oc-demodb: Use oc and YML files to create a Stackgres PostgreSQL cluster with backup
Tested with Openshift 4.15, Stackgres 1.13.

Deploy a minimal PostgreSQL cluster with 2 replicas.

Further customize the deployment by creating initial users and databases.

S3 storage is emulated by a single node Minio docker container. Sadly this deployment of Minio
does not provide the adminstrative REST api. User and access key creation is manual:



---



## Minio preparation

### Create minio user with Minio GUI
* username: stackgres-pg-backup
* password: Secret_1234
* policy: readwrite

### Login into Minio with new user
* create an access key - put accesskey and secretkey values into ` Secret-minio.yml` 
* create a new bucket named "stackgres-pg-backup"



## Login into Openshift cluster with developer

This will authenticate all following oc commands.

``` bash
oc login -u developer
```



## create new OpenShift project by ProjectRequest

As enduser create a ProjectRequest and switch to the project.

``` bash
oc create -f ProjectRequest-demodb.yml
oc project demodb
```



## create secret and minio access 

``` bash
oc apply -f Secret-minio.yml
```



## create SGObjectStorage for minio access

Update value for `endpoint: 'http://192.168.122.1:9000'`  first!

``` bash
oc apply -f SGObjectStorage-minio.yml
```



## Create SGCluster demodb 

This SGCluster resource has a backup location configured, but no schedule. This means that this database cluster will archive WAL files to S3 but does not create database backups on schedule.

``` bash
oc apply -f SGCluster-demodb.yml
```



## Create a manual backup

A single manual backup can be started by creating a SGBackup resource:

``` bash
oc apply -f SGBackup-demodb-manualbackup01.yml
```

TODO: How to check the backup status? Running, Finished - w or w/o errors - wal-g output or backup pod output? 

Each database backup creates a SGBackup resource. Manual backups will not be managed by the configured retention. TODO - check this!

```
NAME                         CLUSTER   MANAGED   STATUS
demodb-manualbackup01        demodb    false     Completed
```



## Add a backup schedule to the database cluster

```oc apply -f SGCluster-demodb-with-backup.yml``` 

Check if the new backup configuration was applied:

``` bash
oc get SGCluster demodb -o yaml | yq -r ".spec.configurations.backups"
- compression: lz4
  cronSchedule: */5 * * * *
  path: sgbackups.stackgres.io/demodb/demodb/2025-02-15-15-39-38/16
  reconciliationTimeout: 300
  retention: 8
  sgObjectStorage: minio
```

The Schedule will create a new database backup every 5 minutes and keep 8 most current backups.

``` 
NAME                         CLUSTER   MANAGED   STATUS
demodb-2025-02-15-16-10-02   demodb    true      Completed
demodb-manualbackup01        demodb    false     Completed
```



## Customize PostgreSQL 

To customize the PostgreSQL server at initialization provide a SGScript resource for SGCLuster as `spec.managedSql.scripts` .



``` 
oc apply -f Secret-demodb-create-user-app01.yml 
oc apply -f ConfigMap-demodb-init-script-app01.yml
oc apply -f SGScript-demodb.yml 
oc apply -f SGCluster-demodb-with-init.yml
```
