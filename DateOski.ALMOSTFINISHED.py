# Start game by running python DateOski.py

from operator import neg
import time
import random
import os
player_name = ""
oski_points = 0
questions_asked = []
positive_responses_given = []
negative_responses_given = []
neutral_responses_given = []
scenarios_done = []

# List of free-response questions Oski can ask the player
oski_questions = [
    "Oski: So... What do you think of my outfit?",
    "Oski: I know I'm probably the first bear you've talked to... What do you think of bears?",
    "Oski: So... What do you think of UC Berkeley's campus?",
    "Oski: How do you feel about the UC Berkeley Marching Band? I'm their conductor!",
    "Oski: So... What do you think of our school's football games?",
    "Oski: I have an odd question for you... How do I smell?",
    "Oski: So I help out in the school dining halls sometime! What do you think of their food?",
    "Oski: I think this date is quite lovely! What do you think of it so far?",
    "Oski: What do you think of living in Berkeley?",
    "Oski: How do you feel about the UC libraries?"
]
positive_words = [
    "beautiful", "handsome", "cute", "dashing", "cool", "fire", "nice", "lovely", "love", "like", "dear", "awesome", "great", "talented", "win", "good", "delicious", "tasty", "yummy", "fun", "pleasant", "calm", "study", "favorite"
]
negative_words = [
    "ugly", "weird", "scary", "annoying", "dumb", "boring", "horrible", "hate", "lame", "lose", "loser", "losers", "stinky", "bad", "awful", "gross", "rotten", "disgusting", "unpleasant", "terrible"
]

# Allows Oski's response boards to be refreshed after player_name is entered
def set_oski_responses():
    global oski_responses_positive
    global oski_responses_negative
    global oski_responses_neutral
    # List of Oski's responses if the player is nice!
    oski_responses_positive = [
        f"Oski blushes.\nOski: Wow... That's good to hear, {player_name}!",
        f"Oski flashes a smile.\nOski: I agree, {player_name}!",
        f"Oski grins.\nOski: You're so right, {player_name}!",
        f"Oski nods in agreement.\nOski: That's really nice, {player_name}!",
        f"Oski smiles warmly.\nOski: I may be biased... but you're right, {player_name}!"
    ]

    # List of Oski's responses if the player is mean :(
    oski_responses_negative = [
        f"Oski frowns.\nOski: That was hurtful, {player_name}.",
        f"You watch a singular tear drip down from Oski's eye.\nOski: Why would you say this, {player_name}?.",
        f"Oski looks disappointed.\nOski: That's not nice, {player_name}.",
        f"Oski's smile drops.\nOski: If that's what you think, {player_name}...",
        f"Oski sighs.\nOski: I guess we all have our own opinions, {player_name}.",
    ]

    # List of Oski's responses if the player's response is neutral or positive/negative words are not detected.
    oski_responses_neutral = [
        f"Oski ponders for a moment.\nOski: That's fair enough, {player_name}!",
        "Oski nods.\nOski: I see.",
        "Oski looks indifferent.\nI understand.",
        "Oski pauses for a moment.\nOski: I guess so.",
        "Oski: I suppose so."
    ]

# Initiates chatting with Oski, player can respond freely, checks if player's response is positive, negative, or neutral
def chat():
    global questions_asked, positive_responses_given, negative_responses_given, neutral_responses_given
    question = random.randint(0,len(oski_questions)-1)
    while question in questions_asked:
        question = random.randint(0,len(oski_questions)-1)
    questions_asked.append(question)
    print_slow(oski_questions[question])
    print()
    response = input(">> ").lower()
    response = ''.join([char for char in response if char.isalpha()])
    impression = 0
    for word in positive_words:
        if response.count(word) > 0:
            impression = 1
            break
    if impression == 0:
        for word in negative_words:
            if response.count(word) > 0:
                impression = -1
                break
    if impression == 1:
        for word in negative_words:
            if response.count(word) > 0:
                impression = 0
                break
    if response.count("not" and "dont") % 2 == 1:
        impression = -impression 
    if impression == 1:
        oski_response = random.randint(0,len(oski_responses_positive)-1)
        while oski_response in positive_responses_given:
            oski_response = random.randint(0,len(oski_responses_positive)-1)
        positive_responses_given.append(oski_response)
        print_slow(oski_responses_positive[oski_response])
        change_oski_points(5)
    elif impression == -1:
        oski_response = random.randint(0,len(oski_responses_negative)-1)
        while oski_response in negative_responses_given:
            oski_response = random.randint(0,len(oski_responses_positive)-1)
        negative_responses_given.append(oski_response)
        print_slow(oski_responses_negative[oski_response])
        change_oski_points(-5)
    elif impression == 0:
        oski_response = random.randint(0,len(oski_responses_neutral)-1)
        while oski_response in neutral_responses_given:
            oski_response = random.randint(0,len(oski_responses_neutral)-1)
        neutral_responses_given.append(oski_response)
        print_slow(oski_responses_neutral[oski_response])
        change_oski_points(2)

