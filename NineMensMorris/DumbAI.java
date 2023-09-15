/* Conor Weiss
 * 3/4/23
 */

import java.util.Random;
import java.util.Arrays;


/**
 * DumbAI extends Player.  It uses randomly generated numbers to make moves
 * @author Conor
 *
 */
public class DumbAI extends Player implements AIDriven {
	private String[] boardSpaces = {"A1","A4","A7","B2","B4","B6","C3","C4","C5","D1","D2","D3","D5","D6","D7","E3","E4","E5","F2","F4","F6","G1","G4","G7"};
	
	Random brain = new Random();
	
	public DumbAI() {
		super("Dumbo");
	}
	
	/**
	 * takeAction method.
	 * uses the random generator to make moves.
	 * Much of this code is borrowed from the gameDriver.
	 */
	
	
	public void takeAction() {
		
		//As in gameDriver, after all 9 pieces are placed, move pieces instead of placing
		if (getPieceCount() == 9) {
			int[] pieceMemory = {1, 1, 1, 1, 1, 1, 1, 1, 1};	//Set up memory to allow AI to forfeit
			int[] failState = {0, 0, 0, 0, 0, 0, 0, 0, 0};
			boolean success = false;
			while (!success) {									
				if (Arrays.equals(pieceMemory, failState)) {	//If we've tried everything and we have no options, forfeit the game.
					try {
						getBoard().getOpponent(this).win();
						success = true;
					}
					catch (Exception e) {};
				}
				int AIMove = brain.nextInt(9);					//Pick a piece to move
				if (getPieces()[AIMove] == null) {				//Skip removed pieces
					pieceMemory[AIMove] = 0;					//And take them out of the options list
				}
				if (pieceMemory[AIMove] != 0) {					//if this piece is still in the options list:
					for (Space neighbor : getPieces()[AIMove].getSpace().getNeighbors()) {	//For the picked piece, try each neighbor
						if (neighbor.getPiece() == null) {
							try {
								movePiece(getPieces()[AIMove].getSpace(), neighbor);
								success = true;
							}
							catch (Exception e) {}
						}
						if (success == true) {
							break;															//Once you're successful, get out of the loop!
						}
					}
					if (!success) {															//if you didn't succeed, take this piece out of the options list
						pieceMemory[AIMove] = 0;											//since it has no currently valid moves.
					}
				}
			}
		}
		
		
		if (getPieceCount() < 9){
			boolean success = false;
			while (!success) {
				int AIMove = brain.nextInt(24);											//Pick a space
				try {
					if (getBoard().findSpace(boardSpaces[AIMove]).getPiece() == null) {	//if there's nothing there, put the piece there.
					
						placePiece(getBoard().findSpace(boardSpaces[AIMove]));
						success = true;
					}
				}
				catch (Exception e) {}
			}
				
		}
		
		//If you've made a mill (three pieces in a row), remove one of your opponent's pieces.
		while (millCount() > 0) {
			System.out.println("Dumbo has made a mill!");
			getBoard().printBoard();
			boolean success = false;
			while (!success) {
				int AIMove = brain.nextInt(9);
				try {
					millRemove(getBoard().getOpponent(this).getPieces()[AIMove].getSpace());
					success = true;
				}
				catch (Exception e) {success = false;}
			}
		}

	}

}
