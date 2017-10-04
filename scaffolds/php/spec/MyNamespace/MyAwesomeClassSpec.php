<?php

namespace spec\MyNamespace;

use MyNamespace\MyAwesomeClass;
use PhpSpec\ObjectBehavior;
use Prophecy\Argument;

class MyAwesomeClassSpec extends ObjectBehavior
{
    function let()
    {
        $this->beConstructedWith(1000);
    }

    function it_is_initializable()
    {
        $this->shouldHaveType(MyAwesomeClass::class);
    }

    function it_negates_amount()
    {
        $this
            ->negate()
            ->shouldBeLike(new MyAwesomeClass(-1000))
        ;
    }
}
