# demodb-medium-0.1.0
This is a medium HELM chart for creating a Stackgres PostgrSQL cluster.

It allows to customize the following:

* minio S3 connection details
* Main PostgreSQL configuration
* Custom database initialization

* Optional Backup schedule for regular backups

* prometheusAutobind: true - get Prometheus metrics in Openshift



## Comments on prometheusAutobind

This requires a correct setup of the Openshift cluster. For details check out OpenShift - Enable monitoring of Stakgres PostgreSQL servers 
