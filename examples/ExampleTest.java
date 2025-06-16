// GoblinExampleFile
// not for compilation or execution

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class ExampleTest {
    @Test
    public void testAddition() {
        assertEquals(2, 1 + 1);
    }

    public void helperMethod() {
        System.out.println("Not a test");
    }

    @Ignore
    @Test
    public void ignoredTest() {
        // This test will be ignored
        assertEquals(3, 1 + 2);
    }

    @Test
    @Disabled
    public void noAssertionsTest() {
        // do nothing here
        System.out.println("This test has no assertions");
        helperMethod();
    }

    @Test
    @TODO("This test is a placeholder and needs implementation")
    public void placeholderTest() {
        // This test is a placeholder
        System.out.println("This test is a placeholder and needs implementation");
    }

    public void testWithNoAnnotation() {
        assertEquals(5, 2 + 3);
        assertEquals(6, 3 + 3);
        System.out.println("This test has multiple assertions");
    }

    public void setupMethod() {
        // This is a setup-like method without @Test annotation
        System.out.println("Setup method called");
    }

    @Test
    public void setupTestMethod() {
        // This is a setup-like method with @Test annotation
        System.out.println("Setup test method called");
    }
}
