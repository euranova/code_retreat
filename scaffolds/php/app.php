<?php

# For libraries that specify autoload information,
# Composer generates a vendor/autoload.php file.
# You can simply include this file and start using
# the classes that those libraries provide without
# any extra work:
require __DIR__ . '/vendor/autoload.php';

$myClass = new MyNamespace\MyAwesomeClass(50);
var_dump($myClass->getAmount());

$myNegateClass = $myClass->negate();
var_dump($myNegateClass->getAmount());
