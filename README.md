# openshift-examples
OpenShift related code examples - tested on a single node CRC Openshift environment.

Some examples rely on these tools:
* ` yq`  - a YAML query tool, practical to filter YAML output

There are some support files in the base folder:

* ` openshift-dns.sh` - Setup local DNS resolver to resolve CRC URLs
* ` openshift-rest-api.py` - Do HTTP requests with authentication and file contents. 


## stackgres
Stackgres operates PostgreSQL databases in your Openshift Cluster.

Some examples how to build a PostgreSQL cluster using HELM charts can be found here.

Some background on HELM and Openshift UI is also available.

## infra
Find supportive infrastructure code here, like minio S3 on docker.

## html5-app

A very simple web server deployment serving a static HTML5 website.
