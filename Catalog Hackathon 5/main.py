import hashlib
import getpass
import random
import os
from tabulate import tabulate

candidates = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

votes = {}
otp_storage = {}
voter_ids_used = set()

def generate_otp(voter_id):
    otp = random.randint(100000, 999999)
    otp_storage[voter_id] = otp

    otp_filename = f"otp_{voter_id}.txt"
    with open(otp_filename, "w") as otp_file:
        otp_file.write(str(otp))

    print(f"OTP has been generated and stored in {otp_filename}.")

def validate_otp(voter_id, entered_otp):
    if voter_id in otp_storage and otp_storage[voter_id] == entered_otp:
        return True
    return False

def hash_vote(voter_id, choice):
    vote_data = f"{voter_id}:{choice}"
    return hashlib.sha256(vote_data.encode()).hexdigest()

def cast_vote(voter_id):
    print("\n--- Cast Your Vote ---")
    print("Select a candidate:")
    for num, name in candidates.items():
        print(f"{num}: {name}")

    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        if choice not in candidates:
            print("Invalid choice. Vote not recorded.")
            return
    except ValueError:
        print("Invalid input. Vote not recorded.")
        return

    print(f"\nYou have selected: {candidates[choice]}")
    confirm = input("Press 'C' to confirm your choice: ").strip().lower()

    if confirm == 'c':
        votes[voter_id] = (choice, hash_vote(voter_id, choice))
        print("Your vote has been successfully cast.\n")
        print("----------------------------------------------------------------------------------")

    else:
        print("Vote cancelled. You can re-enter your vote.")
        print("----------------------------------------------------------------------------------")

def validate_votes():
    print("\n--- Validate Votes ---")
    for voter_id, (choice, hashed_vote) in votes.items():
        reentered_choice = int(input(f"Voter {voter_id}, please re-enter your vote to validate: "))
        if hash_vote(voter_id, reentered_choice) == hashed_vote:
            print("Vote is valid.")
        else:
            print("Vote has been tampered with!")
            return False
    return True

def display_results():
    print("\n--- Voting Results ---")

    results = {name: 0 for name in candidates.values()}
    for voter_id, (choice, _) in votes.items():
        results[candidates[choice]] += 1

    table_data = []
    for candidate, vote_count in results.items():
        table_data.append([candidate, vote_count])

    table = tabulate(table_data, headers=["Candidate", "Votes"], tablefmt="grid")
    print(table)

def main():
    voter_count = int(input("Enter the number of voters: "))

    while len(voter_ids_used) < voter_count:
        voter_id = getpass.getpass(prompt="Enter your voter ID (hidden): ")

        if voter_id in voter_ids_used:
            print("This voter ID has already cast a vote. You cannot vote again.\n")
            print("----------------------------------------------------------------------------------")
            continue

        generate_otp(voter_id)
        entered_otp = int(input(f"Enter the OTP found in otp_{voter_id}.txt: "))

        if validate_otp(voter_id, entered_otp):
            print("OTP validated successfully.")
            cast_vote(voter_id)
            voter_ids_used.add(voter_id)
        else:
            print("Invalid OTP. You cannot cast your vote.")

    if validate_votes():
        display_results()
    else:
        print("Votes validation failed. Voting results will not be displayed.")

if __name__ == "__main__":
    main()
