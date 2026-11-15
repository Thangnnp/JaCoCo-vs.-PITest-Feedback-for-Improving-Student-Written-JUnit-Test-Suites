package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Before {

	@Test
	void testSample1() {
		String input = "2\n" +
				"10 11\n" +
				"11 12\n" +
				"2\n" +
				"N 2\n" +
				"E 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testSample2() {
		String input = "2\n" +
				"10 11\n" +
				"11 12\n" +
				"2\n" +
				"N 2\n" +
				"W 1\n" +
				"0";
		assertEquals("No", Judge.run(input));
	}

	@Test
	void testEdgeCaseAndMultipleMovements() {
		// Thử nghiệm robot di chuyển đến các góc biên (0,0) và (20,20)
		// Đá quý ở (0,0) và (20,20). Robot đi lấy (0,0) nhưng không tới được (20,20)
		String input = "2\n" + 
				"0 0\n" + 
				"20 20\n" + 
				"4\n" + 
				"W 10\n" + 
				"S 10\n" + 
				"N 20\n" + 
				"E 10\n" + 
				"0";
		assertEquals("No", Judge.run(input));
	}
	
	
}

