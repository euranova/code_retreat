package euranova

import org.scalatest.FunSuite

class MyTest extends FunSuite{

	test("prop's val is OK") {
	  val thing = new TheThing()
	  assert("not OK value" != thing.theProp)
	}
  
	test("create Thing") {
	  val thing = new TheThing()
	  assert(true === thing.isReady)
	}
  
}
