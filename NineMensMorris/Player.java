/* Conor Weiss
 * 3/4/23
 */

/**
 * Player abstract class.  All objects which can play the game will inherit from this object.
 * @author Conor
 *
 */

public abstract class Player {
	
	private int pieceCount = 0;
	private Piece[] pieces = new Piece[9];
	private Board board;
	private String name;
	private String pieceSymbol;
	private int millsMade;
	private int piecesRemoved = 0;
	private static int playerCount = 0;
	
	/**
	 * Constructor method.  
	 * @param name - player's name
	 */
	
	public Player(String name){
		String nameString = (String)(name + playerCount);
		playerCount++;
		this.name = nameString;
	}
	
	
	/**
	 * JoinBoard method: the player attempts to join a game board.  If successful, they are attached to the board, and the board records them.
	 * @param board
	 */
	public void joinBoard(Board board) {
		try{
			board.playerJoin(this);
			this.board = board;
		}
		catch(Exception e) {
			System.out.println(e);
		}
	}
	
	/**
	 * getBoard method: returns the player's board.
	 * @return the player's board.
	 */
	
	public Board getBoard() {
		return this.board;
	}
	
	/**
	 * toString override: prints the player's name.
	 */
	
	@Override
	public String toString() {
		return this.name;
	}
	
	/**
	 * setPieceSymbol: simple setter method to set the symbol for player's pieces.
	 * @param the symbol that will be used when the board is printed.
	 */
	
	public void setPieceSymbol(String symbol) {
		this.pieceSymbol = symbol;
	}
	
	/**
	 * getPieceCount: simple getter to return the player's piece count.  Used to determine which moves they can make by the driver.
	 * @return the number of pieces remaining to place.
	 */
	
	public int getPieceCount() {
		return pieceCount;
	}
	
	/**
	 * getPieces: returns the pieces array
	 * @return the player's pieces array
	 */
	
	public Piece[] getPieces() {
		return pieces;
	}
	
	/**
	 * millCount: reports millsMade.
	 * @returns millsMade
	 */
	
	public int millCount() {
		return millsMade;
	}
	
	/**
	 * placePiece: places a piece on the board.  Throws an exception if called when pieceCount is 9 or higher.
	 * If mills are made after placing a piece, this is recorded in millsMade.
	 * @param space - the space where the piece will be placed
	 * @throws an exception if the player has no more pieces to place (driver should not allow player to place pieces when out.)
	 */
	
	public void placePiece(Space space) throws Exception {
		if (pieceCount < 9) {
				Piece piece = new Piece(pieceSymbol);		//Make the piece
				millsMade = piece.place(space);				//Place the piece
				pieces[pieceCount] = piece;					//Record the piece in your pieces array
				pieceCount++;								//up piece count
		}
		else {
			System.out.println("Out of pieces");			//Only have 9 pieces to place.
			new Exception("Out of pieces.");
		}
	}
	
	/**
	 * millRemove: controlled by driver, but when a player makes a mill, they remove one of their opponent's pieces.
	 * They must choose a piece that is not in a mill unless all pieces are in a mill
	 * @param space: the space that the piece will be removed from
	 * @throws an exception if the player has not made a mill, tries to remove from an empty space, or tries to remove their own piece.
	 */
	
	public void millRemove(Space space) throws Exception {
		if (millsMade > 0 && space.getPiece() != null) {					//Only do this if the player has made a mill and there's a piece here to remove.
				Player opponent = this.board.getOpponent(this);				//get opponent
				Piece[] opponentPieces = opponent.getPieces();				//get their piece array
				boolean allMills = true;									//assume all pieces are in a mill
				for (int i = 0; i < opponent.getPieceCount(); i++) {
					if (opponentPieces[i] != null) {						//if the piece hasn't yet been removed.
						if (!opponentPieces[i].getSpace().millReport()) {	//check each piece to see if it is in a mill.  If it isn't,
							allMills = false;								//not all pieces are in the mill...
							break;											//and you can stop.
						}
					}
				}
				if ((!space.millReport() || allMills) && !(space.getPiece().toString() == pieceSymbol)) {
																			//if either this piece isn't in a mill OR all pieces were in mills AND this isn't your piece.
					for (int i = 0; i < opponent.getPieceCount(); i++) {	//check through the opponent's pieces.  Remove this piece from among them.
						if (opponentPieces[i] != null) {
							if (opponentPieces[i] == space.getPiece()) {
								opponentPieces[i] = null;
							}
						}
					}
				
					space.setPiece(null);										//Set the piece in this space to null (i.e. remove it.)
					space.millMoveUpdate();										//Remove mills destroyed because this piece was removed.
					millsMade--;												//You've removed a piece because you made a mill.
					piecesRemoved++;											//track this for win condition.
					}
				else {
					if (space.millReport()) {System.out.println("You cannot remove a piece that is in a mill unless there is no other option.");}
					throw new Exception("Mill removal failed.");
				}
			}
		else {
			if (millsMade <= 0) {System.out.println("Attempted to remove a piece via mill when no mill was made.");}
			if (space.getPiece() == null) {System.out.println("No piece to remove at this space");}
			if (space.getPiece().toString() == pieceSymbol) {System.out.println("You cannot remove your own piece");}
			throw new Exception("Mill removal failed.");
		}
	}
	
	/**
	 * movePiece method.  Moves a piece from it's space to a neighboring space.
	 * Throws exceptions if you're trying to move a piece that's not yours or from an empty space.
	 * Adjacency and target space's emptiness handled in Piece.
	 * @param space1 - the space the piece is in
	 * @param space2 - the space the piece is moving to.
	 * @throws Exception
	 */
	
	public void movePiece(Space space1, Space space2) throws Exception {	
		if (pieceCount != 9) {
			System.out.println("You have not placed enough pieces to make a move");
			throw new Exception("Move attempted before 9 pieces placed.");
		}
		if (space1.toString() == pieceSymbol) {
				millsMade = space1.getPiece().move(space2);
		}
		else {
			System.out.println("Can't move an opponent's piece or from an empty space");
			throw new Exception("Can't move an opponent's piece or from an empty space.");
		}
	}
	
	/**
	 * isWinning: counts how many pieces you've removed through mills.
	 * A player wins if they've removed 7 of their opponent's pieces.
	 * @return a boolean: false if not winning yet, true if won.
	 */
	
	public boolean isWinning() {
		return (piecesRemoved == 7);
	}
	
	/**
	 * win: can be used to set the player to win.
	 */
	
	public void win() {
		piecesRemoved = 7;
	}
	
	public static int getPlayerCount() {
		return playerCount;
	}
}
