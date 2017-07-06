#imports functions from random, sys, and datetime
import random
import sys
import datetime

#the categories
students = ['ABID', 'CJ', 'KHALID', 'BRADLEY', 'SYLVIA', 'CODY', 'LYDIA', 'ALI', 'RILEY', 'SUAD', 'AUBREY']
movies = ['SCREAM', 'HOLES', 'JAWS', 'TAKEN', 'THOR', 'CARS', 'HOP', 'FROZEN', 'XMEN', 'SUPERMAN', 'TANGLED', 'SPIDERMAN', 'MATRIX', 'BOLT', 'BRAVE', 'MULAN']
games = ['MARIO', 'MINECRAFT', 'HALO', 'SKYRIM', 'PONG', 'DESTINY', 'PORTAL', 'KIRBY', 'DIABLO', 'SMITE', 'DOTA', 'ZELDA', 'SONIC', 'SPYRO', 'METROID']
superheroes = ['FLASH', 'ROBIN', 'THOR', 'HULK', 'RAVEN', 'SPIDERMAN', 'CYBORG', 'ICEMAN', 'SUPERMAN', 'BEAST', 'MYSTIQUE', 'SUPERBOY', 'STORM']
tv_shows = ['LOST', 'FRIENDS', 'FLASH', 'GOTHAM', 'SHERLOCK', 'BONES', 'HOUSE', 'PSYCH']
brands = ['SHARPIE', 'LEGO', 'DISNEY', 'NIKE', 'HONDA', 'VISA', 'FORD', 'IKEA', 'EBAY', 'FOX', 'NBC', 'PIXAR', 'KRAFT', 'COLGATE', 'SONY', 'HP', 'SEGA']
food = ['MANGO', 'HAM', 'PEAR', 'FRIES', 'SANDWICH', 'DONUT', 'CHIPS', 'RIBS', 'RAMEN', 'POUTINE', 'SOUP', 'BREAD']
animals = ['ZEBRA', 'LEOPARD', 'SHARK', 'SALMON', 'DOLPHIN', 'FLY', 'COW', 'OSTRICH', 'OWL', 'FLAMINGO', 'SPIDER', 'WHALE', 'BAT', 'TADPOLE', 'FROG', 'WORM', 'LIZARD']
countries = ['USA', 'CHINA', 'VIETNAM', 'CHILE', 'OMAN', 'FRANCE', 'ITALY', 'UK', 'IRELAND','MEXICO', 'GERMANY', 'SWITZERLAND']
colours = ['BLUE', 'RED', 'ORANGE', 'BROWN', 'BLACK','WHITE', 'PINK', 'GREY', 'GOLD', 'PEACH']
transportation = ['BIKE', 'CAR', 'TRUCK', 'PLANE', 'JET', 'TRAIN', 'SUBWAY', 'BOAT', 'SHIP', 'SUBMARINE']
body = ['ARM', 'LEG', 'HAND', 'HEAD', 'FINGER', 'TOE', 'NECK', 'STOMACH', 'NOSE', 'MOUTH', 'EARS', 'CHIN', 'ELBOW', 'CHEST', 'WRIST', 'ANKLE']
sports = ['GOLF', 'HOCKEY', 'CURLING', 'SKATING', 'BOWLING', 'WRESTLING', 'BOXING']
nature = ['LEAF', 'SNOW', 'SNOWFLAKE', 'ICE', 'SUN', 'SUNLIGHT', 'FLOWER', 'ROCK', 'BEACH', 'SAND', 'OCEAN', 'MUD', 'DIRT']
jobs = ['LAWYER', 'POLICE', 'FIREMAN', 'NURSE', 'PAINTER', 'SINGER', 'ACTOR', 'CASHIER', 'WAITER', 'JUDGE', 'SOLDIER', 'PILOT', 'CHEF']
teachers_and_staff = ['ZHENG', 'DUTKO', 'GROSNEY', 'COMBE', 'BONDY', 'MAHONEY', 'UHM', 'KHAN', 'RIGAS', 'LEZON', 'HARVEY', 'CHOI', 'ROTI', 'WATSON', 'MORAVEC']
disney = ['MICKEY', 'PLUTO', 'DAISY', 'PUMBA', 'SIMBA', 'TIMON', 'SCAR', 'ALICE', 'MULAN', 'DUMBO', 'ARIEL', 'JASMINE', 'ABU', 'NEMO', 'PIGLET', 'MERIDA', 'RAPUNZEL', 'ELSA', 'OLAF']
instruments = ['VIOLA', 'FLUTE', 'GUITAR', 'PIANO', 'CLARINET', 'DRUMS', 'TRIANGLE', 'KEYBOARD', 'HARP', 'ORGAN', 'BANJO', 'TUBA', 'VIBRAPHONE', 'HORN']

