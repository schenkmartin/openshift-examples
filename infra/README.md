# infra

Supportive infrastructure for OpenShift CRC.

## minio

S3 compatible storage, used for:

* Stackgres backup files



### mc: configure admin access credentials

Create admin access key in UI first.

``` 
docker exec -it infra-minio-1 bash
mc alias set local http://localhost:9000 RFW0PXcgZU7WRxBQsRyL hUq3BoWOWCBEuyykNwtXuE8ytj2fKKGKdl0J6jdW
```

## Gitea

Not used yet.

First user account created becomes admin.

Create another user:

* username: helm
* email: helm@example.com
* password: Secret_1234



```
touch README.md
git init
git checkout -b main
git add README.md
git commit -m "first commit"
git remote add origin http://localhost:3000/helm/openshift-charts.git
git push -u origin main
```



## nginx

Used as HELM repostory.

After container startup change ownership of ~/nginx directory

``` 
sudo chgrp mygrp ~/nginx
sudo chmod 777 ~/ginx
```



sudo apt install apache2-utils

htpasswd -c htpasswd upload

enter password: Secret_1234



See files/nginx/default.conf 

Upload requires the api path to preceed all paths:

``` 
curl -u upload:Secret_1234 -T ~/openshift-examples/stackgres/helm/demodb-helm-0.1.0.tgz http://localhost/api/helm/openshift-charts/demodb-helm-0.1.0.tgz
```

