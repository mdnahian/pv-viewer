class PersistentVolume():
    def __init__(self, name, storage_class, status, capacity, pvc_name, pvc_namespace):
        self.name = name
        self.storage_class = storage_class
        self.status = status
        self.capacity = capacity
        self.pvc_name = pvc_name
        self.pvc_namespace = pvc_namespace
    
    def toJSON(self):
        return self.__dict__

    def get_current_size(self):
        return 0