oc login -u kubeadmin
for podname in `oc get podmonitor -n openshift-monitoring -o yaml | yq -r '.items[].metadata.name'`; do oc delete podmonitor -n openshift-monitoring $podname;  done
