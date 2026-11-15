package codenet;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class After {

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
	void testSample3() {
		String input = "3\n" +
				"0 15\n" +
				"5 10\n" +
				"5 15\n" +
				"5\n" +
				"W 10\n" +
				"S 10\n" +
				"N 20\n" +
				"E 10\n" +
				"S 10\n" +
				"0";
		assertEquals("No", Judge.run(input));
	}

	@Test
	void testGemAtStartPointFixed() {
		// Mặc dù đề bài nói đá quý không ở (10,10), nhưng Main.java có code xử lý nó (dòng 22).
		// Để diệt mutant NO_COVERAGE dòng 22, ta bắt buộc phải vi phạm ràng buộc đề bài một chút 
		// (đưa 10 10 vào input) vì PITest yêu cầu phủ dòng code đó.
		String input = "1\n" +
				"10 10\n" +
				"1\n" +
				"N 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testEastMovementBoundary() {
		// Diệt mutant dòng 48 (changed conditional boundary) bằng cách kiểm tra 
		// việc di chuyển hướng East với mov > 0. 
		// Đặt đá quý ở cuối quãng đường di chuyển để đảm bảo vòng lặp chạy hết.
		String input = "1\n" +
				"15 10\n" +
				"1\n" +
				"E 5\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testWestAndSouthMovementWithGems() {
		String input = "2\n" +
				"9 10\n" +
				"9 9\n" +
				"2\n" +
				"W 1\n" +
				"S 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testAllDirectionsAndBoundaryFixed() {
		String input = "3\n" +
				"10 11\n" +
				"11 11\n" +
				"11 10\n" +
				"4\n" +
				"N 1\n" +
				"E 1\n" +
				"S 1\n" +
				"W 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testMovementWithZeroGemsRemaining() {
		String input = "1\n" +
				"10 11\n" +
				"2\n" +
				"N 2\n" +
				"S 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}
}
