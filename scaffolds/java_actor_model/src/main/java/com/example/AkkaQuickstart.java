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
    public static void main(String[] args) {

        final ActorSystem system = ActorSystem.create("Hello_Akka");

        // Create an actor
        ActorRef ref1 = system.actorOf(Props.create(MyActor.class), "String_actor");
        // Send an object as a message for the actor
        ref1.tell("test message", ActorRef.noSender());

        // crate 2 mroe actors and send different object as messages
        ActorRef ref2 = system.actorOf(Props.create(MyActor.class), "Int_actor");
        ref2.tell(1, ActorRef.noSender());
        ActorRef ref3 = system.actorOf(Props.create(MyActor.class), "Double_actor");
        ref3.tell(1.0, ActorRef.noSender());

        System.out.println("Actors are created.");

        try {
            // wait till all the dummy actors are done processing the messages
            Thread.sleep(10000);
        } catch (Exception ignored) {
        } finally {
            // Clean
            system.terminate();
        }

        System.out.println("system is terminated.");

        try {
            // Input to block the termination
            int s = System.in.read();
        } catch (IOException ignored){}


    }
}
