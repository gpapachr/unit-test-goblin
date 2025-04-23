import org.junit.jupiter.api.Test;

public class TestGoblin {

    @Test
    @TODO
    public void testNothing() {
        //TODO This test does literally nothing
    }

    @Test
    public void testFakeTest() {
        System.out.println("Wow!");
    }

    @Test
    public void testRealTest() {
        assertEquals(42, 6 * 7);
    }
}