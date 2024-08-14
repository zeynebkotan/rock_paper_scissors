import random

# Function to evaluate the winner of the round
def evaluate_winner(choice_of_player, choice_of_computer):
    global player_round_score, computer_round_score, winner

    if (choice_of_player in ["rock", "stein", "taş"] and choice_of_computer in ["paper", "papier", "kağıt"]) or \
       (choice_of_player in ["paper", "papier", "kağıt"] and choice_of_computer in ["scissors", "schere",
        "makas"]) or \
       (choice_of_player in ["scissors", "schere", "makas"] and choice_of_computer in ["rock", "stein", "taş"]):
        winner = computers_name
        computer_round_score += 1
    elif (choice_of_computer in ["rock", "stein", "taş"] and choice_of_player in ["paper", "papier", "kağıt"]) or \
         (choice_of_computer in ["paper", "papier", "kağıt"] and choice_of_player in ["scissors", "schere",
          "makas"]) or \
         (choice_of_computer in ["scissors", "schere", "makas"] and choice_of_player in ["rock", "stein", "taş"]):
        winner = players_name
        player_round_score += 1
    else:
        winner = None

# Function to display the game score
def display_scoreboard():
    cell_width = max(len(players_name), len(computers_name), len(str(player_game_score)),
                     len(str(computer_game_score))) + 2  # We add 2 for side spaces.
    line = "+" + "-" * cell_width + "+" + "-" * cell_width + "+"  # Drawing the horizontal line.
    print(line)
    print(f"| {players_name.center(cell_width - 2)} | {computers_name.center(cell_width - 2)} |")
    print(line)
    print(f"| {str(player_game_score).center(cell_width - 2)} | {str(computer_game_score).center(cell_width - 2)} |")
    print(line)


# List of available languages
languages = ["english", "deutsch", "türkçe"]

# Choosing the language
while True:
    print("-" * 200)
    print("Choose a language to continue.")
    print("You can choose either English, Deutsch, or Türkçe.")
    language_preference = input("Which language do you prefer?: ").lower()
    print("-" * 200)
    if language_preference not in languages:
        print("Please write something valid.")
        continue
    else:
        break

# Initializing the variables and counters
player_round_score = 0
computer_round_score = 0
player_game_score = 0
computer_game_score = 0
game_number = 0
round_number = 0
winner = None

