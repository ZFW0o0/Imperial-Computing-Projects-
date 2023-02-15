#include <iostream>
#include <cstdio>
#include "sudoku.h"

using namespace std;

int main() {

  char board[9][9];

  /* This section illustrates the use of the pre-supplied helper functions. */
  cout << "============= Pre-supplied functions =============\n\n";

  cout << "Calling load_board():\n";
  load_board("easy.dat", board);

  cout << '\n';
	cout << "Displaying Sudoku board with display_board():\n";
  display_board(board);
  cout << "Done!\n\n";

  cout << "=================== Question 1 ===================\n\n";

  load_board("easy.dat", board);
  cout << "Board is ";
  if (!is_complete(board)) {
    cout << "NOT ";
  }
  cout << "complete.\n\n";

  load_board("easy-solution.dat", board);
  cout << "Board is ";
  if (!is_complete(board)) {
    cout << "NOT ";
  }
  cout << "complete.\n\n";

  cout << "=================== Question 2 ===================\n\n";

  load_board("easy.dat", board);

  // Should be OK
  cout << "Putting '1' into I8 is ";
  if (!make_move("I8", '1', board)) {
    cout << "NOT ";
  }
  cout << "a valid move. The board is:\n";
  display_board(board);
  cout << endl;

  // write more tests
  // should be invalid as Z8 is an invalid position
  load_board("easy.dat", board);
  cout << "Putting '1' into Z8 is ";
  if (!make_move("Z8", '1', board)) {
    cout << "NOT ";
  }
  cout << "a valid move.\n\n";

  // should be invalid as '0' can not be filled into a sudoku board
  load_board("easy.dat", board);
  cout << "Putting '0' into I8 is ";
  if (!make_move("I8", '0', board)) {
    cout << "NOT ";
  }
  cout << "a valid move.\n\n";
 
  cout << "=================== Question 3 ===================\n\n";

  load_board("easy.dat", board);
  if (save_board("easy-copy.dat", board)) {
    cout << "Save board to 'easy-copy.dat' successful.\n";
  } else {
    cout << "Save board failed.\n";
  }
  cout << '\n';

  cout << "=================== Question 4 ===================\n\n";

  
  load_board("easy.dat", board);
  if (solve_board(board)) {
    cout << "The 'easy' board has a solution:\n";                                 
    display_board(board);
  } else {
    cout << "A solution cannot be found.\n";
  }
  cout << '\n';

  load_board("medium.dat", board);
  if (solve_board(board)) {
    cout << "The 'medium' board has a solution:\n"; 
    display_board(board);
  } else {
    cout << "A solution cannot be found.\n";
  }
  cout << '\n';

  // write more tests 

  cout << "=================== Question 5 ===================\n\n";

  // write more tests
  // solve mystery1, display solved board if solvable and report failure if not solvable. 
  load_board("mystery1.dat", board);
  if (solve_board(board))
  {
    cout << "The 'mystery1' board has a solution:\n";
    display_board(board);
    cout << endl;
  }
  else {
    cout << "A solution cannot be found for 'mystery1'.\n\n";
  }

  // solve mystery2, display solved board if solvable and report failure if not solvable. 
  load_board("mystery2.dat", board);
  if (solve_board(board))
  {
    cout << "The 'mystery2' board has a solution:\n";
    display_board(board);
    cout << endl;
  }
  else {
    cout << "A solution cannot be found for 'mystery2'.\n\n";
  }

  // solve mystery3, display solved board if solvable and report failure if not solvable
  load_board("mystery3.dat", board);
  if (solve_board(board))
  {
    cout << "The 'mystery3' board has a solution:\n";
    display_board(board);
    cout << endl; 
  }
  else {
    cout << "A solution cannot be found for 'mystery3'.\n\n";
  }

 
  return 0;
}
