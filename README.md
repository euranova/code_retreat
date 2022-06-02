# Code Retreat

You'll find here materials that we have developed at [ENX](https://euranova.eu)
to facilitate [code retreat](http://coderetreat.org).

## Scaffolds

When you're not comfortable with a language, it might take you a lot of time
to scaffold the minimum and start right away. This is a pity!

We provide a scaffold allowing you to start to write code and practice Test
Driven Development quickly for the following programming languages:

* [Bash](scaffolds/bash/README.md)
* [Clojure](scaffolds/clojure/README.md)
* [C++](scaffolds/cpp/README.md)
* [C#](scaffolds/csharp/README.md)
* [Elixir](scaffolds/elixir/README.md)
* [Java](scaffolds/java/README.md)
* [JavaScript](scaffolds/javascript/README.md)
* [Julia](scaffolds/julia/README.md)
* [PHP](scaffolds/php/README.md)
* [Python](scaffolds/python/README.md)
* [Ruby](scaffolds/ruby/README.md)
* [Rust](scaffolds/rust/README.md)
* [Scala](scaffolds/scala/README.md)
* [Swift](scaffolds/swift/README.md)
* [Typescript](scaffolds/typescript/README.md)

### Actor model scaffolds

We also provide starting points for training exercices that rely on the
[Actor model](https://en.wikipedia.org/wiki/Actor_model). Those can be found
in the [`scaffolds_actor_model`](scaffolds_actor_model/) folder.

## TCR

`test && commit || revert` is a practice invented by Kent Beck.

We provide scripts to use TCR with the scaffolds:

* `./scripts/tcr`: the classic version.
* `./scripts/btcr`: this script is easier to work with: build failures will **not**
  be reverted, giving you a chance to fix them.

Those scripts can be called from within a scaffold folder. They will directly
call the appropriate `scripts/build` and `scripts/test` of that folder.

For example:

```shell
cd scaffolds/javascript
../../scripts/tcr
```

Inspirations:

* <https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864>
* <http://5.45.106.120/tcr/index.php/2018/11/15/71/#more-71>

## Contribute to scaffolds

We try to follow these recommendations:

* There should be a simple, minimal example of a test
* As much as possible, the scaffold should use a well-known and established
  build tool and dependency management tool.
* Instructions should be provided to explain how to:
  * install the necessary dependencies,
  * build and
  * run the tests.
* Scripts should be provided to build and test in a consistent and predictable,
  so that it's easy for users to switch to another language location. These
  scripts are also expected by the TCR scripts. The scripts provided should be:
  * `./scripts/test`
  * `./scripts/build`
* For those who don't want to install dependencies, a script should be provided
  to make it possible to run the commands in a container, so that people can use
  the scaffolds without having anything to install except docker. Examples of such scripts can be found here:
  * [`mix`](scaffolds/elixir/mix) for Elixir
  * [`node`](scaffolds/javascript/node-env) for Javascript

### Rudimentary tests

To check that all the scaffold scripts are present and work as intended, a
testing script can be launched: [`test_all.sh`](scaffolds/test_all.sh).

## Contributors

* [Toch](https://github.com/toch)
* [jbruggem](https://github.com/jbruggem)
* [albar0n](https://github.com/albar0n)
