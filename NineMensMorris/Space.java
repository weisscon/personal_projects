/* Conor Weiss
 * 3/1/23
 */

/**
 *Space class.  Players play pieces in spaces.
 *
 */
public class Space {
	
	private Space[] neighbors;
	private SpaceType type = null;
	private Piece piece = null;
	private Mill[] mills = new Mill[2];
	
	/**
	 * Constructor method: sets the type of Space.
	 * @param type - type of space
	 */
	
	public Space(SpaceType type) {
		this.type = type;
		if (type == SpaceType.CORNER) {neighbors = new Space[2];}
		else if (type == SpaceType.TEE) {neighbors = new Space[3];}
		else if (type == SpaceType.PLUS) {neighbors = new Space[4];}
	}
	
	/**
	 * toString override.
	 * Prints the space by printing blank if no piece is on it, or the piece if it is.
	 */
	public String toString() {
		if (piece == null) {
			return "o";
		}
		else {
			return piece.toString(); 
		}
	}

	/**
	 * setNeighbors method: sets the neighbors of a space.  read in order, so neighbors that are two spaces away from each other (e.g. indices 0 and 2) are in the same line.
	 * @param a Space[] array which will be read into this space's neighbor array
	 * @throws IllegalArgumentException if the array sizes don't match.
	 */
	public void setNeighbors(Space[] neighbors) {
		if (this.neighbors.length == neighbors.length) {
			for (int i =0; i < neighbors.length; i++) {
				this.neighbors[i] = neighbors[i];
			}
		}
		else {throw new IllegalArgumentException("Neighbor array is incorrect size.");}
	}
	
	/**
	 * getNeighbors
	 * @return the neighbors array.
	 */
	public Space[] getNeighbors() {
		//for (int i = 0; i < neighbors.length; i++) {
		//	System.out.println(neighbors[i]);
		//}
		return neighbors;
	}
	
	/**
	 * setPiece method.  Invoked by the Piece object when it is placed here.
	 * @param piece: the piece to to be placed
	 */
	
	public void setPiece(Piece piece) {
		this.piece = piece;
	}
	
	/**
	 * getPiece method.  Returns the piece in the space.  
	 * Used to determine if the space is empty or what mills it may form.
	 * @return the piece in this space.
	 */
	
	public Piece getPiece() {
		return piece;
	}
	
	/**
	 * millArray method: simple getter method for the mills array.
	 * @return the mills array
	 */
	
	public Mill[] millArray() {
		return mills;
	}
	
	/**
	 * millCheck method.  Based on the type of space, checks the connected spaces for pieces with the same symbol.  
	 * If successful, creates a mill and assigns all pieces to it.
	 * @return the number of mills made.
	 */
	
	public int millCheck() {
		int millnum = 0;
		if (piece != null) {																			//If there is a piece here:
			for(int i = 0; i < 2; i++) {																//Only need to check the first two neighbors.
				if (neighbors[i].toString() == this.toString()) {										//check neighbors for matching symbol.
																										//If so, select from these options:
					
					if (type == SpaceType.CORNER || (type == SpaceType.TEE && i == 1)) {					//Either a corner space, or going down the long leg of a tee:
						for (int j = 0; j < neighbors[i].neighbors.length; j++) {
							if (neighbors[i].neighbors[j] == this) {											//check neighbor's neighbors for this piece.
								int k = 0;
								if (j <= 1) {k = j + 2;}															//add or subtract 2 from this space's address
								if (j > 1) {k = j - 2;}																//depending on whether on upper or lower end of array.
								if (neighbors[i].neighbors[k].toString() == this.toString()) {						//if all three match
									@SuppressWarnings("unused")
									Mill mill = new Mill(this,neighbors[i],neighbors[i].neighbors[k]);				//make a new Mill.
									millnum++;
								}
							}
						}
					}
					else if (type == SpaceType.PLUS || (type == SpaceType.TEE && i == 0)) {					//Either a plus space, or the cross of the tee:
						if (neighbors[i+2].toString() == this.toString()) {										//Check space on opposite side from match
							@SuppressWarnings("unused")
							Mill mill = new Mill(this, neighbors[i],neighbors[i+2]);							//if all three match, make a new Mill.
							millnum++;
						}
					}
				}
			}
		}
		return millnum;
	}
	
	/**
	 * addMill method, which is used by the Mill object to associate this space with the mill.
	 * @param mill - the mill to be associated
	 * @throws Exception - throws an exception if two mills already associated with this object.  (There should never be more than 2.  If there are, I have messed up.)
	 */
	
	public void addMill(Mill mill) throws Exception{
		if (mills[0] == null) {mills[0] = mill;}
		else if (mills[1] == null) {mills[1] = mill;}
		else {
			System.out.println("You've messed up your mill processes!");
			throw new Exception ("You've messed up your mill processes!");}
	}
	
	/**
	 * millReport method.  Reports if there is a mill involving this space.
	 * @return true if there is a mill in the space, false if there is not.
	 */
	
	public boolean millReport() {
		boolean report = false;
		for (Mill i : mills) {
			if (i != null) {
				report = true;
			}
		}
		return report;
	}
	
	/**
	 * millMoveUpdate: if the piece in this space is moved, gets rid of any mills in this space.
	 */
	
	public void millMoveUpdate() {		
		for (Mill mill : this.mills) {									//Check each mill in the mill array
			if (mill != null) {											//if the mill is not null
				for (Space millComponent : mill.getSpaces()) {			//go through each space in the mill's space array
					for (int i = 0; i < millComponent.millArray().length; i++) {	//in each space, check each mill in the mill array
						if (millComponent.millArray()[i] == mill) {						//when you find the mill in its spaces' mill arrays
							millComponent.millArray()[i] = null;							//delete the mill from the mill's spaces' mill arrays
						}
					}
				}
			}
		}
	}
}