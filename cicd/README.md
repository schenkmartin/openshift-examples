# CI/CD with HELM charts

This is an example for using CICD to publish new HELM charts to a web server (or artifactory).

To start, we have

* Have a git repository containing one or more HELM charts
* Have a HELM chart repository to which we can publish new or updated HELM charts
* Have an OpenShift cluster using the repository.

What do we want to achieve when we create a new version of the chart? Meaning whenever a commit to the main branch of the repository happens:

* Create a HELM package of the chart
* Upload the package to the webserver (or artifactory)
  * refresh index.yaml if it is not an artifactory

The test environment is composed of

* CRC 4.15
* Stackgres Operator 1.13
* Gitlab (docker compose)
* Gitlab Runner (docker compose)
* Nginx folder as upload target for HELM charts



## CRC

The HELM chart repository can be added by applying the following resource config as admin: https://github.com/schenkmartin/openshift-examples/blob/main/stackgres/helm/helm-chart-repository.yml



## GIitLab 

The repository used contains a HELM chart in the folder `demodb-medium`.

This service can be found in [docker-compose.yml](./docker/docker-compose.yml)

### Credentials for web upload

To store the upload credentials in GitLab, goto the repository home page and choose Settings -> CICD -> Variables

Add 2 new variables:

* Key: HELM_REPO_USERNAME - Value: upload- Protected: FALSE
* Key: HELM_REPO_PASSWORD - Value: Secret_1234 - Protected: FALSE

TODO: using protected values requires additional settings (tags, protected repository)



## GitLab Runner

To run pipelines in Gitlab at least one runner is needed:

Goto Settings -> CICD -> New project runner

* Tags: helm
* Run untagged jobs = TRUE
* Runner description: my first runner
* Maximum Job Timeout: 600

Continue with starting the runner. It is started with the same [docker-compose.yml](./docker/docker-compose.yml) as GitLab.

With the gitlab-container running execute the following command to register the runner in GitLab by starting a shell inside the container:  ` docker exec -it gitlab-runner bash`

``` 
gitlab-runner register --url http://bc3096d14e0f --token glrt-t3_NTfnxEfNhEJsAUACACo9
```

Choose `shell` as executor. This simple executor is enough to create and upload the HELM package.

> [!NOTE]
>
> For now, some tools have to be installed manually in the gitlab-runner container:
>
> ``` 
> cd /usr/bin
> wget wget https://get.helm.sh/helm-v3.17.2-linux-amd64.tar.gz
> tar xzf helm-v3.17.2-linux-amd64.tar.gz
> mv linux-amd64/helm .
> ```



## GitLab workflow

Create the file [.gitlab-ci.yml](./helm-stackgres/.gitlab-ci.yml) in the root folder of the repository.

As soon as this file is committed to the repository, the pipeline will be executed immediately. 



## Notes

What is missing in this workflow:

* The index.yaml file for HELM repositories will not be created automatically be the webserver. An artifactory however will run this automated.