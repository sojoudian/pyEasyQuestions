votes_for_A = 0
votes_for_B = 0
total_votes = 5  # Set the total number of votes allowed

for _ in range(total_votes):
    vote = input("Vote for Candidate A or Candidate B: ").strip().upper()
    if vote == "A":
        votes_for_A += 1
    elif vote == "B":
        votes_for_B += 1
    else:
        print("Invalid vote. Please vote for either Candidate A or Candidate B.")
        continue  # Skips to the next iteration without counting the vote

if votes_for_A > votes_for_B:
    winner = "Candidate A"
elif votes_for_B > votes_for_A:
    winner = "Candidate B"
else:
    winner = "No winner, it's a tie!"

print(f"Voting finished. {winner} wins!")

