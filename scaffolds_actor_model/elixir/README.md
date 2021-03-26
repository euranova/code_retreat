# Actor Model

This is an example of actors in Elixir. Since actors are built in
Erlang/Elixir, this is simply an example of a way to use them.

It features an application that starts `ActorModel.Worker` GenServers.

* Each Worker has a friend, with which it exchanges messages.
* A Worker will randomly crash (on purpose) as an example of the
  "Let it crash" philosophy.

These Workers use `ActorModel.Person` as their state `struct`,
and rely on that module to implement the greeting operations.

Tests cover:
* `Person`, to make sure mutations of the state are correct
* `Worker`, to make sure that the life cycle of the actor works
  as expected.


## Run the tests

```
./mix test --no-start --trace
```


## Run the app

```
./mix run --no-halt
```


