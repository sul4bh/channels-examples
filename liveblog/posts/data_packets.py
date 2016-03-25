import json


class Packet(object):
    type = None
    payload = None

    def __init__(self, payload=None):
        self.payload = payload

    def serialize(self):
        return json.dumps(
            {
                'type'   : self.type,
                'payload': self.payload
            }
        )


class CreatePost(Packet):
    type = 'create'


class DeletePost(Packet):
    type = 'delete'
