from channels.generic.websocket import WebsocketConsumer

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        # self.user = self.scope['user']
        self.accept()