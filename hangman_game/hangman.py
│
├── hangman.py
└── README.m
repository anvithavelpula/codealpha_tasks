import random
words = ["apple", "tiger", "python", "robot", "school"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6
print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter")
print("_ " * len(word))
while wrong_guesses < max_attempts:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    if "_" not in display:
        print("🎉 You won! The word is:", word)
        break
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - wrong_guesses}")
    print("------------------------")
if wrong_guesses == max_attempts:
    print("💀 Game Over! The word was:", word)