#a list of pictures that go with the number of lives the player has
hangman = [
'''
================================================================================

OSE!!!   YOU LOSE!!!   YOU LOSE!!!   YOU LOSE!!!   YOU LOSE!!!   YOU LOSE!!!   Y

================================================================================


                                        -----
                                       /    |
                                      O     |
                                     /|\    |
                                      |     |
                                     / \    |
                                            |
                                     ------------
''',
'''
________________________________________________________________________________

                                 <3
________________________________________________________________________________


                                        -----
                                       /    |
                                      O     |
                                     /|\    |
                                      |     |
                                     /      |
                                            |
                                     ------------                                 
''',
'''
________________________________________________________________________________

                                 <3 <3
________________________________________________________________________________


                                        -----
                                       /    |
                                      O     |
                                     /|\    |
                                      |     |
                                            |
                                            |
                                     ------------                                 
''',
'''
________________________________________________________________________________

                                 <3 <3 <3
________________________________________________________________________________


                                        -----
                                       /    |
                                      O     |
                                      |\    |
                                      |     |
                                            |
                                            |
                                     ------------                                  
''',
'''
________________________________________________________________________________

                                 <3 <3 <3 <3
________________________________________________________________________________


                                        -----
                                       /    |
                                      O     |
                                      |     |
                                      |     |
                                            |
                                            |
                                     ------------                                   
''',
'''
________________________________________________________________________________

                                 <3 <3 <3 <3 <3
________________________________________________________________________________


                                        -----
                                       /    |
                                      O     |
                                            |
                                            |
                                            |
                                            |
                                     ------------                                   
''',
'''
________________________________________________________________________________

                                 <3 <3 <3 <3 <3 <3
________________________________________________________________________________


                                        -----
                                       /    |
                                            |
                                            |
                                            |
                                            |
                                            |
                                     ------------                                     
''',
'''
________________________________________________________________________________

                                 <3 <3 <3 <3 <3 <3 <3
________________________________________________________________________________


                                        -----
                                            |
                                            |
                                            |
                                            |
                                            |
                                            |
                                     ------------
''',
]
def clear():
    #clears screen
    print ("\n" * 100)
def logo():
    logo = raw_input('''















                                    PROJECT: HANG
                                       
                                 by Vincent Ky Nguyen
















                                  PRESS ENTER TO PLAY
''')
    logo = ("start")
    if logo == ("start"):
        clear()
        start()
