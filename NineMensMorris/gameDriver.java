import java.util.Scanner;

/* Conor Weiss
 * 3/3/23
 */

/**
 * The gameDriver program allows two players (or 1 player and a very bad AI) to play Nine Men's Morris
 * @author Conor
 *
 */
public class gameDriver {
	
	public static void main(String[] args) {
		Board board = new Board();
		Player player1;
		Player player2;
		Player activePlayer;
		int playerTurn = 0;
		int playerNum = 0;
		
		Scanner userIn = new Scanner(System.in);
		
		while(playerNum != 1 && playerNum != 2) {
			System.out.println("How many human players? (1 or 2)");
			playerNum = userIn.nextInt();
		}
		
		userIn.reset();
	
		System.out.println("Player 1's name?");
		player1 = new User(userIn.next());
		activePlayer = player1;
		
		userIn.reset();
		
		if (playerNum == 2) {
			System.out.println("Player 2's name?");
			player2 = new User(userIn.next());
			userIn.reset();
		}
		else {
			player2 = new DumbAI();	//Replace with an AI
		}
		
		player1.joinBoard(board);
		player2.joinBoard(board);
		
		//This loop will run until one player wins.  The "isWinning()" method counts how many pieces the players have removed of their opponents.
		//You win when your opponent only has two pieces left/you have removed 7.
		while (!player1.isWinning() && !player2.isWinning()) {
			
			//Swap active player
			if (playerTurn == 0) {
				activePlayer = player1;
			}
			if (playerTurn == 1) {
				activePlayer = player2;
			}
			
			//update board
			board.printBoard();
			
			//Tell the player who's playing.
			System.out.println(activePlayer + "'s Turn!");
			
			//Let the AI handle things if it's an AI.
			if (activePlayer instanceof AIDriven) {
				((AIDriven) activePlayer).takeAction();
				try {
					if (board.getOpponent(activePlayer).isWinning()){
						activePlayer = board.getOpponent(activePlayer);
					}
				}
				catch (Exception e) {}
			}
			
			
			if(activePlayer instanceof User) {
				//After all 9 pieces have been placed, you move pieces.
				//This is placed first because the placePiece increments pieceCount.
				if (activePlayer.getPieceCount() == 9) {
					boolean success = false;
					while (!success) {
						System.out.println("Which space will you move a piece from?");
						System.out.println("(Spaces take the form \"A1\", \"A4\", and so on.)");
						
						System.out.println("(If you have no valid moves, you may forfeit. Type \"quit\" to do so.)");
						String startSpace = userIn.next();
						if (startSpace.equals("quit")) {
							try {
								activePlayer = board.getOpponent(activePlayer);
								activePlayer.win();
								break;
							}
							catch (Exception e) {}
						}
						
						System.out.println("Where will you move the piece too?");
						System.out.println("It must be an adjacent space.");
						
						String playerMove = userIn.next();
						
						try {
							activePlayer.movePiece(board.findSpace(startSpace), board.findSpace(playerMove));
							success = true;
						}
						catch (Exception e) {
							System.out.println(e);
							success = false;}
					}
				}
			
				//You must place all 9 of your pieces before making any moves.
				if (activePlayer.getPieceCount() < 9){
					boolean success = false;
					while (!success) {
						System.out.println("Where will you place a piece?");
						System.out.println("(Spaces take the form \"A1\", \"A4\", and so on.)");
						try {
							String playerMove = userIn.next();
							activePlayer.placePiece(board.findSpace(playerMove));
							success = true;
						}
						catch (Exception e) {
							System.out.println(e);
							success = false;
						}
					}	
				}
			
				//If you've made a mill (three pieces in a row), remove one of your opponent's pieces.
				while (activePlayer.millCount() > 0) {
					board.printBoard();
					boolean success = false;
					while (!success) {
						System.out.println("You've made a mill! Which space will you remove a piece from?");
						System.out.println("You can't remove a piece that's in a mill unless you have no other option.");
						String playerMove = userIn.next();
						try {
							activePlayer.millRemove(board.findSpace(playerMove));
							success = true;
						}
						catch (Exception e) {
							System.out.println(e);
							success = false;}
					}
				}
			}
			//finish the turn and swap.  This method is preferable to using the .opponent() method for board because the method may throw an exception.
			playerTurn = (playerTurn + 1) % 2;
		}
		System.out.println(activePlayer + " wins!");
		userIn.close();
	}
}