# Initiates ending of the game; determines ending based on number of Oski points
def game_end():
    global oski_points
    if oski_points >= 30:
        make_choice(3)
    elif oski_points >= 20:
        make_choice(4)
    else:
        print_slow(f"Oski turns to you and shuffles awkwardly.\nOski: {player_name}, I think I'm gonna go now... I'll uhh... see you around campus. Bye!\nBefore you can even respond, Oski has vanished.\nYou walk home alone, wondering what you could've done differently.\n")


# Allows scenario_board to be refreshed after player_name is entered
def set_scenario_board():
    # The board of scenarios that require the player to make a choice
    global scenario_board
    scenario_board = [
        # 0 (INTRO.1)
        ["It is a perfectly normal day for you as you take a stroll throughout the beautiful campus of UC Berkeley. You close your eyes and breathe in the fresh air, when suddenly...\nBONK!\nYou bump into something- no, ~someone~ large, round, and fuzzy. The recoil causes you to bounce off and fall on your butt.\nStranger: Oh dear! I am so sorry! Please allow me to help you up!\nThe stranger reaches his gloved hand out to you.\n(1) -Accept the stranger's helping hand.-\n(2) WATCH WHERE YOURE GOING, JERK!!!\n(3) -You stand up by yourself, without his assistance.-\n",
        ["The stranger hoists you up to your feet using his immense strength. You take a good look at him. He is a large, brown, and furry bear in white gloves and a yellow UC Berkeley cardigan. You blush upon seeing his shiny, charismatic smile.", 5],
        ["Stranger: IM SORRY!!!! I CAN BARELY SEE THROUGH THIS COSTUME'S EYES!!!!\nThe stranger cries and runs away. You never see him again.", -1000],
        ["The stranger pulls his hand back and smiles apologetically. He shuffles awkwardly.", 2]
        ],
        # 1 (INTRO.2)
        ["You are shopping for snacks in Trader Joes, when you see that there is only one box of your favorite dark chocolate peanut butter cups left! As you reach out to grab it, your hand clashes with another gloved hand belonging to a large, fuzzy, and brown stranger wearing a yellow UC Berkeley cardigan.\n(1) Oh... you can have it!\n(2) I saw those first!\n(3) -Slap his hand away!-\n",
        ["The stranger looks grateful.\nStranger: You are too kind! Sorry for taking the last box, but if I don't get my daily fix of sugar, I fear that I may harm others...\nIgnoring his odd comment, you realize how dashingly handsome the stranger is!", 5],
        ["The stranger looks embarassed.\nStranger: I am so sorry! I didn't see you there!\nYou buy the chocolates begrudgingly and see the apologetic stranger waiting for you by the exit.", 2],
        ["Stranger: IM SORRY!!!! I JUST LOVE CHOCOLATE SO MUCH!!!!\nThe stranger cries and runs out of the store. You never see him again.", -1000]
        ],
        # 2 (INTRO.3)
        ["You are scootering around the streets of Berkeley at full speed, when suddenly, a large, round, brown, fuzzy stranger in a yellow UC Berkeley cardigan jumps onto the road! You collide, and your scooter is totalled, so you throw it away in the trash can, and face the stranger.\n(1) Are you okay???\n(2) YOU RUINED MY SCOOTER! IM GONNA KILL YOU!\n(3) Why did you do that???\n",
        ["The stranger stands up, perfectly uninjured.\nStranger: I am okay, thank you, but I am so sorry for ruining your scooter! I thought jumping into the road would be a funny prank...\nYou berate him about road safety and he ashamedly endures your lecture. You check to see if he's listening, and he flashes a charismatic smile.", 5],
        ["Stranger: IM SORRY!!!! I THOUGHT IT WOULD BE FUNNY!!!!\nThe stranger cries and hobbles away with what appears to be a broken leg. You never see him again.", -1000],
        ["The stranger stands up, perfectly uninjured.\nStranger: I thought jumping into the road would be a funny prank... Sorry about your scooter...\nYou berate him about road safety and he ashamedly endures your lecture. You check to see if he's listening, and he flashes you a charismatic smile.", 2]
        ],
        # 3 (ENDING.HIGH)
        [f"Oski suddenly shuffles shyly, then holds your hands and gazes into your eyes.\nOski: {player_name}, I had a lot of fun with you. Would you want to... be mine?\n(1) Oh, Oski... Of course!\n(2) Sorry... I don't feel the same way...\n(3) -Kiss Oski-\n",
        [f"Oski picks you up and spins you around.\nOski: Oh, {player_name}, I'm so happy to hear this!\nYou and Oski embrace in a warm hug before parting ways, smiling the whole walk home.\n", 0],
        [f"Oski looks devastated. He lets go of your hands and turns away to weep.\nOski: I see... Well... Goodbye forever, {player_name}.\nYou hear Oski's crying grow softer as he walks away, a heartbroken bear.\n", 0],
        [f"Oski's eyes widen in shock, but he melts into your kiss.\nOski: I'll take that as a yes...\nYou and Oski smile lovingly into each other's eyes, and Oski picks you up and carries you into the sunset.\n", 0]
        ],
        # 4 (ENDING.MID)
        [f"Oski turns to you and smiles.\nOski: {player_name}, I had a lot of fun with you. We should hang out some more when you're free!\n(1) Of course!\n(2) I like you!\n(3) No thanks.\n",
        [f"Oski nods in satisfaction.\nOski: I'll see you around then, {player_name}!\nYou and Oski shake hands before going your separate ways, thinking about the fun that has yet to come in your friendship.\n", 0],
        [f"Oski shuffles awkwardly.\nOski: Sorry {player_name}, I don't think I feel the same way... but I'd still like to be friends!\nYou cover up your heartbreak with a smile and part ways, but when you're home, you wonder what you could've done differently...\n", 0],
        [f"Oski looks disappointed.\nOski: Oh... Well, I can't force you to be my friend. Goodbye, {player_name}.\nYou and Oski turn away from each other and go your separate ways. You hear Oski weeping a little bit, but honestly, you don't care.\n", 0]
        ],
        # 5 (CAFE)
        [f"For a coffee at Cafe Strada!\n(1) As long as you're buying!\n(2) I'm not thirsty. Goodbye.\n", 
        ["Oski blushes bashfully.\nOski: Why of course! Let's go!", 3], 
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.\n", -1000]
        ],
        # 6 (CAMPANILE)
        [f"To my carillon bells performance atop the Campanile!\n(1) You play the carillon?! I'd love to come!\n(2) That's not very impressive. Goodbye.\n",
        ["Oski blushes bashfully.\nOski: Oh I'm not that great... but come along!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nYou watch Oski sadly enter the campanile alone. Soon enough, you hear the sorrowful ringing of carillon bells as a heartbroken Oski plays his heart out.\n",-1000]
        ],
        # 7 (RSF)
        [f"Rock climbing in the Recreational Sports Facility!\n(1) As long as we can race! It's a date!\n(2) This isn't really my thing. Goodbye.\n",
        ["Oski blushes bashfully.\nOski: Alright! Follow me!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.", -1000]
        ],
        # 8 (BIG C)
        [f"On a hike up to the Big C!\n(1) I could use a nice nature hike!\n(2) I'm too tired... I think I'm going to go home. Goodbye.\n",
        ["Oski: Alright! Follow me!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.", -1000]
        ],
        # 9 (AQUARIUM)
        [f"To the aquarium?\n(1) I'd love to!\n(2) NO!!! I HATE FISH!!!! I'M GOING HOME!!!\n",
        ["Oski: Alright! Let's hop on the bus!", 3],
        ["Oski: I'M SO SORRY!!! I DIDN'T KNOW!!!\nOski crumples to the floor, sobbing at the one that got away.", -1000]
        ],
         # 10 (GOLDEN GATE)
        [f"To the Golden Gate Bridge?\n(1) I love San Francisco! \n(2) I don't really want to hang out with you.\n",
        ["Oski: Alright! Let's catch the BART!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.", -1000]
        ],
         # 11 (ICE SKATING)
        [f"Ice skating with me in San Francisco?\n(1) I'd like that very much!\n(2) I dont want to.\n",
        ["Oski: Alright! Let's catch the BART!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.", -1000]
        ],
         # 12 (MARINA)
        [f"To the marina!\n(1) Sure, why not!\n(2) Why would I go to the marina with you? Goodbye.\n",
        ["Oski: Alright! Let's catch the next bus!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.", -1000]
        ],
         # 13 (BOTANICAL GARDEN)
        [f"To the botanical garden?\n(1) Fine... Just 'cause you're cute.\n(2) Of course not! Goodbye.\n",
        ["Oski blushes profusely.\nOski: W-well... let's head over then!", 3],
        ["Oski: Oh... Well, I'm sorry to have bothered you.\nOski sadly walks away. You never see him again.", -1000]
        ],
        # 14 (CAFE.1)
        ["Oski: What are you craving?\n(1) Cafe Strada's famous white hot chocolate!\n(2) A vanilla latte!\n(3) A peach ginger tea!\n(4) Just a water.\n",
        ["Oski's face lights up in glee.\nOski: No way! That's my favorite drink!", 5],
        ["Oski: Ahh, the classic latte!", 2],
        ["Oski: Ooh, something refreshing!", 2],
        ["Oski looks disappointed.\nOski: But I wanted to treat you...", -5]
        ],
        # 15 (CAFE.2)
        ["Oski takes a sip of his white hot chocolate... through a straw coming out of his eyeball.\n(1) WHY is there a STRAW coming out of your EYEBALL???\n(2) That's an... interesting way to drink!\n(3) Wow! I wish I could drink using my eyeball!\n",
        ["Oski's face reddens in humiliation.\nOski: It's just how I was born!", -5],
        ["Oski: Oh... I hope it's not too disturbing!", 2],
        ["Oski lights up.\nOski: Really? People usually freak out when they see this!", 5]
        ],
        # 16 (AQUARIUM.1) 
        ["You and Oski wander around the aquarium, pointing out cool creatures to each other.\nOski: What's your favorite thing in an aquarium?\n(1) Fish!\n(2) Sharks...\n(3) Jellyfish.\n",
        ["Oski's face lights up with awe and excitement. He looks down into your beautiful eyes.\nOski: I love fish too, they make a tasty snack", 5],
        ["Oski looks down and then away with an utter look of disappointment and heartbreak.\nOski: Oh... A shark tried to steal my gloves once... ", -5 ],
        ["Oski with a look of confusion looks at you. \nOski: Jellies are interesting I guess.", 2]
        ],
        # 17(AQUARIUM.2)
        [f"Oski leans against the octopus tank, only for the octopus to escape! It climbs all over him, and Oski starts to panic!\nOski: {player_name.capitalize()}?! A LITTLE HELP???\n(1) Fall on the floor from laughing so hard!\n(2) Rush over and throw the octopus back in the tank!\n(3) Scream and find an employee to help!\n", 
        ["Oski sees your fit of laughter and bursts into tears. He runs away, out of the aquarium, wailing, with the octopus still stuck on him. You don't notice because you are still laughing on the floor. Bystanders are judging you.", -1000],
        ["Oski's screams die down when you chuck the octopus into its tank. Oski gazes at you with shining eyes.\nOski: Th-thank you... My hero...", 5 ],
        ["Oski cries until an employee removes the octopus from his being.\nOski: Thanks... That was embarassing...", 2]
        ],
        # 18 (Golden Gate Bridge.1)
        [ "You head towards the great, gigantic beauty that is the Golden Gate Bridge. You both gaze upon it admirably. \nOski: So... What's your favorite thing about living in the Bay Area? \n(1) The Weather (2) Being close to UC Berkeley (3) Stanford.\n",
        ["Oski: Oh that's like the most boring response I have ever heard ", +2],
        ["Oski stretches his big arms and gives you the tightest hug ever, so much so that you can hear his heart beating.\nOski: You are the best thing that has ever happened to me. I love Berkeley, It is my home and my favorite people live here!", +5],
        ["Oski with a face of disgust looks at you with eyes of horror as his eyes watyer\n His knees begin to weaken as his sorrowful face begins to turn red with anger\n Oski: How dare you. Don't Call me. Don't come by my house. We're done.", -1000],
        ] ,
        # 19 (Golden Gate Bridge.2)
        [ "Oski shyly twirls with his fingers.\nOski: So... I've always wanted to bring a date to the Golden Gate... Can we take a selfie to commemorate?",
        ["Oski: Oh that's like the most boring response I have ever heard ", +2],
        ["Oski stretches his big arms and gives you the tightest hug ever, so much so that you can hear his heart beating.\n Oski: You are the best thing that has ever happened to me. I love Berkeley, It is my home and my favorite people live here!", +5],
        ["Oski with a face of disgust looks at you with eyes of horror as his eyes watyer\n His knees begin to weaken as his sorrowful face begins to turn red with anger\n Oski: How dare you. Don't Call me. Don't come by my house. We're done.", -1000],
        ] ,
        # 19 (Ice Skating in Sf.1)
        [ "Walking towards the section of ice skating in SF, Oski grabs you by the wais\nOski: So do you want to ice skate with me? \n(1) Of course! I would love to, my little bear!\n(2) It seems fun! \n(3) AS IF! Let go of me you bear!\n",
        ["Oski looks at you with a smile that begins to fade he looks at you with confusion \n Oski: I think you're taking things too fast... But I kinda like it...", +2],
        ["Oski with utter excitement grabs your hand as you begin to ice skate around the tree\n Oski: You are utterly breathtaking", +5],
        ["He grabs the left side of his chest as he falls to his knees. Tears falling, he screams in pure agony\nOski: PICK ME, CHOOSE ME, LOVE ME", -1000]
        ],
       
        # 19 (MARINA.1)
        ["Oski blindfolds you suddenly\n : It's a surprise!\n(1)Kick him and run away!\n(2) Allow him to blindfold you...\n(3) Cry in utter disbelief!\n",
        ["Oski: OUCH! You are so mean. This isn't working out!", -1000],
        ["Oski hugs you with his warm fur and picks you up!\n After a long while he puts you down where you feel sound and hear the waves crashing in the distance\n Oski: Hi, I know you have been stressed doing Project 6 for CS10, I hope this helps you relax.",+5],
        ["Oski: Oh no I didn't mean to scare you. \n He takes the blindfold off and hugs you tightly ", +2 ]
        ],

        # 20 (Botanical Gardens.1)
        [ "Walking down the Botanical Gardens you are surrounded by multiple colors that make Oski look more handsome than ever.\nIt smells so wonderful, a mix of clean and flowers\nBoth of you walk down the isles of flowers.\nOski: What's your favorite thing about nature ? \n(1) Trees\n(2) Bears like you!\n",
        [ "A single tear falls down Oski's face. It falls onto the dirt dramatically and slowly \n He looks at you with a menacing face \nOski: Trees are so weird. I cannot with you.", -5 ],
        ["Oski, with a face of pure excitement leaps into the air. Blushing more than ever, he looks down feeling shy.\nOski: You are my favorite human.", +5 ] 
        ],
    ]

