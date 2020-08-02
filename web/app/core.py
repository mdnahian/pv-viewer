from kubernetes import client, config

from common import types

config.load_kube_config()

def get_client():
    return client.CoreV1Api()

def get_pv_all():
    pvs = []
    client = get_client()
    raw_pvs = client.list_persistent_volume(watch=False)
    for item in raw_pvs.items:
        pvs.append(types.PersistentVolume(name=item.metadata.name,
        storage_class=item.spec.storage_class_name,
        status=item.status.phase,
        capacity=item.spec.capacity['storage'],
        pvc_name=item.spec.claim_ref.name,
        pvc_namespace=item.spec.claim_ref.namespace).toJSON())
    return pvs

def get_files_from_pv(pv_name, path='.'):
    client = get_client()
    return []


