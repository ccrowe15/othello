import Point #importing the point object for board


# Game class
# initiates game logic

class Game:
<<<<<<< HEAD
    
    self.white_score
    self.black_score 


=======
>>>>>>> 3db34acae8616b57b70590c6d7c9b8ce19fe5011
    board = [ 
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', 'W', 'B', '_', '_', '_'],
    ['_', '_', '_', 'B', 'W', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '_', '_', '_', '_'], ]
    
<<<<<<< HEAD
    self.game_result(white_placeable_locations, black_placeable_locations):
        is_full = true
        for x in range(7):
            for y in range (7):
                if (board[x][y] == '_'):
                    is_full = false
                    break
        
        #updateScores()
        if (is_full):
            if (white_score > black_score):
                return 1
            elif (white_score < black_score):
                return -1
            elif (white_score == black_score):
                return 0
        
        if (white_placeable_locations.length() == 0 and black_placeable_locations.length() == 0):
            if (white_score > black_score):
                return 1
            elif (white_score < black_score):
                return -1
            elif (white_score == black_score):
                return 0
        
        if (black_score == 0 or white_score == 0):
            if (white_score > black_score):
                return 1
            elif (white_score < black_score):
                return -1;
    
        return 3

        
=======
>>>>>>> 3db34acae8616b57b70590c6d7c9b8ce19fe5011


   
