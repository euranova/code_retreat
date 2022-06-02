# PHP Scaffold for Code Retreat

This scaffold comes with severals tools that work with docker under the hood.
- `php`: a PHP 7.1 executable
- `phpspec`: a PHP test framework
- `composer`: a PHP dependencies manager

Run
```bash
./php-env [command]
```
to use a tool.

See `scripts/` for build/test scripts wrapper in docker.

## Install or update dependencies

The first time you use this scaffold you need to install all dependencies.
This is done by using the PHP dependencies manager: [composer](https://getcomposer.org/).
The following command should install all the dependencies in the `/vendor` directory.
```bash
./php-env composer install
```

Sometimes you need to update your dependencies or add a new one.
As an example, we will add a second PHP unit test framework called: _phpunit_.
```bash
./php-env composer require phpunit/phpunit ^6.2
```

That's it! You can now use your favorite tools!

## Run the tests

[phpspec](http://www.phpspec.net/en/stable/manual/introduction.html) is a tool which can help you
write clean and working PHP code using behaviour driven development.
Run the following command to execute tests:

```bash
./php-env phpspec run
```

phpspec provides a tool to help you writing _specification_.
You can use it with the `desc` subcommand:
```bash
./php-env phpspec desc [MyNewNamespace]/[MyNewClass]
```

## Run the app


```bash
./php-env php app.php
```
