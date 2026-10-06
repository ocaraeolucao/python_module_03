import random


def gen_player_achievements(master_list):
    num_achievements = random.randint(6, 10)
    return set(random.sample(master_list, num_achievements))


def main():
    print("=== Achievement Tracker System ===")
    master_list = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer', 'Hidden Path Finder'
    ]
    master_set = set(master_list)
    alice = gen_player_achievements(master_list)
    bob = gen_player_achievements(master_list)
    charlie = gen_player_achievements(master_list)
    dylan = gen_player_achievements(master_list)
    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    all_distinct = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_distinct}")
    common = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}")
    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")
    print(f"\nAlice is missing: {master_set.difference(alice)}")
    print(f"Bob is missing: {master_set.difference(bob)}")
    print(f"Charlie is missing: {master_set.difference(charlie)}")
    print(f"Dylan is missing: {master_set.difference(dylan)}")


if __name__ == "__main__":
    main()
