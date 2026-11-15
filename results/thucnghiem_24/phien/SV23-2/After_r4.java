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
		// Diệt mutant NO_COVERAGE dòng 22 (map[x][y] tại 10,10)
		String input = "1\n" +
				"10 10\n" +
				"1\n" +
				"N 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testEastMovementBoundaryDeep() {
		// Diệt mutant dòng 48 (changed conditional boundary ở vòng lặp for hướng East)
		// Mutant này thường là đổi j < mov thành j <= mov.
		// Nếu j <= mov, robot sẽ đi lố 1 bước. Ta đặt đá quý ở ngay sau bước cuối cùng (15,10)
		// và kiểm tra xem robot có vô tình nhặt được nó không nếu đi lố.
		// Ở đây ta đặt đá quý ở (16,10), nếu đi E 5 (từ 10,10 đến 15,10) mà nhặt được (16,10) 
		// thì tức là chương trình sai.
		String input = "1\n" +
				"16 10\n" +
				"1\n" +
				"E 5\n" +
				"0";
		assertEquals("No", Judge.run(input));
		
		// Ngược lại, đảm bảo nhặt được ở đúng điểm cuối (15,10)
		String input2 = "1\n" +
				"15 10\n" +
				"1\n" +
				"E 5\n" +
				"0";
		assertEquals("Yes", Judge.run(input2));
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
