
import numpy as np
VECTOR = {
    'd':(1,0),
    'r':(0,1)
    }  


# Scrabble letter scores: Each key represents a letter, and the value represents its score.
LETTER_SCORES = {
    'A': 1,  # Score for the letter A is 1 point.
    'B': 3,  # Score for the letter B is 3 points.
    'C': 3,  # Score for the letter C is 3 points.
    'D': 2,  # Score for the letter D is 2 points.
    'E': 1,  # Score for the letter E is 1 point.
    'F': 4,  # Score for the letter F is 4 points.
    'G': 2,  # Score for the letter G is 2 points.
    'H': 4,  # Score for the letter H is 4 points.
    'I': 1,  # Score for the letter I is 1 point.
    'J': 8,  # Score for the letter J is 8 points.
    'K': 5,  # Score for the letter K is 5 points.
    'L': 1,  # Score for the letter L is 1 point.
    'M': 3,  # Score for the letter M is 3 points.
    'N': 1,  # Score for the letter N is 1 point.
    'O': 1,  # Score for the letter O is 1 point.
    'P': 3,  # Score for the letter P is 3 points.
    'Q': 10, # Score for the letter Q is 10 points.
    'R': 1,  # Score for the letter R is 1 point.
    'S': 1,  # Score for the letter S is 1 point.
    'T': 1,  # Score for the letter T is 1 point.
    'U': 1,  # Score for the letter U is 1 point.
    'V': 4,  # Score for the letter V is 4 points.
    'W': 4,  # Score for the letter W is 4 points.
    'X': 8,  # Score for the letter X is 8 points.
    'Y': 4,  # Score for the letter Y is 4 points.
    'Z': 10, # Score for the letter Z is 10 points.
}


