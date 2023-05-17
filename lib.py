import os
import random
import string

def clear():
    input("Натисніть ENTER щоб продовжити\n")
    os.system("cls")

def intro():
    print("\n\n\n\t\t\tШИБЕНИЦЯ\n\n\n")
    clear()

def rules():
    print("У вас є шість спроб щоб відгадати слово\nЯкщо чоловічок повністю намалювався то ви програли")





def choose_word():
    words = {
        "apple": "Фрукт який круглий та зазвичай червоний або зелений",
        "banana": "Фрукт який викривлений та має жовту шкірку",
        "orange": "Цитрусовий фрукт який зазвичай оранжевий",
        "strawberry": "Ягода яка зазвичай червона й має кісточки на поверхні", 
        "grapefruit":"Великий цитрусовий фрукт з жовтою або рожевою шкіркою",
        "pineapple": "Тропічний фрукт з жорсткою та колючою шкіркою і має жовту та солодку м'якоть"
        }
    word = random.choice(list(words.keys()))
    return word, words[word]

def hangman():
    word, description = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        clear()
        print(description)
        print("\nAttempts remaining: ", attempts)
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "*"
        print(display_word)

        if display_word == word:
            print("Congratultaions! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Потрібно одну букву")
            continue


        if guess in guessed_letters:
            print("You've already guessed this letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong letter!")
            if attempts == 0:
                print("game over! The word was: ", word)
                break


        # print("\t\t  __________")
        # print("\t\t  |       \|")
        # print("\t\t  |        |")
        # print("\t\t           |")
        # print("\t\t           |")
        # print("\t\t           |")
        # print("\t\t           |")
        # print("\t\t           |")
        # print(word_g)
       
    
        

