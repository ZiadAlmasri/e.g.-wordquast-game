import random
fruits = ["apple", "banana", "orange", "grapes"]
countries = ["tunisia", "palestine", "qatar", "jordan", "iraq"]
print(" Welcome to the Ziad brain game!")
while True:
    print("\nChoose a category:")
    print("1 - Fruits ")
    print("2 - Countries ")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        word = random.choice(fruits)
        break
    elif choice == "2":
        word = random.choice(countries)
        break
    else:
        print(" thats no a number! Please enter only 1 or 2.")
hidden = ["_"] * len(word)
used_letters = []
print("\nThe word has", len(word), "letters.")
print("Current word:", " ".join(hidden))
print("You have up to 10 tries.\n")
for attempt in range(10):
    letter = input(f"Try {attempt + 1}/10 - Enter a letter: ").lower()
    if letter in used_letters:
        print(" Do you have a fish memory? you tried this letter!")
        continue
    used_letters.append(letter)
    if letter in word:
        print(f" Correct! The letter '{letter}' exists.")
        positions = []
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
                positions.append(i + 1)
        print("Positions:", positions)
    else:
        print(f" Wrong! The letter '{letter}' doesn't exist.")
    print("Used letters:", ", ".join(used_letters))
    print("Current word:", " ".join(hidden))
    print("----------------------")
    if "_" not in hidden:
        print("\n Great! You found all letters!")
        break
guess = input("\nNow enter the full word: ").lower()
if guess == word:
    print(" Correct! You guessed the word!")
else:
    print(" Wrong! The word was:", word)
    print(" pay 2£ to play again")
