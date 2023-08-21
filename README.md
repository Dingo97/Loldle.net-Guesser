# 🤔 What's Loldle Game?
In this game, the challenge revolves around guessing the names of League of Legends champions. Each time the game is initiated, a new set of champions is randomly selected. These champions are divided into seven distinct attributes: Gender, Position, Species, Resource, Range Type, Region, and Release Year.
https://loldle.net/

# 💡 What's Loldle Guesser?
This Python program interacts with a game API that presents various challenges related to League of Legends champions. The challenges involve guessing different attributes of the champions, such as their names, quotes, abilities, emojis, and splash arts.

## 💬 Features

- The program reads a list of champion names from a text file called `champions.txt`.
- It iterates through different game URLs, each corresponding to a specific challenge.
- For each game, the program sends POST requests with champion names as parameters to check if the response is valid or not.
- If a correct answer is found, the program displays the correct champion name and proceeds to the next stage.
- When an incorrect answer is received, it updates the incorrect champion name displayed on the same line using the `sys` module to manage console output.
- Once a correct answer is found, the incorrect champion name is cleared, and the program proceeds to the next stage.
- The program provides feedback on whether the correct champion was identified or not for each stage.

## 🐱‍💻 Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Verify that the `champions.txt` file is in the same directory as the `main.py`.
4. Run the program using `python main.py`.

## 💻 Dependencies

- `requests`: Used to make HTTP requests to the game API.
- `termcolor`: Used to display colored text in the console.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Dingo97/Loldle.net-Guesser/blob/main/LICENSE) file for details.

## 🎇 Acknowledgements

This project was created for fun and educational purposes. It is not affiliated with or endorsed by Riot Games, the developer of League of Legends, Pimeko, the developer of LoLdle.

Feel free to contribute or modify the code as needed!
