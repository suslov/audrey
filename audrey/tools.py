import msgpack
import base64

from django.db import models

class ObjectField(models.Field):
    
    __metaclass__ = models.SubfieldBase

    def __init__(self,packdb_kwargs={},unpackdb_kwargs={},
                 *args,**kwargs):
        load_object_field()

def load_object_field():
    try:
        from south.modelinspector import add_introspection_rules
    except ImportError:
        pass
    else:
        add_introspection_rules(
            [([ObjectField],[],{}),],
            ["^audrey\.db\.fields\.ObjectField"])
        add_introspection_rules(
            [([UniqueIDField],[],{}),],
            ["^audrey\.db\.fields\.UniqueIDField"])
        
