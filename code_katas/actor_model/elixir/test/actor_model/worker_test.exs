defmodule ActorModel.WorkerTest do
  use ExUnit.Case
  alias ActorModel.Worker
  doctest ActorModel.Worker, import: true

  describe "The Worker" do
    test "Fails if some options are missing" do
      assert_raise KeyError, fn ->
        Worker.start_link([])
      end
    end

    test "Can start correctly" do
      assert {:ok, _pid} = Worker.start_link(name: :john, friend_name: :patrick)
    end

    test "Sends a greeting" do
      assert {:ok, pid} = Worker.start_link(name: :john, friend_name: self())
      assert_receive {:hello, "Hello from john"}, 2000
    end
  end
end
