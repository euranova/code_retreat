defmodule ActorModelTest do
  use ExUnit.Case
  doctest ActorModel

  test "greets the world" do
    assert ActorModel.hello() == :world
  end
end
