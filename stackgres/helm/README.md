# helm

Here you will find:

* HELM charts that create PostgreSQL clusters based on Stackgres
* How a HELM chart repository works
* Using custom HELM chart repository with Openshift

## HELM charts

* [demodb-simple](https://github.com/schenkmartin/openshift-examples/tree/main/stackgres/helm/demodb-simple): a minimal approach, with few options
* demodb-medium: allows for some customization

## HELM repository

A HELM repository are simple HTTP sites that contains the following files:

* an `index.yaml` describing the content of the repository
* at least one HELM package file, described in index.yaml



### The HELM package

A sample HELM chart working with Openshift and the Stackgres Operator can be found in the folder demodb-simple - https://github.com/schenkmartin/openshift-examples/tree/main/stackgres/helm/demodb-simple

Create the package file for this chart by executing the following command in the helm folder. It will create the output file in the output directory.

``` 
helm package demodb-simple/ -d output/
```



### index.yaml

This file is created by executing ` helm repo index`. It is convenient to put this file in the output folder where all the package files are stored.

``` 
helm repo index output/ --url http://192.168.122.1/helm/openshift-charts
```



## Repository webserver

Copy all files of the output directory to the webserver.

I'm using nginx for a very simple setup serving static files. It also allows to upload files by providing basic authentication. 

It allows for an automated distribution of HELM packages late by using ` curl` to upload files e.g.:

``` 
curl -u upload:Secret_1234 -T index.yaml http://localhost/api/helm/openshift-charts/index.yaml
```

It is part of [infra](https://github.com/schenkmartin/openshift-examples/tree/main/infra) docker compose landscape in this repository.



## Permissions required in OpenShift

Some resources that are created by the HELM chart require special user permissions, like creating PrometheusRules.

These are created by applying the follwing configs. They will grant the user "developer" with appropriate permissions.

* ClusterRole-prometheus-rule-manager.yml
* ClusterRoleBinding-prometheus-rule-manager.yml

The Openshift cluster must be able to read service endpoints from user projects to create PodMonitor resources.  TODO this is not peristent for new projects! ClusterRole needs to be applied (configured) when a new project is created.

* ClusterRole-prometheus-k8s.yml
* ClusterRoleBinding-prometheus-k8s-global.yml



## HELM charts in Openshift UI

Beside using the standard `helm` command to deploy a HELM chart to an Openshift cluster, the UI allows for classic user input of values and apply them to the HELM chart. 



## Setup a custom HELM repository for Openshift

We want the charts to be available in the Openshift Console, so we need to setup an additional HELM chart repository in the cluster.

To create the HelmChartRepository resource apply ` helm-chart-repository.yml` as kubeadmin user.

``` bash
oc apply -f helm-chart-repository.yml 
helmchartrepository.helm.openshift.io/my-openshift-charts created

oc get HelmChartRepositories
NAME                    AGE
my-openshift-charts     8s
openshift-helm-charts   251d
```

By default, the repository will be available cluster wide in the Developer Catalog.



### TODO: How HELM charts are displayed in the Openshift UI

values.schema.json - default values are not set here, they would overwrite empty (and full?) values prvided by values.yaml

defaults from values.yaml - these values are display by default

README.md is displayed when creating a HELM release.