# Initiates game over, ends the program, possibly turn it into an input based command for multiple endings!!
def GAMEOVER():
    print_slow("GAME OVER")
    exit()

# Prints text one character at a time
def print_slow(string):
    print()
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.02) #(0.02) default

# The choice-making aspect of the game
def make_choice(scenario):
    print()
    print_slow(scenario_board[scenario][0])
    while True:
        player_choice = input(">> ")
        try:
            if int(player_choice) > 0 and int(player_choice) < len(scenario_board[scenario]) or isinstance(player_choice, int):
                
                print_slow(scenario_board[scenario][int(player_choice)][0])

                if scenario_board[scenario][int(player_choice)][1] != 0:
                    change_oski_points(scenario_board[scenario][int(player_choice)][1])
                    print()

                if oski_points < 0:
                    GAMEOVER()
                break
            else:
                print_slow(f"{oski_name}: Sorry, I don't understand what you're saying.\n")
        except ValueError:
            print_slow(f"{oski_name}: Sorry, I don't understand what you're saying.\n")

# Changes number of Oski Points and prints out the count
def change_oski_points(points_earned):
    global oski_points
    global oski_points_earned
    oski_points_earned = int(points_earned)
    oski_points += oski_points_earned
    print()
    print_slow(f"You earned {oski_points_earned} Oski Points!")
    print_slow(f"You have {oski_points} Oski Points!")

