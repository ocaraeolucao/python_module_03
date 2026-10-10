import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    initial_players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
                       'john', 'kevin', 'Liam']
    print(f"\nInitial list of players: {initial_players}")
    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")
    capitalized_only = [name for name in initial_players if name ==
                        name.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}")
    score_dict = {name:  random.randint(0, 1000) for name in all_capitalized}
    print(f"\nScore dict: {score_dict}")
    avg = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(avg, 2)}")
    high_scores = {name: score for name, score in score_dict.items()
                   if score > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
