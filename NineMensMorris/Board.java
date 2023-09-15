/* Conor Weiss
 * 3/1/23
 */

/**
 * Board class.  This class holds the playing pieces and players playing the Nine-men's-morris game.  
 */
		
public class Board {
	
	private Space A1;
	private Space A4;
	private Space A7;
	private Space B2;
	private Space B4;
	private Space B6;
	private Space C3;
	private Space C4;
	private Space C5;
	private Space D1;
	private Space D2;
	private Space D3;
	private Space D5;
	private Space D6;
	private Space D7;
	private Space E3;
	private Space E4;
	private Space E5;
	private Space F2;
	private Space F4;
	private Space F6;
	private Space G1;
	private Space G4;
	private Space G7;
	
	private Player player1;
	private Player player2;
	
	/**
	 * Constructor method: initializes spaces with correct neighbors, leaves players null.
	 */
	public Board() {
		A1 = new Space(SpaceType.CORNER);
		A4 = new Space(SpaceType.TEE);
		A7 = new Space(SpaceType.CORNER);
		B2 = new Space(SpaceType.CORNER);
		B4 = new Space(SpaceType.PLUS);
		B6 = new Space(SpaceType.CORNER);
		C3 = new Space(SpaceType.CORNER);
		C4 = new Space(SpaceType.TEE);
		C5 = new Space(SpaceType.CORNER);
		D1 = new Space(SpaceType.TEE);
		D2 = new Space(SpaceType.PLUS);
		D3 = new Space(SpaceType.TEE);
		D5 = new Space(SpaceType.TEE);
		D6 = new Space(SpaceType.PLUS);
		D7 = new Space(SpaceType.TEE);
		E3 = new Space(SpaceType.CORNER);
		E4 = new Space(SpaceType.TEE);
		E5 = new Space(SpaceType.CORNER);
		F2 = new Space(SpaceType.CORNER);
		F4 = new Space(SpaceType.PLUS);
		F6 = new Space(SpaceType.CORNER);
		G1 = new Space(SpaceType.CORNER);
		G4 = new Space(SpaceType.TEE);
		G7 = new Space(SpaceType.CORNER);
		
		@SuppressWarnings("unused")
		Space[] neighbors;
		A1.setNeighbors(neighbors = new Space[] {A4,D1});
		A4.setNeighbors(neighbors = new Space[] {A1,B4,A7});
		A7.setNeighbors(neighbors = new Space[] {A4,D7});
		B2.setNeighbors(neighbors = new Space[] {B4,D2});
		B4.setNeighbors(neighbors = new Space[] {B2,A4,B6,C4});
		B6.setNeighbors(neighbors = new Space[] {B4,D6});
		C3.setNeighbors(neighbors = new Space[] {C4,D3});
		C4.setNeighbors(neighbors = new Space[] {C3,B4,C5});
		C5.setNeighbors(neighbors = new Space[] {C4,D5});
		D1.setNeighbors(neighbors = new Space[] {A1,D2,G1});
		D2.setNeighbors(neighbors = new Space[] {B2,D1,F2,D3});
		D3.setNeighbors(neighbors = new Space[] {C3,D2,E3});
		D5.setNeighbors(neighbors = new Space[] {C5,D6,E5});
		D6.setNeighbors(neighbors = new Space[] {B6,D5,F6,D7});
		D7.setNeighbors(neighbors = new Space[] {A7,D6,G7});
		E3.setNeighbors(neighbors = new Space[] {D3,E4});
		E4.setNeighbors(neighbors = new Space[] {E3,F4,E5});
		E5.setNeighbors(neighbors = new Space[] {E4,D5});
		F2.setNeighbors(neighbors = new Space[] {D2,F4});
		F4.setNeighbors(neighbors = new Space[] {E4,F2,G4,F6});
		F6.setNeighbors(neighbors = new Space[] {D6,F4});
		G1.setNeighbors(neighbors = new Space[] {D1,G4});
		G4.setNeighbors(neighbors = new Space[] {G1,F4,G7});
		G7.setNeighbors(neighbors = new Space[] {G4,D7});
		
		player1 = null;
		player2 = null;
	}
	
	/**
	 * printBoard method
	 * Prints nine-men's-morris board using Spaces' toString to report on whether there's a piece (and whose piece it is) in the spaces.
	 */
	
