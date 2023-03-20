defmodule ActorModel.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    children = [
      # Starts a worker by calling: ActorModel.Worker.start_link(arg)
      {ActorModel.Worker, name: :Quick, friend_name: :Flupke},
      {ActorModel.Worker, name: :Flupke, friend_name: :Quick}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: ActorModel.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