def boardMaker():
    '''
    Return: a 15x15 array modeling a Scrabble board.
    Parameter: none
    '''
    # Define color codes for special tile types.
    YELLOW_BG = '\033[1;33m'  # Triple word score (3W)
    GREY_BG = '\033[2;37m'    # Double word score (2W)
    PURPLE_BG = '\033[1;35m'  # Triple letter score (3L)
    BLUE_BG = '\033[1;34m'    # Double letter score (2L)
    RESET_COLOR = '\033[0;0m' # Reset color code
    
    # Create the Scrabble board as a 15x15 array with special tile types.
    board = np.array([
        [YELLOW_BG + '3W' + RESET_COLOR, ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', YELLOW_BG + '3W' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', YELLOW_BG + '3W' + RESET_COLOR],
        [' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' '],
        [' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' '],
        [BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', BLUE_BG + '2L' + RESET_COLOR],
        [' ', ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', ' '],
        [' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' '],
        [' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' '],
        [YELLOW_BG + '3W' + RESET_COLOR, ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', '**', ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', YELLOW_BG + '3W' + RESET_COLOR],
        [' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' '],
        [' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' '],
        [' ', ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', ' '],
        [BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', BLUE_BG + '2L' + RESET_COLOR],
        [' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' '],
        [' ', GREY_BG + '2W' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', PURPLE_BG + '3L' + RESET_COLOR, ' ', ' ', ' ', GREY_BG + '2W' + RESET_COLOR, ' '],
        [YELLOW_BG + '3W' + RESET_COLOR, ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', ' ', YELLOW_BG + '3W' + RESET_COLOR, ' ', ' ', ' ', BLUE_BG + '2L' + RESET_COLOR, ' ', ' ', YELLOW_BG + '3W' + RESET_COLOR]
    ])
    
    return board

def scrabbleDictionary():
    '''
    Get the Scrabble dictionary as a list of words.
    Parameter: None
    Returns:
        myDict (list): The Scrabble dictionary as a list of words in uppercase
    '''
    myDict = set()
    with open("sowpods.txt") as myFile:
        for line in myFile:
            word = line.strip().upper()
            myDict.add(word)
    return myDict

DICTIONARY = scrabbleDictionary()

#GLOBAL VARIABLES
#==============================================================================
#CLASSES

class board:
    def __init__(self, board):
        print('Welcome to the game of Scrabble. Your first move is at coordinate (7,7)')
        self.board = board.copy()
        self.lastBoard = board.copy()
        
    def boardPrint(self):
        '''
        Print the Scrabble board to the console.
        Parameter:
            board (list): a 15x15 array representing the Scrabble board
        '''
        def spaceCalc(string):
            '''
            Calculate the number of spaces needed to align the content properly.
            Parameter:
                string (str): The content to calculate spaces for.
            Returns:
                space (int): Number of spaces needed.
            '''
            if len(str(string)) == 1:
                space = 3
            elif len(str(string)) == 0:
                space = 4
            else:
                space = 2
            return space
    
        # Print the top axis
        print('    ', end='')
        for i in range(len(self.board)):
            print('   ' + '{}'.format(i) + spaceCalc(i) * ' ', end='')
        print('')
        print('    ', end='')
        print(106 * '=')
    
        # Print the board
        for i in range(len(self.board)):
            print((spaceCalc(i) - 2) * ' ' + '{}'.format(i) + '  ', end='')
            for j in range(len(self.board)):
                print('|  ' + self.board[i, j] + spaceCalc(self.board[i, j]) * ' ', end='')
            print('|')
            print('    ', end='')
            print(106 * '=')
    
        # Example usage:
        # Assuming you have created the board using the boardMaker() function:
        # my_board = boardMaker()
        # boardPrint(my_board)
        
    
    
    
    
    
    
    
    def move(self):
        '''
        Perform a move in the Scrabble board after validating the user's input.
        Parameter: self
        '''
        def inputCoords(axis):
            '''
            Get a valid coordinate on the board (not necessarily an available coordinate).
            Parameter:
                axis (str): The axis (i.e., 'row' or 'column')
            Returns:
                coord (int): The valid coordinate on the board
            '''
            valid = False
            while not valid:
                userInput = input(f'Input the {axis} number: ')
                if userInput.isdigit():
                    coord = int(userInput)
                    if 0 <= coord <= 14:
                        valid = True
                    else:
                        print('That is an invalid input. The number must be between 0 and 14.')
                else:
                    print('That is an invalid input. Make sure it is a number!')
            return coord
    
        def inputDirection():
            '''
            Get a valid direction players can place letters (d for "down" or r for "right").
            Parameter: None
            Returns:
                direction (str): The valid direction (d for "down" or r for "right")
            '''
            valid = False
            while not valid:
                userInput = input('Input a direction (d for "down" or r for "right"): ')
                if userInput.isalpha():
                    if userInput in ['r', 'd']:
                        valid = True
                    else:
                        print('That is an invalid input. Make sure it is "r" or "d"!')
                else:
                    print('That is an invalid input. Make sure it is "r" or "d"!')
            return userInput
    
        def inputWord():
            '''
            Get a valid word in Scrabble and ask the user to confirm if it's correct.
            If confirmed, update the dictionary with the new word.
            Parameter: None
            Returns:
                word (str): The valid word in uppercase
            '''
            valid = False
            while not valid:
                userInput = input('Enter your word: ')
                if userInput.isalpha():
                    word = userInput.upper()
                    if word in DICTIONARY:
                        print(f"The word '{word}' is a valid word in Scrabble. ")
                        valid = True
                    else:
                        confirm = input(f"Is '{word}' a valid word in Scrabble? (yes/no): ").lower()
                        if confirm == 'yes':
                            # Update the dictionary with the new word
                            DICTIONARY.add(word)
                            valid = True
                        else:
                            print('Please enter a different word.')
                else:
                    print('That is an invalid input. Make sure you are typing letters!')
            return word
    
        def vectorCheck(playedCoords):
            '''
            Check if the word fits within the dimensions of the board.
            Parameter:
                playedCoords (list): A list of tuples of the form (#, #) representing coordinates
            Returns:
                valid (bool): True if the word fits within the board dimensions, False otherwise
            '''
            return all(0 <= j <= 14 for i in playedCoords for j in i)
    
        def pCoords(row, col, direction, word):
            '''
            Get a list of coordinates for the player's word placement.
            Parameters:
                row (int): Row number
                col (int): Column number
                direction (str): 'r' (right) or 'd' (down)
                word (str): The word the user would like to play
            Returns:
                playedCoords (list): A list of coordinates (tuples of the form (#, #)) for the word placement
            '''
            multipliers = {
                'd': (1, 0),
                'r': (0, 1)
            }
    
            x, y = multipliers[direction]
            length = len(word)
    
            playedCoords = [(row + x*i, col + y*i) for i in range(length)]
            return playedCoords
    
        # Loop until a valid move is played
        while True:
            row = inputCoords('row')
            col = inputCoords('col')
            direction = inputDirection()
            word = inputWord()
            proposedCoords = pCoords(row, col, direction, word)
    
            if vectorCheck(proposedCoords):
                proposed = self.board.copy()
                for i in range(len(word)):
                    proposed[proposedCoords[i]] = word[i]
    
                if self.validMove(proposed, proposedCoords):
                    # Update the board and print it
                    self.lastBoard = self.board
                    self.board = proposed
                    self.boardPrint()
                    break
                else:
                    self.boardPrint()
                    print('Sorry, that is not a valid entry. Please try again.')
            else:
                self.boardPrint()
                print('Sorry, that was an invalid move. Please try again.')
        
        
        
        
        
        
    def validMove(self, proposed, playedCoords):
        '''
        Check if the player makes a valid move.
        Parameters:
            proposed (numpy.ndarray): The proposed board layout
            playedCoords (list): A list of tuples of the form (#, #) representing the player's move
        Returns:
            valid (bool): True if the player makes a valid move, False otherwise
        '''
        existing = self.board.copy()
        proposed = proposed.copy()
    
        def boardProcessor(board):
            '''Return a board without any letter or word multipliers.
            Parameters:
                board (numpy.ndarray): The board
            Returns:
                numpy.ndarray: The processed board
            '''
            return np.where(np.char.str_len(board) > 1, ' ', board)
    
        def usedCoords(board):
            '''Return a list of all used coordinates on the board.
            Parameters:
                board (numpy.ndarray): The board
            Returns:
                list: A list of tuples of the form (#, #) representing used coordinates
            '''
            return {(i, j) for i in range(len(board)) for j in range(len(board)) if board[i, j] != ' ' and len(board[i, j]) == 1}
    
        def coordCheck(existing, proposed):
            '''
            Check if there are no changes in existing letters on the proposed board.
            Parameters:
                existing (numpy.ndarray): The current board
                proposed (numpy.ndarray): The proposed board
            Returns:
                valid (bool): True if there are no changes in played spaces, False otherwise
            '''
            for i in range(len(existing)):
                for j in range(len(existing)):
                    if existing[i, j] != ' ' and existing[i, j] != proposed[i, j]:
                        return False
            return True

    
        def wordCheck(proposed):
            '''Check if all of the words are valid in all of the rows.
            Parameters:
                proposed (numpy.ndarray): The proposed board
            Returns:
                bool: True if all words are valid in all of the rows, False otherwise
            '''
            row = proposed
            col = proposed.transpose()
    
            def rowCheck(row):
                '''Check if all words in a row are valid (excluding singular letters).
                Parameters:
                    row (numpy.ndarray): A list of letters in the row
                Returns:
                    bool: True if all words in the row are valid, False otherwise
                '''
                words = ''.join(row).strip().split()
                return all(len(word) == 1 or word in DICTIONARY for word in words)
    
            return all(rowCheck(row[i]) and rowCheck(col[i]) for i in range(len(proposed)))
    
        def connectionCheck(existing, playedCoords):
            '''Check if new letters added are connected to existing letters.
            Parameters:
                existing (numpy.ndarray): The current board
                playedCoords (list): The coordinates played by the user
            Returns:
                bool: True if new letters are connected to existing letters, False otherwise
            '''
    
            def possiblePlays(coord):
                '''Return the possible paths from a used coordinate that can be played.
                Parameters:
                    coord (tuple): A tuple in the form (#, #)
                Returns:
                    list: A list of tuples of the form (#, #) representing possible paths
                '''
                up = (coord[0] - 1, coord[1])
                left = (coord[0], coord[1] - 1)
                down = (coord[0] + 1, coord[1])
                right = (coord[0], coord[1] + 1)
    
                return {up, left, down, right}
    
            used_existing = usedCoords(existing)
            
            all_plays = {play for i in used_existing for play in possiblePlays(i)}
            
            return any(play in all_plays for play in playedCoords)
    
        
        
    
        existing = boardProcessor(existing)
        proposed = boardProcessor(proposed)
        
        valid = coordCheck(existing, proposed) and wordCheck(proposed)
        if len(usedCoords(existing)) > 0:
            valid = connectionCheck(existing, playedCoords) and valid    

        return valid
    
    
    
    
    
    
    
    
    
    def pointCalculator(self, proposed, move):
        '''
        Calculates the points earned by a certain move on the Scrabble board. The function takes a proposed move and a flag 'move', indicating whether it should calculate points from the last move or the best move.

        Parameters:
            self: The instance of the Scrabble board class.
            proposed: The proposed move for optimization (a 2D list representing the board).
            move: A boolean flag - True if it calculates points from the last move, False if it calculates the best move.
        
        Returns:
            totalScore (int): The total score earned by the given move on the board.
        '''
        # Preparing boards based on the 'move' parameter
        # 'board1' is the previous board if 'move' is True, otherwise it is the current board
        # 'board2' is the current board if 'move' is True, otherwise it is the proposed board
        if move:
            board1 = self.lastBoard
            board2 = self.board
        else:
            board1 = self.board
            board2 = proposed
    
        def wordFinderBoard(board, axisType):
            '''
            Return a list of words and their respective coordinates in proper format.
    
            Parameters:
                board (list): The playing board as a list of rows or columns.
                axisType (str): 'row' or 'col' to indicate whether the board is processed by rows or columns.
    
            Returns:
                words (list): A list of words in the form [[('H', (7, 7)), ('I', (7, 8))], [('H', (7, 7)), ('I', (8, 7))], ...]
            '''
    
            def wordFinderAxis(axisNum, axisType, axis):
                words = []
                word = []
                for i, cell in enumerate(axis):
                    # Extract the letter from the cell, removing any brackets or markers
                    letter = cell.replace('[', '').replace('**', '').strip()
    
                    # Check if the cell contains a single letter
                    if len(letter) == 1:
                        # Append the letter and its coordinates to the 'word' list
                        # The coordinates are represented as tuples (row, column) or (column, row)
                        word.append((letter, (axisNum, i)) if axisType == 'row' else (letter, (i, axisNum)))
                    # If the word length is greater than 1, consider it as a complete word and append it to 'words'
                    elif len(word) > 1:
                        words.append(word)
                        word = []
                    else:
                        # If the word length is 1 or it is not a valid word, clear the 'word' list
                        word = []
    
                # Append the last word if it's not a single letter
                if len(word) > 1:
                    words.append(word)
    
                return words
    
            words = []
            if axisType == 'row':
                for i, row in enumerate(board):
                    words.extend(wordFinderAxis(i, axisType, row))
            elif axisType == 'col':
                for i, col in enumerate(zip(*board)):
                    words.extend(wordFinderAxis(i, axisType, col))
    
            return words
    
        # Get all words from previous board and new board
        previousWords = set(tuple(wordPair) for wordPair in wordFinderBoard(board1, 'row') + wordFinderBoard(board1, 'col'))
        newWords = set(tuple(wordPair) for wordPair in wordFinderBoard(board2, 'row') + wordFinderBoard(board2, 'col'))
    
        # Remove words that exist in previousWords from newWords
        newWords = newWords.difference(previousWords)
    
        # Create a dictionary to store cell values for efficient lookup
        cellValues = {(i, j): board1[i][j] for i in range(15) for j in range(15)}
    
        def calculator(wordPair, cellValues):
            '''
            Calculate the score for a given word on the board.
    
            Parameters:
                wordPair (tuple): A tuple containing the letters and their respective coordinates for a word.
                cellValues (dict): A dictionary containing cell values with coordinates as keys.
    
            Returns:
                wordScore (int): The score earned by the word.
            '''
            wordScore = 0
            wordMultiplier = 1
    
            for letter, coord in wordPair:
                # Get the cell value using the coordinates from the 'cellValues' dictionary
                cell_value = cellValues[coord]
    
                # Check for word multipliers (2W, 3W)
                if '2W' in cell_value:
                    wordMultiplier *= 2
                elif '3W' in cell_value:
                    wordMultiplier *= 3
    
                letterMultiplier = 1
                # Check for letter multipliers (2L, 3L)
                if '2L' in cell_value:
                    letterMultiplier *= 2
                elif '3L' in cell_value:
                    letterMultiplier *= 3
    
                # Calculate the score for the letter and apply letter multiplier
                wordScore += LETTER_SCORES[letter] * letterMultiplier
    
            # Apply word multiplier to the final score
            return wordScore * wordMultiplier
    
        totalScore = 0
        # Calculate the total score for all new words
        for wordPair in newWords:
            totalScore += calculator(wordPair, cellValues)
    
        return totalScore


    





    def bestMove(self):
        '''return: the best move in the form: (row,col,dir,word)
        parameter: letters in the players hand
        '''
        
        def getLetters():
            '''Prompt the player to enter valid letters and return them in uppercase.
        
            Returns:
                letters (list): A list of valid letters entered by the player.
            '''
            valid = False
            while not valid:
                userInput = input('Enter your letters here (abcdefg): ')
                if userInput.isalpha():
                    # If the user input contains only letters (no numbers or special characters)
                    letters = list(userInput.upper())  # Convert to uppercase for consistency
                    valid = True
                else:
                    print('That is an invalid input. Try inputting letters!')
            return letters

        
        letters = getLetters()        
        
        existing = self.board.copy()
        
        def wordFinder(board, letters):
            '''return: all possible word combinations
            parameter:
                board: the scrabble board
                letters: letters in the players hand
            '''
            possibleWords = DICTIONARY.copy()
            
            def refine1(letters, possibleWords):
                '''return: words that have letters in them from 'letters'
                parameter:
                    letters: letters in the players hand
                    possibleWords: the current dictionary
                '''
                refined = []
                for i in range(len(letters)):
                    letters[i] = letters[i].upper()
                for word in possibleWords:
                    valid = False
                    for letter in word:
                        if letter in letters:
                            valid = True
                    if valid:
                        refined.append(word)
                return refined

            
            def rowWordFinder(axisNum, axisType, axis, letters):
                '''return: The possible words in a row (not considering laterally)
                            in form: [[('H',(7,7)),('I',(7,8))],....]
                parameter: 
                    axis: a row in the array form
                    axisType: row (row) or col (column)
                    axisNum: the index of the row or column
                    letters: letters in the players hand
                '''
                        
                def multiStringMaker(string):
                    '''Return all strings of possible starting positions in row.
                
                    Parameters:
                        string (str): The row as a string.
                
                    Returns:
                        stringsR1 (list): A list of strings of possible starting positions in row.
                    '''
                    strings = []
                
                    # Generate all possible substrings starting from each index in the row string
                    for i in range(len(string) - 1):
                        strings.append((string[i:], i))
                
                    stringsR1 = [strings[0]]
                    for i in range(1, len(string) - 1, 1):
                        # Include substrings that start with a space after a space (indicates possible word start)
                        if strings[i - 1][0][0] == ' ' and len(strings[i][0].strip()) > 0:
                            stringsR1.append(strings[i])
                
                    # Check if the last substring should be removed (ends with a space)
                    remove = True
                    for letter in stringsR1[-1][0]:
                        if letter == ' ':
                            remove = False
                            break
                
                    if remove:
                        stringsR1 = stringsR1[:-1]
                
                    return stringsR1

                            
                def matcher(possibleWords, stringPair, letters):
                    '''Return all words that the player can make given a starting point.
                
                    Parameters:
                        possibleWords (list): The revised dictionary.
                        stringPair (tuple): The starting point (i.e., ('hello   f   as', 5)).
                        letters (list): Letters in the player's hand.
                
                    Returns:
                        refinedWords (list): A list of words that the player can make with the given starting point and available letters.
                    '''
                    words = []
                    string = stringPair[0]
                    firstSection = string.split()[0]
                
                    for word in possibleWords:
                        valid = True
                        if len(word) <= len(string) and len(word) > len(firstSection):
                            for i in range(len(word)):
                                if string[i] != word[i] and string[i] != ' ':
                                    valid = False
                                elif len(word) + 1 <= len(string) and string[len(word)] != ' ':
                                    valid = False
                        else:
                            valid = False
                
                        if valid:
                            words.append(word)
                
                    # Finding words that work with letters given
                    refinedWords = []
                    bingos = []
                    for word in words:
                        valid = True
                        availableLetters = letters.copy()
                        givenLetters = []
                        length = len(word)
                        section = string[:length]
                        for i in section:
                            if i != ' ':
                                givenLetters.append(i)
                
                        for letter in word:
                            if letter in availableLetters:
                                availableLetters.remove(letter)
                            elif letter in givenLetters:
                                givenLetters.remove(letter)

                            else:
                                valid = False
                
                        if valid:
                            refinedWords.append(word)
                            if len(availableLetters) == 0 and len(letters) == 7:
                                bingos.append(word)
                
                    return refinedWords, bingos

                
                string = ''
                coords = []
                for i in range(len(axis)):
                    if '[' in axis[i] or '**' in axis[i]:
                        string = string + ' '
                    else:
                        string = string + axis[i]
                    if axisType == 'row':
                        coords.append((axisNum, i))
                    elif axisType == 'col':
                        coords.append((i, axisNum))
                strings = multiStringMaker(string)
                
                formattedWords = []
                formattedBingos = []
                
                for i in strings: #i is the row (string, index)
                    startIndex = i[1]
                    if len(i[0].strip())>0:
                        words, bingos = matcher(DICTIONARY,i,letters)
                        for j in words: #j is a word
                            word = []
                            for k in range(len(j)): #k is a letter in word
                                word.append((j[k],coords[k+startIndex]))
                            formattedWords.append(word)
                        
                        for j in bingos: #j is a word
                            bingo = []
                            for k in range(len(j)): #k is a letter in word
                                bingo.append((j[k],coords[k+startIndex]))
                            formattedBingos.append(bingo)
                            
                return formattedWords, formattedBingos
                
            words = []
            bingos = []
            rows = board.copy()
            cols = board.transpose()
            
            for i in range(len(rows)):
                word, bingo = rowWordFinder(i, 'row', rows[i], letters)
                words += word
                bingos += bingo
            for i in range(len(cols)):
                word, bingo = rowWordFinder(i, 'col', cols[i], letters)
                words += word
                bingos += bingo
            return words, bingos
        
        moves, bingos = wordFinder(existing,letters)
        movesR1 = []
        for move in moves:
            proposed = z.board.copy()
            playedCoords = []
            for i in move:
                playedCoords.append(i[1])
                proposed[i[1]] = i[0]
            if self.validMove(proposed,playedCoords):
                score = self.pointCalculator(proposed,False)
                if move in bingos:
                    score += 50
                movesR1.append((move,score))
        
                
        def top10(movesR1):
            '''Return the top ten plays in the format:
            1. 9 points, row: 7, col: 7, dir: r, HELLO
        
            Parameters:
                movesR1 (list): All possible moves with associated point values.
        
            Returns:
                None: This function only prints the top ten plays.
            '''
            N = 10
            best10Plays = sorted(movesR1, key=lambda x: x[1], reverse=True)[:N]
            
            def printer(best10Plays):
                '''Print the top ten plays with their details.
        
                Parameters:
                    best10Plays (list): The top ten plays with associated point values.
        
                Returns:
                    None: This function only prints the plays.
                '''
                placing = 1
                for play in best10Plays:
                    word = ''
                    for i in play[0]:  # Extract the word from the play tuple
                        word += i[0]
                    
                    points = play[1]
                    row = play[0][0][1][0]
                    col = play[0][0][1][1]
                    direction = 'r' if play[0][1][1][0] - play[0][0][1][0] == 0 else 'd'
                    print('{}. {} points, row: {}, col: {}, dir: {}, {}'.format(placing, points, row, col, direction, word))
                    placing += 1
                    
            # Call the printer function with the top ten plays
            printer(best10Plays)
            
            return best10Plays

        return top10(movesR1)         
        
         
        
        
        
        













import time

z = board(boardMaker())
z.move()

print(time.time())
print(z.pointCalculator(None, True))
print(time.time())