	public void printBoard() {
		System.out.println("   1 2 3 4 5 6 7  ");
		System.out.println(" _________________");
		System.out.println("A| "+A1+"-----"+A4+"-----"+A7+" |");
		System.out.println(" | |     |     | |");
		System.out.println("B| | "+B2+"---"+B4+"---"+B6+" | |");
		System.out.println(" | | |   |   | | |");
		System.out.println("C| | | "+C3+"-"+C4+"-"+C5+" | | |");
		System.out.println(" | | | |   | | | |");
		System.out.println("D| "+D1+"-"+D2+"-"+D3+"   "+D5+"-"+D6+"-"+D7+" |");
		System.out.println(" | | | |   | | | |");
		System.out.println("E| | | "+E3+"-"+E4+"-"+E5+" | | |");
		System.out.println(" | | |   |   | | |");
		System.out.println("F| | "+F2+"---"+F4+"---"+F6+" | |");
		System.out.println(" | |     |     | |");
		System.out.println("G| "+G1+"-----"+G4+"-----"+G7+" |");
		System.out.println(" |_______________|");
	}
	
	/**
	 * playerJoin method
	 * Sets the given player to player 1 if available, or player 2 if not.  If both are full, throws exception.
	 * @param player
	 * @throws an exception if there are already two players at the board.
	 */
	
	public void playerJoin(Player player) throws Exception{
		if (this.player1 == null) {
			this.player1 = player;
			player1.setPieceSymbol("@");
		}
		else if (this.player2 == null) {
			this.player2 = player;
			player2.setPieceSymbol("X");
		}
		else {throw new Exception("This board is already full.");}
	}
	
	/**
	 * toString override. Prints the board and players.
	 */
	
	@Override
	public String toString() {
		if(player1 == null && player2 == null) {
			return("Empty board.");
		}
		else if (player2 == null) {
		return(player1+ "'s board");
		}
		else {return player1 + " and " + player2 + "'s board";}
		
	}
	
	/**
	 * findSpace method.  Used by players to specify where they are placing pieces.
	 * @param spaceName - a string of the form "L#" matching the space variable names.
	 * @return the space matching the string sent.
	 * @throws an exception if the spaceName string does not match one of the space variable names.
	 */
	
	public Space findSpace(String spaceName) throws Exception {
		if (spaceName.equals("A1")) {
			return A1;
		}
		else if (spaceName.equals("A4")) {
			return A4;
		}
		else if (spaceName.equals("A7")) {
			return A7;
		}
		else if (spaceName.equals("B2")) {
			return B2;
		}
		else if (spaceName.equals("B4")) {
			return B4;
		}
		else if (spaceName.equals("B6")) {
			return B6;
		}
		else if (spaceName.equals("C3")) {
			return C3;
		}
		else if (spaceName.equals("C4")) {
			return C4;
		}
		else if (spaceName.equals("C5")) {
			return C5;
		}
		else if (spaceName.equals("D1")) {
			return D1;
		}
		else if (spaceName.equals("D2")) {
			return D2;
		}
		else if (spaceName.equals("D3")) {
			return D3;
		}
		else if (spaceName.equals("D5")) {
			return D5;
		}
		else if (spaceName.equals("D6")) {
			return D6;
		}
		else if (spaceName.equals("D7")) {
			return D7;
		}
		else if (spaceName.equals("E3")) {
			return E3;
		}
		else if (spaceName.equals("E4")) {
			return E4;
		}
		else if (spaceName.equals("E5")) {
			return E5;
		}
		else if (spaceName.equals("F2")) {
			return F2;
		}
		else if (spaceName.equals("F4")) {
			return F4;
		}
		else if (spaceName.equals("F6")) {
			return F6;
		}
		else if (spaceName.equals("G1")) {
			return G1;
		}
		else if (spaceName.equals("G4")) {
			return G4;
		}
		else if (spaceName.equals("G7")) {
			return G7;
		}
		else {
			System.out.println("There is no space with that label on this board.");
			throw new Exception("There is no space with that label on this board.");}
	}
	
	
	/**
	 * getOpponent method
	 * @param the player calling the method
	 * @return the player who does not call the method.
	 * @throws an exception if the player calls the method and has no opponent yet.
	 */
	
	public Player getOpponent(Player player) throws Exception{
		if (player == player1) {return player2;}
		else if (player == player2) {return player1;}
		else {
			System.out.println("No opponent found");
			throw new Exception("No opponent found");
		}
	}

}
