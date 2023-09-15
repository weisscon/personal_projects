/* Conor Weiss
 * 3/1/23
 */

/**
 * Mill class.  Mills are formed when three spaces in a line have matching symbols.
 * Mills hold their spaces within them, and are attached to the spaces.
 * @author Conor
 *
 */
public class Mill {
	
	private Space[] spaces = new Space[3];
	
	/**
	 * Constructor method: Mills are made from three spaces.  
	 * Associates this mill with the spaces, and associates the spaces with the mills.
	 * @param space1 - first space in the mill
	 * @param space2 - second space in the mill
	 * @param space3 - third space in the mill
	 */
	
	public Mill(Space space1, Space space2, Space space3) {
		spaces[0] = space1;
		spaces[1] = space2;
		spaces[2] = space3;
		
		for (int i = 0; i < 3; i++) {
			try{
				spaces[i].addMill(this);
			}
			catch(Exception e) {
				System.out.println(e);
			}
		}
	}
	
	/**
	 * getSpaces method.  Returns the spaces array
	 * @return the spacesarray
	 */
	
	public Space[] getSpaces() {
		return spaces;
	}

}
