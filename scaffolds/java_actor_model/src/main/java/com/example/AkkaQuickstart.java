package com.example;

import akka.actor.ActorSystem;
import akka.actor.AbstractActor;
import akka.actor.ActorRef;
import akka.actor.Props;

import java.io.IOException;


class MyActor extends AbstractActor {
    public Receive createReceive() {
        return receiveBuilder()
        .match(String.class, p -> {
            Thread.sleep(5000);
            System.out.println("This is the String message. The message is: " + p);
        })
        .matchAny(p -> {
            Thread.sleep(5000);
            System.out.println("The class name of this message is: " + p.getClass().getName());
        })
        .build();
    }
}


public class AkkaQuickstart {
    public static void main(String[] args) throws InterruptedException{

        final ActorSystem system = ActorSystem.create("Hello_Akka");

        // Create an actor
        ActorRef stringActor = system.actorOf(Props.create(MyActor.class), "String_actor");
        // Send a String as a message for the actor
        stringActor.tell("test message", ActorRef.noSender());

        // crate 2 more actors and send different types of messages
        ActorRef ref2 = system.actorOf(Props.create(MyActor.class), "Int_actor");
        ref2.tell(1, ActorRef.noSender());
        ActorRef ref3 = system.actorOf(Props.create(MyActor.class), "Double_actor");
        ref3.tell(1.0, ActorRef.noSender());

        System.out.println("Actors are created.");

        // wait till all the dummy actors are done processing the messages
        Thread.sleep(10000);
        system.terminate();
        System.out.println("The Actor system has been terminated.");

        try {
            // Input to block the termination
            int s = System.in.read();
        } catch (IOException ignored){}


    }
}
