import thespian.actors as ta

class MyClass(ta.Actor):
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
     actor_sys = ta.ActorSystem()

     #create actors
     actor1 = actor_sys.createActor(MyClass)
     actor2 = actor_sys.createActor(MyClass)

     #send address of actor2 to actor1  
     actor_sys.tell(actor1, {"msg_type": "receive_address", "address": actor2})

     #tell actor1 to send a message its neighbour
     actor_sys.tell(actor1, {"msg_type": "send_msg", "content": "hello world"})