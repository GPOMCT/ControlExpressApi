from channels.consumer import SyncConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        layer = get_channel_layer()
        async_to_sync(layer.group_send)('chat_ulises', {
            'type': 'position_event',
            'position': 'se supone que es una posision'
        })
        # do something with topic and payload
        print("topic: {0}, payload: {1}".format(topic, payload))

    def mqtt_pub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print("topic: {0}, payload: {1}".format(topic, payload))