# Function to display the menu
def display_menu():
    print(""" 
                        ***++*#                    
                       #+====*##                    
                       ##+**+#+#                    
                   #######*###*+++*###****#         
                  ######++*+++++++*#++####*#        
                  #####++****+++++***++##*##        
                  #**#*++*--+*++*+=-#++**##         
                    ###+*#####**#####+*#            
                      #++++++##*#*+++++#            
                      #*++++++++++++*++###          
                   #####*++++*****+++########       
              #############*******###############   
            ####################################### 
           #########################################
    ##******##############*#########################
  ##-=###############++++*#-=###################### 
##==##################+++**#*-+###################  
#-*####**************#+++#*###-=#############++##   
#-*####-###############***####-=###############+##  
#-*####-#--------------+#*++++-=############++####  
#-*####-#--------------+##################*+++++#   
#-*####-#-------------------*############++++++*#   
#-*####-#-------------------=##########*++++++**#   
#-*####-#---------------------+#####*++++++++++#    
#-*####-#--------------++======+#*****+*++++++*#    
#-*####-#--------------+=+####-+##**+++*++++++#     
#-*####------------------+####-+# #**++#*++*#*# ### 
#==##########################*-+#  ##*+*+++++*#     
 ##==#######################-=#       #####++++*#   
   ##-----------------------##       ##**++#**++*#  
     #######################         #########*###  
""")
    print_slow(""" 
  ___  ____  _  _____   ____    _  _____ ___ _   _  ____   ____ ___ __  __ 
 / _ \/ ___|| |/ /_ _| |  _ \  / \|_   _|_ _| \ | |/ ___| / ___|_ _|  \/  |
| | | \___ \| ' / | |  | | | |/ _ \ | |  | ||  \| | |  _  \___ \| || |\/| |
| |_| |___) | . \ | |  | |_| / ___ \| |  | || |\  | |_| |  ___) | || |  | |
 \___/|____/|_|\_\___| |____/_/   \_\_| |___|_| \_|\____| |____/___|_|  |_|
""")
    time.sleep(1)
    print_slow("(1) Start Dating Simulator")
    print_slow("(2) Exit")
    return input("\n>> ")

