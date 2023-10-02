#!/usr/bin/python3
def get(self, cls, id):
    if cls not in classes.values():
        return None
    for obj_id, obj in FileStorage.__objects.items():
        if obj.id == id and obj.__class__ == cls:
            return obj
    return None

def count(self, cls=None):
    count = 0
    if not cls:
        for obj in FileStorage.__objects.values():
            count += 1
        return count
    if cls not in classes.values():
        return 0
    for obj in FileStorage.__objects.values():
        if obj.__class__ == cls:
            count += 1
    return count