# Game logic starts here
if language_preference == "english":  # English language implementation

    # possible actions (eng)
    actions = ["rock", "paper", "scissors"]

    # Welcome message
    print("Hello stranger! Before I ask you if you'll play with me, I want to know your name. Also, you have to choose "
          "a name for me.")
    print("Oh, who am I? I am your computer silly, DUH!")

    # Learning player's name and what she/he wants to call computer
    print("-" * 200)
    players_name = input("Please enter your name: ")
    computers_name = input("Please give a name to me: ")
    print("Nice to meet you " + str(players_name) + " and thank you for the name that you gave me!")
    print("-" * 200)

    # Asking player if she/he wants to play
    while True:

        is_playing = input("Do you want to play rock-paper-scissors? You can answer shortly 'yes' or 'no'. ").lower()
        if is_playing not in ["yes", "no"]:
            print("You entered an invalid answer. Please write either 'yes' or 'no'.")
            continue  # Making sure the player gave a valid answer
        else:
            break

    if is_playing == "no":  # If the player doesn't want to play
        print("Oh, OK :(( You can come and play whenever you want, I am always here for you.")
        print("-" * 200)
    else:  # If the player wants to play

        # Asking if the player wants to read the rules of the game
        while True:  # Asking if the player wants to read rules
            is_reading_rules = input(
                "Do you want to read the rules of the game before we start? You can answer 'yes' or 'no'. ").lower()
            if is_reading_rules not in ["yes", "no"]:
                print("You entered an invalid answer. Please write either 'yes' or 'no'.")
                continue  # Making sure the player gave a valid answer
            else:
                break

        if is_reading_rules == "yes":  # If the player wants to read the rules
            print("-" * 200)
            print("#### RULES OF THE GAME: ROCK-PAPER-SCISSORS ####")
            print("The game rock-paper-scissors is a very popular game among people of all ages.")
            print("It is often used to make decisions, such as who gets the last piece of cake, who starts a game "
                  "first, or who goes to the store.")
            print("The basic rules are: Rock beats scissors, scissors beat paper, and paper beats rock.")
            print("In this version, you'll choose an action—rock, paper, or scissors—and the computer will choose its "
                  "action randomly.")
            print("Each game consists of rounds, and the game ends when one player wins 2 rounds.")
            print("After each game, you'll be asked if you want to play again.")
            print("-" * 200)
        else:  # If the player doesn't want to read the rules
            print("-" * 200)
            print("Ok, then let's move on to the game quickly.")

        # Main game loop
        while True:
            game_number += 1  # This way game number can be incremented by each iteration
            print(f"#################### GAME {game_number} ###############################")  # Title for the game

            while player_round_score < 2 and computer_round_score < 2:
                # As long as both of the players' scores are smaller than 2 (excluding) this block will be executed.
                round_number += 1  # Round number is incremented by each round thx to this code line ♡
                print(f"ROUND {round_number} of GAME {game_number}")

                # Taking choice of player
                while True:
                    choice_of_player = input("Please choose one of the actions: Rock, Paper, Scissors. Please be "
                                             "careful to write your choice correctly: ").lower()
                    if choice_of_player not in actions:
                        print("You entered an invalid action. Please write either 'rock', 'paper', or 'scissors'.")
                        continue  # Making sure the player gave a valid answer
                    else:
                        break

                # Taking choice of computer
                choice_of_computer = random.choice(actions)
                print(str(computers_name) + " has chosen " + choice_of_computer)

                # Evaluating the winner of the round
                evaluate_winner(choice_of_player, choice_of_computer)

                if winner == computers_name:
                    print(f"{computers_name} won this round. Congratulations {computers_name}!")
                elif winner == players_name:
                    print(f"{players_name} won this round. Congratulations {players_name}!")
                else:
                    print("The situation is a draw. For this round, we have no winner.")

                print(
                    f"Round score: {players_name} has {player_round_score} wins. {computers_name} has "
                    f"{computer_round_score} wins.")
                print("-" * 200)

            # Determine the winner of the game
            if player_round_score == 2:
                player_game_score += 1
                print(f"{players_name} won GAME {game_number}!")
            elif computer_round_score == 2:
                computer_game_score += 1
                print(f"{computers_name} won GAME {game_number}!")

            # Reset round scores for the next game
            player_round_score = 0
            computer_round_score = 0
            round_number = 0

            # Display the scoreboard
            display_scoreboard()

            # Asking if the players want to play another game
            while True:
                print("-" * 200)
                play_again = input("Do you want to play another game? Type 'yes' to continue or 'no' to stop: ").lower()
                if play_again not in ["yes", "no"]:
                    print("You entered an invalid answer. Please write either 'yes' or 'no'.")
                    continue  # Making sure the player gave a valid answer
                else:
                    break

            if play_again == "no":
                print("Thank you for playing! See you next time.")
                break

            # Computer decides if it wants to play again
            computer_response = random.choices(["yes", "no"], [0.8, 0.2])[0]
            print(f"{computers_name} says: '{computer_response}'")

            if computer_response == "no":
                print(f"{computers_name} doesn't want to play another game.")
                break

        print("Game Over. Final Scores:")
        display_scoreboard()

