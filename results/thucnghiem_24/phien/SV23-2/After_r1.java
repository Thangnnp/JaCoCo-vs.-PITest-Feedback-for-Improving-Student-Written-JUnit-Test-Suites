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
	void testGemAtStartPoint() {
		// Test trường hợp đặc biệt: đá quý nằm ngay tại vị trí xuất phát (10,10)
		// Mutant dòng 22 (map[x][y])ans++ cần được phủ.
		String input = "1\n" +
				"10 10\n" +
				"1\n" +
				"N 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testWestAndSouthMovementWithGems() {
		// Test để diệt mutant ở dòng 38, 41 (West) và 60, 61 (South)
		// Đặt đá quý trên đường đi về phía Tây và phía Nam
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
	void testAllDirectionsAndBoundary() {
		// Di chuyển đủ 4 hướng và kiểm tra vòng lặp di chuyển (mov)
		// Đảm bảo ans++ và map[x][y] = false được thực hiện đúng
		String input = "4\n" +
				"10 11\n" +
				"11 11\n" +
				"11 10\n" +
				"10 10\n" +
				"4\n" +
				"N 1\n" +
				"E 1\n" +
				"S 1\n" +
				"W 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}
}

