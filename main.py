import requests
from termcolor import colored
import sys

def make_request_and_check(url, data):
    response = requests.post(url, json=data)
    response_data = response.json()

    if "valid" in response_data and response_data["valid"] == True:
        return True
    elif "message" in response_data and response_data["message"] == "Wrong answer":
        return False

def main():
    game_urls = [
        "https://loldle.apimeko.link/games/classic/answer",
        "https://loldle.apimeko.link/games/quote/answer",
        "https://loldle.apimeko.link/games/ability/answer",
        "https://loldle.apimeko.link/games/emoji/answer",
        "https://loldle.apimeko.link/games/splash/answer"
    ]
    
    with open("champions.txt", "r") as file:
        champions = file.read().splitlines()

    games = ["champion", "quote", "ability", "emoji", "splash art"]

    for game_idx, game_url in enumerate(game_urls):
        print()
        print(colored(f"I'm guessing the {games[game_idx]}...", "yellow"))
        found_correct_champ = None

        for champion in champions:
            data = {
                "name": champion,
                "utc": 2
            }

            valid = make_request_and_check(game_url, data)

            if valid:
                found_correct_champ = champion
                break
            else:
                sys.stdout.write("\r" + " " * 100)
                sys.stdout.write("\r" + colored(f"Wrong {games[game_idx]} {champion}", "red"))
                sys.stdout.flush()

        if found_correct_champ is not None:
            sys.stdout.write("\r" + " " * 100)
            print()
            print(colored(f"The correct answer for the {games[game_idx]} is", "green"), colored(found_correct_champ, "green"))

    print()
    print(colored("See you soon! :)", "yellow"))
    print()

if __name__ == "__main__":
    main()
