defmodule ActorModel.Person do
  require Logger

  @enforce_keys [:name, :friend_name]

  defstruct friend_name: nil, name: nil, count_greetings_sent: 0, count_greetings_received: 0

  @type t() :: %__MODULE__{
          name: atom(),
          friend_name: Genserver.server(),
          count_greetings_sent: number(),
          count_greetings_received: number()
        }

  @doc """

      iex> greet(%Person{name: :a, friend_name: :b})
      {"Hello from a", %ActorModel.Person{count_greetings_received: 0, count_greetings_sent: 1, friend_name: :b, name: :a}}

  """
  def greet(%__MODULE__{name: name, count_greetings_sent: count_greetings_sent} = state) do
    Logger.info("#{name}: preparing message #{count_greetings_sent} to my friend.")
    {"Hello from #{name}", %{state | count_greetings_sent: count_greetings_sent + 1}}
  end

  @doc """

      iex> %Person{name: :a, friend_name: :b, count_greetings_received: 4} |> receive_greeting("Guten tag")
      %ActorModel.Person{count_greetings_received: 5, count_greetings_sent: 0, friend_name: :b, name: :a}

  """
  def receive_greeting(
        %__MODULE__{name: name, count_greetings_received: count_greetings_received} = state,
        message
      ) do
    simulate_possible_crash()

    sleep_time =
      100 + count_greetings_received * 100 + :rand.uniform((count_greetings_received + 1) * 100)

    Logger.info(
      "#{name}: Yay, I got a message: #{message} (#{count_greetings_received}). " <>
        "Will sleep #{sleep_time}ms to simulate something happening."
    )

    unless Mix.env() == :test do
      Process.sleep(sleep_time)
    end

    %{state | count_greetings_received: count_greetings_received + 1}
  end

  defp simulate_possible_crash() do
    if 5 == :rand.uniform(10) and Mix.env() != :test do
      raise "Simulating a crash!"
    end
  end
end