elif language_preference == "deutsch":  # German langugae implementation

    # possible actions (deu)
    actions = ["stein", "papier", "schere"]

    # Welcome message
    print(
        "Hallo Fremder! Bevor ich dich frage, ob du mit mir spielen willst, möchte ich deinen Namen wissen. Außerdem "
        "musst du einen Namen für mich aussuchen.")
    print("Oh, wer bin ich? Ich bin dein Computer, du Dummerchen, DUH!")

    # Learning player's name and what she/he wants to call computer
    print("-" * 200)
    players_name = input("Bitte geben Sie Ihren Namen ein: ")
    computers_name = input("Bitte geben Sie mir einen Namen: ")
    print("Nett dich kennenzulernen, " + str(players_name) + " und danke für den Namen, den du mir gegeben hast!")
    print("-" * 200)

    # Asking player if she/he wants to play
    while True:
        is_playing = input(
            "Willst du Schere-Stein-Papier spielen? Dann kannst du kurz mit „Ja“ oder „Nein“ antworten. ").lower()
        if is_playing not in ["ja", "nein"]:
            print("Ihre Antwort ist ungültig. Bitte schreiben Sie entweder „ja“ oder „nein“.")
            continue
        else:
            break

    if is_playing == "nein":
        print("Oh, OK :(( Du kannst kommen und spielen, wann immer du willst, ich bin immer für dich da.")
        print("-" * 200)
    else:
        # Asking if the player wants to read the rules of the game
        while True:
            is_reading_rules = input(
                "Möchten Sie die Spielregeln lesen, bevor wir beginnen? Sie können mit „Ja“ oder „Nein“ "
                "antworten. ").lower()
            if is_reading_rules not in ["ja", "nein"]:
                print("Ihre Antwort ist ungültig. Bitte schreiben Sie entweder „ja“ oder „nein“.")
                continue
            else:
                break

        if is_reading_rules == "ja":
            print("-" * 200)
            print("#### SPIELREGELN: SCHERE-STEIN-PAPIER ####")
            print("Das Spiel Schere-Stein-Papier ist bei Menschen jeden Alters sehr beliebt.")
            print("Es wird oft verwendet, um Entscheidungen zu treffen, z. B. wer das letzte Stück Kuchen bekommt, wer "
                  "zuerst ein Spiel beginnt oder wer zum Laden geht.")
            print("Die Grundregeln lauten: Stein schlägt Schere, Schere schlägt Papier und Papier schlägt Stein.")
            print("In dieser Version wählen Sie eine Aktion – Stein, Papier oder Schere – und der Computer wählt seine "
                  "Aktion nach dem Zufallsprinzip.")
            print("Jedes Spiel besteht aus Runden und endet, wenn ein Spieler 2 Runden gewinnt.")
            print("Nach jedem Spiel werden Sie gefragt, ob Sie erneut spielen möchten.")
            print("-" * 200)
        else:
            print("-" * 200)
            print("Ok, dann lasst uns schnell zum Spiel kommen.")

        # Main game loop
        while True:
            game_number += 1
            print(f"#################### SPIEL {game_number} ###############################")

            while player_round_score < 2 and computer_round_score < 2:
                round_number += 1
                print(f"RUNDE {round_number} von SPIEL {game_number}")

                # Taking choice of player
                while True:
                    choice_of_player = input(
                        "Bitte wählen Sie eine der Aktionen: Schere, Stein, Papier. Achten Sie bitte darauf, Ihre "
                        "Auswahl richtig zu schreiben: ").lower()
                    if choice_of_player not in actions:
                        print(
                            "Sie haben eine ungültige Aktion eingegeben. Bitte schreiben Sie entweder „Stein“, „Papier“"
                            " oder „Schere“.")
                        continue
                    else:
                        break

                # Taking choice of computer
                choice_of_computer = random.choice(actions)
                print(str(computers_name) + " hat " + choice_of_computer + " ausgewählt.")

                # Evaluating the winner of the round
                evaluate_winner(choice_of_player, choice_of_computer)

                if winner == computers_name:
                    print(f"{computers_name} hat diese Runde gewonnen. Herzlichen Glückwunsch, {computers_name}!")
                elif winner == players_name:
                    print(f"{players_name} hat diese Runde gewonnen. Herzlichen Glückwunsch, {players_name}!")
                else:
                    print("Das Ergebnis ist unentschieden. Für diese Runde gibt es keinen Gewinner.")

                print(
                    f"Rundenergebnis: {players_name} hat {player_round_score} Siege. {computers_name} hat "
                    f"{computer_round_score} Siege.")
                print("-" * 200)

            # Determine the winner of the game
            if player_round_score == 2:
                player_game_score += 1
                print(f"{players_name} gewann SPIEL {game_number}!")
            elif computer_round_score == 2:
                computer_game_score += 1
                print(f"{computers_name} gewann SPIEL {game_number}!")

            # Reset round scores for the next game
            player_round_score = 0
            computer_round_score = 0
            round_number = 0

            # Display the scoreboard
            display_scoreboard()

            # Asking if the players want to play another game
            while True:
                print("-" * 200)
                play_again = input(
                    "Möchten Sie ein anderes Spiel spielen? Geben Sie „Ja“ ein, um fortzufahren, oder „Nein“, um "
                    "aufzuhören: ").lower()
                if play_again not in ["ja", "nein"]:
                    print("Ihre Antwort ist ungültig. Bitte schreiben Sie entweder „ja“ oder „nein“.")
                    continue
                else:
                    break

            if play_again == "nein":
                print("Vielen Dank fürs Spielen! Bis zum nächsten Mal.")
                break

            # Computer decides if it wants to play again
            computer_response = random.choices(["ja", "nein"], [0.8, 0.2])[0]
            print(f"{computers_name} sagt: '{computer_response}'")

            if computer_response == "nein":
                print(f"{computers_name} möchte nicht spielen mehr.")
                break

        print("Spiel vorbei. Endergebnisse:")
        display_scoreboard()

