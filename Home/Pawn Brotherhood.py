def safe_pawns(pawns):
    letters = [' ', 'a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', ' ']
    safe_place = []
    for pawn in pawns:
        next_row = str(int(pawn[1])+1)
        safe_place += [letters[letters.index(pawn[0])+1] + next_row,
                       letters[letters.index(pawn[0])-1] + next_row]
    return len([x for x in pawns if x in safe_place])
