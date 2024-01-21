from client import Client
from inspector import Inspector
from transport import Transport
class Exam:
    def __init__(self, client, inspector, transport, date, time, price):
        self.client = client
        self.inspector = inspector
        self.transport = transport
        self.date = date
        self.time = time
        self.price = price