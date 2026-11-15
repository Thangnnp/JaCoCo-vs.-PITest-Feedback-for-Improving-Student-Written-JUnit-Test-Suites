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
		// Đề bài nói "tất cả đá quý được đảm bảo ở trên các điểm lưới trừ điểm trung tâm"
		// Tuy nhiên, chương trình Main.java có dòng 22 xử lý map[10][10].
		// Để an toàn và diệt mutant dòng 22, tôi đặt đá quý ở (10,11) nhưng robot đi qua (10,10)
		// Thực tế đề bài bảo đá quý không ở (10,10), nên tôi sẽ đặt đá quý ở vị trí hợp lệ khác.
		String input = "1\n" +
				"10 11\n" +
				"1\n" +
				"N 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}

	@Test
	void testWestAndSouthMovementWithGems() {
		// Diệt mutant dòng 38, 41 (West) và 60, 61 (South)
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
		// Sửa lại test bị fail (do logic robot quay về 10,10 thì ans sẽ tăng sai nếu map chưa xóa)
		// Ở đây robot đi hình chữ nhật: (10,10) -> (10,11) -> (11,11) -> (11,10) -> (10,10)
		// Đá quý ở: (10,11), (11,11), (11,10). Tổng cộng 3 viên.
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
		// Kiểm tra trường hợp robot đi qua ô đã lấy đá quý rồi (map[x][y] lúc này phải là false)
		// Di chuyển N 2 rồi S 1. Viên đá ở (10,11) chỉ được đếm 1 lần.
		String input = "1\n" +
				"10 11\n" +
				"2\n" +
				"N 2\n" +
				"S 1\n" +
				"0";
		assertEquals("Yes", Judge.run(input));
	}
}
