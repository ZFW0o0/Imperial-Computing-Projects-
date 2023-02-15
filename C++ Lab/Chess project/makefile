chess: ChessMain.o ChessPiece.o ChessBoard.o
	g++ ChessMain.o ChessPiece.o ChessBoard.o -o chess

ChessMain.o: ChessMain.cpp ChessPiece.h ChessBoard.h
	g++ -c -g -Wall ChessMain.cpp

ChessPiece.o: ChessPiece.cpp ChessPiece.h
	g++ -c -g -Wall ChessPiece.cpp

ChessBoard.o: ChessBoard.cpp ChessBoard.h ChessPiece.h
	g++ -c -g -Wall ChessBoard.cpp

clean:
	rm -f *.o chessboard
