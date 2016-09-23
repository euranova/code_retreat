package euranova

import org.scalatest.FunSuite
import org.scalatest.FlatSpec

class ThingTest extends FlatSpec {

	"Thing.prop" should " have the right value" in {
	  val thing = new Thing()
	  assert("wrong value" != thing.prop)
	}

  "Thing" should "always return that it's ready" in {
    val thing = new Thing()
    assert(true === thing.isReady)
  }

}
