import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class DummyTest {
  @Test
  public void itSaysHelloWorld() {
    Dummy dummy = new Dummy();
    assertEquals("Hello World!", dummy.hello());
  }
}
