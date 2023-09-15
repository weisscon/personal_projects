/* Conor Weiss
 * 3/5/23
 */

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class PieceTest {
	
	Board board;
	Piece piece1;
	Piece piece2;
	Piece piece3;
	Piece piece4;
	Piece piece5;
	Piece piece6;
	Piece piece7;
	Piece piece8;
	Piece piece9;
	Space s1;
	
	@Before
	public void setup() {
		board = new Board();
		piece1 = new Piece("@");
		piece2 = new Piece("@");
		piece3 = new Piece("@");
		piece4 = new Piece("Fred");
		piece5 = new Piece("X");
		piece6 = new Piece("@");
		piece7 = new Piece("@");
		piece8 = new Piece("@");
		piece9 = new Piece("@");
		try {
			s1 = board.findSpace("A1");
		}
		catch(Exception e) {}
	}

	@Test
	public void toStringTest() {
		assertEquals(piece1.toString(),"@");
		assertEquals(piece2.toString(),"@");
		assertEquals(piece3.toString(),"@");
		assertEquals(piece4.toString(),"Fred");
		assertEquals(piece5.toString(),"X");
	}
	
	@Test
	public void placeTest() {
		try {
			assertEquals(piece1.place(board.findSpace("A1")),0);
			assertEquals(piece2.place(board.findSpace("A4")),0);
			assertEquals(piece3.place(board.findSpace("A7")),1);
			assertEquals(piece6.place(board.findSpace("D1")),0);
			assertEquals(piece7.place(board.findSpace("G4")),0);
			assertEquals(piece8.place(board.findSpace("G7")),0);
			assertEquals(piece9.place(board.findSpace("G1")),2);
		}
		catch (Exception e) {}
	}
	
	@Test(expected = Exception.class)
	public void placeTest2() throws Exception{
		
			piece1.place(s1);
			piece6.place(s1);
	}
	
	@Test
	public void getSpaceTest() {
		try {
			piece6.place(board.findSpace("D1"));
			assertEquals(piece6.getSpace(),board.findSpace("D1"));
		}
		catch (Exception e) {}
	}
	
	@Test
	public void moveTest() {
		try {
			piece1.place(board.findSpace("A4"));
			piece2.place(board.findSpace("D2"));
			piece3.place(board.findSpace("D3"));
			assertEquals(piece1.move(board.findSpace("A1")),0);
			assertEquals(piece1.move(board.findSpace("D1")),1);
		}
		catch(Exception e) {}
	}
	
	@Test(expected = Exception.class)
	public void moveTest2() throws Exception {
		
			piece1.place(board.findSpace("A1"));
			piece1.move(board.findSpace("G7"));
		
	}
	
	@Test(expected = Exception.class)
	public void moveTest3() throws Exception{
		
			piece1.place(board.findSpace("A1"));
			piece2.place(board.findSpace("A4"));
			piece1.move(board.findSpace("A4"));
		
	}

}
