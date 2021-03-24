import thespian.actors as ta

def get_or_create_actor_by_name(name):
    """
    Return the actor corresponding to name if it does not exist,
    otherwise create actor with name.

    :param name: String
    """
    return ta.ActorSystem().createActor(MyClass, globalName=name)

class MyClass(ta.Actor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.given_address = None

    def receiveMessage(self, msg, sender):
        if msg["msg_type"] == "receive_address":
            self.given_address = msg["address"]
        elif msg["msg_type"] == "send_msg":
            if self.given_address:
                self.send(self.given_address,
                         {"msg_type": "print_msg",
                          "content": msg["content"]})
            else:
                self.send(get_or_create_actor_by_name("Actor2"),
                         {"msg_type": "send_msg",
                          "content": msg["content"]})
        elif msg["msg_type"] == "print_msg":
            print(msg["content"])


if __name__ == "__main__":
    #create actors
    actor1 = get_or_create_actor_by_name("Actor1")
    actor2 = get_or_create_actor_by_name("Actor2")

    actor_sys = ta.ActorSystem()
    #send address of actor2 to actor1
    actor_sys.tell(actor2, {"msg_type": "receive_address", "address": actor1})

    #tell actor1 to send a message its neighbour
    actor_sys.tell(actor1, {"msg_type": "send_msg", "content": "hello world"})

