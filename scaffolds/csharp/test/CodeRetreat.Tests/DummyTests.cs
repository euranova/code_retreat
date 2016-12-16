using Xunit;

namespace CodeRetreat.Tests
{
  public class DummyTests
  {
    [Fact]
    public void Hello_CallTheMethod_TheReturnValueIsHelloWorld()
    {
      // Arrange
      var dummy = new Dummy();
      // Act
      var value = dummy.Hello();
      // Assert
      Assert.Equal("Hello World!", value);
    }
  }
}
