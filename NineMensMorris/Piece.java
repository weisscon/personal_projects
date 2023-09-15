/* Conor Weiss
 * 3/1/23
 */

/**
 * Piece class - represents the game pieces used to play the game.
 * @author Conor
 *
 */

public class Piece {
	
	private String symbol;
	private Space space = null;
	
	/**
	 * Constructor: sets the symbol for the piece
	 * @param symbol - the string that will represent the piece on the board.
	 */
	
	public Piece(String symbol) {
		this.symbol = symbol;
	}
	
	/**
	 * place: places the piece on the given space on the board as long as it is empty.  Returns the number of mills made by millCheck().
	 * @param space
	 * @throws an exception if the space is not empty
	 * @return number of mills made
	 */
	
	public int place(Space space) throws Exception{
		if (space.getPiece() != null) {
			System.out.println();
			throw new Exception("There is already a piece where you would like to move.  Choose a different space.");
		}
		else {
			this.space = space;
			this.space.setPiece(this);
			return this.space.millCheck();
		}
	}
	
	/**
	 * Getter method for the piece's space.
	 * @return the space that this piece is placed on.
	 */
	public Space getSpace() {
		return space;
	}
	
	/**
	 * toString override.  Prints the piece's symbol.  Used to print the board.
	 */
	
	@Override
	public String toString() {
		return symbol;
	}
	
	/**
	 * move: moves the piece from its current space to a neighboring space
	 * @param space - the space that the piece is moving to
	 * @throws an exception if the space is not a neighbor or if it is not empty
	 * @return the number of mills made by the move
	 */
	
	public int move(Space space) throws Exception {
		boolean neighbor = false;
		for (Space space2 : this.space.getNeighbors()) {		//Check the neighbors array of the destination space
			if (space2 == space) {						//if you find this space there
				neighbor = true;						//they are neighbors.
			}
		}
		if (neighbor) {									//If they are neighbors:
				this.space.millMoveUpdate();			//remove mill status if any mills will be broken by this move.
				this.space.setPiece(null);				//remove this piece from its space
				return this.place(space);				//place the piece on its new space.  This throws an exception if the space is already full
		}												//which is desired, as the move is what's failing.
		else {
			System.out.println("You must move to a neighboring space"); 
			throw new Exception("You must move to a neighboring space");	//And throw a non-neighbors exception if the move fails this way.
		}	
	}

}
