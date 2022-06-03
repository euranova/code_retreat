defmodule ActorModel.Worker do
  use GenServer
  require Logger
  alias ActorModel.Person

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

    {:ok, %Person{friend_name: friend_name, name: name}, {:continue, :contact_friend}}
  end

  def handle_continue(:contact_friend, %Person{} = state), do: contact_friend(state)
  def handle_info(:contact_friend, %Person{} = state), do: contact_friend(state)

  def handle_info({:hello, message}, state) do
    state = state |> Person.receive_greeting(message)
    {:noreply, state, {:continue, :contact_friend}}
  end

  defp contact_friend(%Person{} = state) do
    {message, state} = state |> Person.greet()

    state.friend_name
    |> GenServer.whereis()
    |> case do
      pid when is_pid(pid) -> pid |> Process.send({:hello, message}, [])
      _ -> raise "Friend not found"
    end

    {:noreply, state}
  end
end
