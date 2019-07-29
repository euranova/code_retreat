include("../src/MyModule.jl")
using Test

@testset "MyModule" begin
    @test MyModule.my_function() == "Hello world"
    @test_throws DimensionMismatch [1, 2, 3] + [1, 2]
end