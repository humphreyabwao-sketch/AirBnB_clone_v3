#!/usr/bin/python3
def get(self, cls, id):
    from models import classes
    if cls not in classes.values():
        return None
    obj = self.__session.query(cls).get(id)
    return obj

def count(self, cls=None):
    from models import classes
    if not cls:
        return len(self.__session.query(State).all())
    if cls not in classes.values():
        return 0
    return len(self.__session.query(cls).all())