#STARTS MENU FUNCTION and DISPLAYS 
def MENU():
    while True:
        option = display_menu()
        if option == "1":
            os.system('cls')or os.system('clear')
            START()
            break
        elif option == "2":
            print_slow("Exiting the Oski Dating Simulator. Goodbye!")
            break
        else:
            print_slow("Invalid option. Please choose again.")

# Starts game, plays upon start of program
def START():
    global oski_name, scenarios_done
    oski_name = "Stranger"
    set_scenario_board()
    make_choice(random.randint(0,2))
    global player_name
    print_slow(f"{oski_name}: My name is Oski. What is yours?\n")
    oski_name = "Oski"
    player_name = input(">> ")
    set_scenario_board()
    set_oski_responses()
    #Oski: Well, {player_name}, please allow me to make it up to you with 
    for i in range(3):
        random_scenario = random.randint(5, 13)
        while random_scenario in scenarios_done:
            random_scenario = random.randint(5, 13)
        scenarios_done.append(random_scenario)
        if i == 0:
            print_slow(f"Oski: Well, {player_name}, would you forgive me if I took you...")
        elif i == 1:
            print_slow(f"Oski: That was quite nice, {player_name}, but why don't we continue this date elsewhere? Let's go")
        elif i == 2:
            print_slow(f"Oski: {player_name}, the day is nearly over, but for one last item, do you want to go")
        make_choice(random_scenario)
        if random_scenario == 5:
            #Cafe Strada date
            print_slow(f"You and Oski take a peaceful stroll to Cafe Strada.\nOski: Why dont you have a seat, {player_name}, and I'll buy your drink.")
            make_choice(14)
            print_slow("Oski buys your drinks, which are promptly made, and sits across from you.")
            chat()
            make_choice(15)
            print_slow("Oski finishes his drink, and watches as you finish yours.")
            chat()
        elif random_scenario == 6:
            #Campanile date
            print_slow("Campanile")
        elif random_scenario == 7:
            #RSF date
            print_slow("RSF")
        elif random_scenario == 8:
            print_slow("You and Oski head over to the start of the hiking trail. You notice that Oski doesn't walk normally... or at all. Instead, he skips with his arms crossed behind his back.")
            #Big C
            print_slow("Big C")
        elif random_scenario == 9:
            #Aquarium Date 
            print_slow ("Aquarium")
            make_choice(16)
        elif random_scenario == 10: 
            # Golden Gate Bridge date 
            print_slow("Golden Gate Bridge")
            make_choice(17)
        elif random_scenario == 11:
            #Ice Skating in Sf
            print_slow("Ice Skating in San Francisco")
            make_choice(18)
        elif random_scenario == 12:
            # Beach Date 
            print_slow("Beach")
            make_choice(19)
        elif random_scenario == 13: 
            # Botanical Garden 
            print_slow ("Botanical Garden")
            make_choice(20)
    game_end()


MENU()
