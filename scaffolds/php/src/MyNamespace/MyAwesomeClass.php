<?php

namespace MyNamespace;

class MyAwesomeClass
{
    private $amount;

    /**
     * @param int $amount
     */
    public function __construct(int $amount)
    {
        $this->amount = $amount;
    }

    /**
     * Return the amount of my awesome class
     */
    public function getAmount() : int
    {
        return $this->amount;
    }

    public function negate() : self
    {
        return new MyAwesomeClass(- $this->amount);
    }
}
