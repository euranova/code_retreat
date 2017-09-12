namespace CodeRetreat.Tests
{
    using CodeRetreat.Model;
    using Microsoft.VisualStudio.TestTools.UnitTesting;

    [TestClass]
    public class DummyTests
    {
        [TestMethod]
        public void Hello_CallTheMethod_TheReturnValueIsHelloWorld()
        {
            // Arrange
            var dummy = new Dummy();
            // Act
            var value = dummy.Hello();
            // Assert
            Assert.AreEqual("Hello World!", value);
        }
    }
}
