using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace CodeRetreat.Tests
{

    using NUnit.Framework;

    [TestFixture]
    public class DummyTests
    {

        [Test]
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
