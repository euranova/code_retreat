defmodule ActorModel.Worker do
  use GenServer
  require Logger

  def start_link(opts) do
    GenServer.start_link(__MODULE__, opts, name: opts |> Keyword.fetch!(:name))
  end

  def child_spec(opts) do
    %{
      id: opts |> Keyword.fetch!(:name),
      start: {__MODULE__, :start_link, [opts]},
      restart: :permanent
    }
  end

  def init(opts) do
    friend_name = opts |> Keyword.fetch!(:friend_name)
    name = opts |> Keyword.fetch!(:name)
    Logger.info("#{name} initializing.")

    self() |> Process.send_after(:contact_friend, 100 + :rand.uniform(1000))

    {:ok, %{friend_name: friend_name, name: name, count: 0}}
  end

  def handle_info(:contact_friend, %{friend_name: friend_name, name: name, count: count} = state) do
    Logger.info("#{name}: will send message #{count} to my friend.")
    friend_name |> GenServer.whereis() |> Process.send({:hello, "Hello from #{name}"}, [])
    {:noreply, %{state | count: count + 1}}
  end

  def handle_info({:hello, message}, %{name: name, count: count} = state) do
    sleep_time = 100 + count * 100 + (:rand.uniform((count + 1) * 100))
    Logger.info("#{name}: Yay, I got a message: #{message}. Will sleep #{sleep_time}ms.")
    Process.sleep(sleep_time)
    self() |> Process.send(:contact_friend, [])
    {:noreply, state}
  end
end
