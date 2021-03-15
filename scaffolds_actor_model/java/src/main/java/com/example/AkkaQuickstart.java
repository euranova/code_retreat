package com.example;

import akka.actor.ActorSystem;
import akka.actor.AbstractActor;
import akka.actor.ActorRef;
import akka.actor.Props;
import akka.actor.ActorSelection;
import akka.actor.ActorPath;

import java.io.IOException;


class DummyData{
    DummyData(){
    }
}


class MyActor extends AbstractActor {
    public Receive createReceive() {
        return receiveBuilder()
        .match(String.class, p -> {
            Thread.sleep(5000);
            System.out.println("This is a String message. The message is: " + p);
        })
        .match(DummyData.class, p -> {
            System.out.println("This is a DummyData message.");
            // This is how you can obtain an actor's referance from within the context of another actor
            final ActorSelection actorSelection = context().system().actorSelection("user/String_actor");
            actorSelection.tell("test actorSelection from within the context of another actor", ActorRef.noSender());
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

        // Props is a configuration class to specify options for the creation of actors
        Props prob = Props.create(MyActor.class);

        // Create an actor with the name "String_actor"
        ActorRef stringActor = system.actorOf(prob, "String_actor");
        System.out.println("The Actor Path is: " + stringActor.path());
        System.out.println("The Actor name is: " + stringActor.path().name());
        System.out.println("");

        // Send a String as a message for the actor
        stringActor.tell("test message", ActorRef.noSender());

        // Create 2 more actors and send different types of messages
        ActorRef intActor = system.actorOf(prob, "Int_actor");
        intActor.tell(1, ActorRef.noSender());
        ActorRef doubleActor = system.actorOf(prob, "Double_actor");
        doubleActor.tell(1.0, ActorRef.noSender());
        System.out.println("Actors are created and messages are sent.\n");

        // wait till all the dummy actors are done processing the messages
        Thread.sleep(10000);
        System.out.println("Output of the actors should be there by now.");

        System.out.println("\n========================\n");

        // Find an actor by actor name
        final ActorSelection actorSelection = system.actorSelection("user/String_actor");
        actorSelection.tell("test actorSelection", ActorRef.noSender());
        Thread.sleep(10000);

        System.out.println("\n========================\n");

        // send a message from one actor (senderActor) to another actor (String_actor)
        ActorRef senderActor = system.actorOf(prob, "Sender_actor");
        senderActor.tell(new DummyData(), ActorRef.noSender());
        Thread.sleep(10000);

        system.terminate();
        System.out.println("\nThe Actor system has been terminated.");

        try {
            // Input to block the termination
            int s = System.in.read();
        } catch (IOException ignored){}

    }
}
