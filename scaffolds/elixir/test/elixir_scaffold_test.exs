defmodule ElixirScaffoldTest do
  use ExUnit.Case
  doctest ElixirScaffold

  test "greets the world" do
    assert ElixirScaffold.hello() == :world
  end
end
