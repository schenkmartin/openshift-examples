# helm

1) Create a custom HELM repository in Openshift - https://docs.openshift.com/container-platform/4.15/applications/working_with_helm_charts/configuring-custom-helm-chart-repositories.html
2) Create an application based on this HELM charts



# HELM repository contents

HELM repositories are simple HTTP sites that contain the following files:

* an ` index.yaml` describing the content of the repository
* at least one HELM package file, described in index.yaml





## Setup a custom HELM repository for Openshift

We want the charts to be available in the Openshift Console. 

To create a HelmChartRepository resource apply ` helm-chart-repository.yml` as kubeadmin user



``` bash
martin@ubuntu24:~/openshift-examples/stackgres/helm$ oc apply -f helm-chart-repository.yml 
helmchartrepository.helm.openshift.io/my-openshift-charts created
martin@ubuntu24:~/openshift-examples/stackgres/helm$ oc get HelmChartRepositories
NAME                    AGE
my-openshift-charts     8s
openshift-helm-charts   251d

```

By default, the repository will be available cluster wide in the Developer Catalog.



## Create index.yaml for charts repository

``` 
~/openshift-examples/stackgres$ helm repo index charts/ --url http://192.168.122.1/helm/openshift-charts --debug
```



## chart-simple

Simple chart for a PostgreSQL cluster.





## Upload 

``` 
curl -u upload:Secret_1234 -T index.yaml http://localhost/api/helm/openshift-charts/index.yaml

```