else:  # Turkish language implementation

    # possible actions (tur)
    actions = ["taş", "kağıt", "makas"]

    # Welcome message
    print(
        "Merhaba yabancı! Benimle oyun oynaıp oynamayacağını sormadan önce adını öğrenmek isterim. Ayrıca benim için de"
        " bir isim seçmelisin.")
    print("Aa, ben kim miyim? Ben senin bilgisayarınım şapşik!")

    # Learning player's name and what she/he wants to call computer
    print("-" * 200)
    players_name = input("Lütfen adını yaz:  ")
    computers_name = input("Lütfen bana bir isim ver: ")
    print("Tanıştığımıza memnun oldum " + str(players_name) + " ve bana verdiğin isim için de teşekkür ederim!")
    print("-" * 200)

    # Asking player if she/he wants to play
    while True:
        is_playing = input(
            "Taş-kağıt-makas oynamak ister misin? Kısaca 'evet' ya da 'hayır' olarak yanıtlayabilirsin. ").lower()
        if is_playing not in ["evet", "hayır"]:
            print("Geçersiz bir yanıt girdin. Lütfen ya 'evet' ya da 'hayır' yaz.")
            continue
        else:
            break

    if is_playing == "hayır":
        print("Aa, tamam o zaman.:(( Ne zaman istersen tekrar gelebilirsin, senin için daima buradayım.")
        print("-" * 200)
    else:
        # Asking if the player wants to read the rules of the game
        while True:
            is_reading_rules = input(
                "Başlamadan önce oyunun kurallarını okumak ister misin? 'Evet' veya 'hayır' şeklinde yanıt "
                "verebilirsin. ").lower()
            if is_reading_rules not in ["evet", "hayır"]:
                print("Geçersiz bir yanıt girdin. Lütfen ya 'evet' ya da 'hayır' yaz.")
                continue
            else:
                break

        if is_reading_rules == "evet":
            print("-" * 200)
            print("#### OYUNUN KURALLARI: TAŞ-KAĞIT-MAKAS ####")
            print("Taş-kağıt-makas oyunu her yaştan insan arasında oldukça popüler bir oyundur.")
            print(
                "Genellikle son pasta dilimini kimin alacağı, oyuna kimin önce başlayacağı veya kimin markete gideceği "
                "gibi kararlar almak için kullanılır.")
            print("Temel kurallar şunlardır: Taş makası yener, makas kağıdı yener ve kağıt taşı yener.")
            print(
                "Bu versiyonda, bir eylem seçersiniz—taş, kağıt veya makas—ve bilgisayar kendi eylemini rastgele seçer.")
            print("Her oyun turlardan oluşur ve oyun herhangi bir oyuncu 2 tur kazandığında sona erer.")
            print(
                "Her oyundan sonra, tekrar oynamak isteyip istemediğiniz sorulur.")
            print("-" * 200)
        else:
            print("-" * 200)
            print("Tamam o zaman hemen oyuna geçelim.")

        # Main game loop
        while True:
            game_number += 1
            print(f"#################### OYUN {game_number} ###############################")

            while player_round_score < 2 and computer_round_score < 2:
                round_number += 1
                print(f"OYUN {game_number} / TUR {round_number}")

                # Taking choice of player
                while True:
                    choice_of_player = input(
                        "Lütfen şu hareketlerden birini seç: Taş, kağıt, makas. Lütfen cevabını doğru yazmaya dikkat "
                        "et. ").lower()
                    if choice_of_player not in actions:
                        print("Geçersiz bir yanıt girdin. Lütfen ya 'taş' ya 'kağıt' ya da 'makas' yaz.")
                        continue
                    else:
                        break

                # Taking choice of computer
                choice_of_computer = random.choice(actions)
                print(str(computers_name) + " şunu seçti: " + choice_of_computer)

                # Evaluating the winner of the round
                evaluate_winner(choice_of_player, choice_of_computer)

                if winner == computers_name:
                    print(f"{computers_name} bu turu kazandı. Tebrikler {computers_name}!")
                elif winner == players_name:
                    print(f"{players_name} bu turu kazandı. Tebrikler {players_name}!")
                else:
                    print("Durum berabere. Bu tur için bir kazananımız yok.")

                print(
                    f"Tur sonu skor durumu: {players_name} --> {player_round_score} : {computers_name} --> "
                    f"{computer_round_score}")
                print("-" * 200)

            # Determine the winner of the game
            if player_round_score == 2:
                player_game_score += 1
                print(f"OYUN {game_number}, {players_name} tarafından kazanıldı!")
            elif computer_round_score == 2:
                computer_game_score += 1
                print(f"OYUN {game_number}, {computers_name} tarafından kazanıldı!")

            # Reset round scores for the next game
            player_round_score = 0
            computer_round_score = 0
            round_number = 0

            # Display the scoreboard
            display_scoreboard()

            # Asking if the players want to play another game
            while True:
                print("-" * 200)
                play_again = input("Bir kez daha oynamak ister misin? Devam etmek için 'evet', durmak için 'hayır' "
                                   "yaz. ").lower()
                if play_again not in ["evet", "hayır"]:
                    print("Geçersiz bir yanıt girdin. Lütfen ya 'evet' ya da 'hayır' yaz.")
                    continue
                else:
                    break

            if play_again == "hayır":
                print("Oynadığın için teşekkürler! Bir dahaki sefere görüşmek üzere.")
                break

            # Computer decides if it wants to play again
            computer_response = random.choices(["evet", "hayır"], [0.8, 0.2])[0]
            print(f"{computers_name} şöyle cevapladı: '{computer_response}'")

            if computer_response == "hayır":
                print(f"{computers_name} yeniden oynamak istemiyor.")
                break

        print("Oyun bitti. Son skorlar:")
        display_scoreboard()