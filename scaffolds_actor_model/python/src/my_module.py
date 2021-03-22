from thespian.actors import *

class MyClass(Actor):
     def __init__(self, **kwargs):
          super().__init__(**kwargs)
          self.neighbour = None

     def receiveMessage(self, msg, sender):
          if msg["msg_type"] == "receive_address":
               self.neighbour = msg["address"]
          elif msg["msg_type"] == "send_msg":
               self.send(self.neighbour, {"msg_type": "print_msg", "content": msg["content"]})
          elif msg["msg_type"] == "print_msg":
               print(msg["content"])


if __name__ == "__main__":
     actor_sys = ActorSystem()

     #create actors
     actor1 = actor_sys.createActor(MyClass)
     actor2 = actor_sys.createActor(MyClass)

     #init values   
     ActorSystem().tell(actor1, {"msg_type": "receive_address", "address": actor2})
     ActorSystem().tell(actor1, {"msg_type": "send_msg", "content": "hello world"})