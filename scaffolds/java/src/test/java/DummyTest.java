import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class DummyTest {
  @Test
  public void itSaysHelloWorld() {
    Dummy dummy = new Dummy();
    assertEquals("Hello World!", dummy.hello());
  }
}