def start():
    #sets lives to 7
    lives = 7
    #empty list of guessed letters
    guessed = []
    #variable that states whether the player wins or not
    win = False
    #variable that states whether the player's input is valid
    categ_valid = False
    print ('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   WELCOME TO HANGMAN. IF YOU DO NOT GUESS THE WORD IN TIME, BILLY WILL DIE.''')

    #asks player to choose a category until it gets a valid answer
    while categ_valid == False:
        categ = raw_input('''
 ______________________________________________________________________________
|                               PICK A CATEGORY:                               |
|______________________________________________________________________________|
|                                                                              |
| STUDENTS IN THIS CLASS     MOVIES      VIDEO GAMES        SUPERHEROES        |
| TV SHOWS                   BRANDS      FOOD               ANIMALS            |
| COUNTRIES                  COLOURS     TRANSPORTATION     BODY PARTS         |
| SPORTS                     NATURE      JOBS               TEACHERS AND STAFF |
| DISNEY CHARACTERS                                         INSTRUMENTS        |
|                                                                              |
|                                    RANDOM                                    |
|______________________________________________________________________________|
        \n
        ''')
        #makes the input lowercase
        categ = categ.lower()
        #picks a random word from the chosen category
        if categ == ("students in this class") or categ == ("students") or categ == ("class"):
            categ = ("students in this class")
            word = random.choice(students)
            categ_valid = True
        elif categ == ("movies"):
            word = random.choice(movies)
            categ_valid = True
        elif categ == ("video games") or categ == ("games"):
            categ = ("video games")
            word = random.choice(games)
            categ_valid = True
        elif categ == ("superheroes") or categ == ("heroes"):
            categ = ("superheroes")
            word = random.choice(superheroes)
            categ_valid = True
        elif categ == ("tv shows") or categ == ("shows"):
            categ = ("tv shows")
            
            word = random.choice(tv_shows)
            categ_valid = True
        elif categ == ("brands"):
            word = random.choice(brands)
            categ_valid = True
        elif categ == ("food"):
            word = random.choice(food)
            categ_valid = True
        elif categ == ("animals"):
            word = random.choice(animals)
            categ_valid = True
        elif categ == ("countries"):
            word = random.choice(countries)
            categ_valid = True
        elif categ == ("colours") or categ == ("colors"):
            categ = ("colours")
            word = random.choice(colours)
            categ_valid = True
        elif categ == ("transportation") or categ == ("transport"):
            categ = ("transportation")
            word = random.choice(transportation)
            categ_valid = True
        elif categ == ("body parts") or categ == ("body"):
            categ = ("body parts")
            word = random.choice(body)
            categ_valid = True
        elif categ == ("sports"):
            word = random.choice(sports)
            categ_valid = True
        elif categ == ("nature"):
            word = random.choice(nature)
            categ_valid = True
        elif categ == ("jobs") or categ == ("occupations"):
            word = random.choice(jobs)
            categ_valid = True
        elif categ == ("teachers and staff") or categ == ("teachers") or categ == ("staff"):
            categ = ("teachers and staff")
            word = random.choice(teachers_and_staff)
            categ_valid = True
        elif categ == ("disney characters") or categ == ("disney"):
            categ = ("disney characters")
            word = random.choice(disney)
            categ_valid = True
        elif categ == ("instruments"):
            categ = ("instruments")
            word = random.choice(instruments)
            categ_valid = True    
        elif categ == ("random") or categ == ("any"):
            #picks random number
            num = random.randint(-1, 17)
            #list of categories
            rand = [students, movies, games, superheroes, tv_shows, brands, food, animals, countries, colours, transportation , body, sports, nature, jobs, teachers_and_staff, disney, instruments]
            #lists of category names
            display = ['students in this class', 'movies', 'video games', 'superheroes', 'tv shows', 'brands', 'food', 'animals', 'countries', 'colours', 'transportation' , 'body parts', 'sports', 'nature', 'jobs', 'teachers and staff', 'disney characters', 'instruments']
            #picks category and name according to number chosen
            choices = rand[num]
            categ = display[num]
            #picks random word from chosen category
            word = random.choice(choices)
            #exits while loop
            categ_valid = True
        else:
            clear()
            print('''
________________________________________________________________________________
                                                                              
                         THAT IS NOT A VALID CATEGORY!!                                                                                                      
________________________________________________________________________________

''')

    #hides the word            
    hidden = ('_')*(len(word))
    #prints visuals
    print (hangman[7])
    #adds a space after each underline and then prints it
    spaced = (' ')
    for ch in hidden:
        spaced = spaced + ch + (' ')
    print ('''
________________________________________________________________________________
                                                 
                                    %s 
________________________________________________________________________________
        ''' % spaced)
    
    while lives > 0 and win == False:
        categ = categ.upper()
        print ("                                        LIVES: %r" % lives) #prints lives
        print ("                                YOUR CATEGORY IS: %s" % categ)

        if ('_') not in hidden:
            #if the word is guessed, the player wins
            win == True
            print('''
                                         ^__^
                                         
                                      YOU WIN!!!
            ''')
            #brings the player to the end of the game
            end()
        else:
            print ("                                  LETTERS REMAINING: %r" % hidden.count('_')) #prints how many letters left
            #asks the player to guess a letter
            guess = raw_input("\n GUESS A LETTER.\n >>> ")
            guess = guess.upper()
            #checks if it is a valid letter                   
            if True and guess in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                #lessens the word to the first character
                try:
                    guess = guess[0]
                except IndexError:
                    guess = None
                #if it is empty, a warning will show 
                if guess == None:
                    clear()
                    print('''
________________________________________________________________________________

                             DON'T LEAVE IT EMPTY!!
________________________________________________________________________________

                    ''')
                elif guess in guessed:
                    clear()
                    #prints a warning message saying that the player chose already guessed that letter
                    print('''
________________________________________________________________________________

                           YOU ALREADY GUESSED THAT!!
________________________________________________________________________________

                    ''')

                else:
                    guessed.append(guess)   
                    if guess in word:
                        #if the guess is correct, the letter is revealed
                        hidden = hidden[0:word.index(guess)]+guess+hidden[word.index(guess)+1:]
                    else:
                        #if it is wrong, the player loses a life
                        lives = lives-1
                    clear()                        
            else:
                clear()
                #prints a warning message saying that it is not a valid letter
                print('''
________________________________________________________________________________

                             THAT IS NOT A LETTER!!
________________________________________________________________________________

                    ''')

        #prints guessed letters
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
        print ("GUESSED LETTERS: ")
        print (guessed)
        #prints the picture according to the lives
        print (hangman[lives])
        #adds a space after each letter
        spaced = (' ')
        for ch in hidden:
            spaced = spaced + ch + (' ')
        print ('''
________________________________________________________________________________
                                                 
                                    %s 
________________________________________________________________________________
            ''' % spaced)
        
    #if there are no lives, a losing message is printed
    if lives == 0:
        print('''
________________________________________________________________________________

                             THE WORD WAS %s
________________________________________________________________________________

                    '''% (word))
        print('''
                                         X__X
                                         
                                      GAME OVER!

        ''')
        #brings the player to the end of the game
        end()

#end of game conditions
def end():
    #variable that states whether the player's input is valid or not
    validchoice = False
    #prints the date and my name
    print ("GAME COMPLETED: %s" % str(datetime.date.today()))
    print ("MADE BY VINCENT KY NGUYEN")
    #asks the player if they want to replay until it gets a valid answer
    while validchoice == False:
        choice = raw_input("\n                                PLAY AGAIN?: YES OR NO\n                        >>> ")
        choice = choice.lower()    
        if choice == ("yes") or choice == ('y') or choice == ('yeah') or choice == ('yaas') or choice == ('yep') or choice == ('yup'):
            clear()           
            #exits while loop
            validchoice = True
            #starts game again
            logo()
        elif choice == ("no") or choice == ('n') or choice == ('nah') or choice == ('nope') or choice == ('nuh uh'):
            #exits while loop
            validchoice = True
            print('''
________________________________________________________________________________

                                   GOODBYE!!!
________________________________________________________________________________

                    ''')
            #exits
            exit()
            
#start of game
logo()
