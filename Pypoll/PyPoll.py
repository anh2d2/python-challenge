# importing dependencies
import csv
import os

# setting file paths
file_to_load = os.path.join("Pypoll", "Resources", "election_data.csv")
file_to_output = os.path.join("Pypoll", "analysis", "election_analysis.txt")

# setting vote count variable
total_votes = 0

# setting up lists and dicitoinaries
candidate_options = []
candidate_votes = {}

# tracking for winner
winning_candidate = ""
winning_count = 0

# reading csv
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # setting the header
    header = next(reader)

    for row in reader:

        # loader
        print(". ", end=""),

        # iterate vote count
        total_votes = total_votes + 1

        # setting name for candidate
        candidate = row[2]

        # if name not found
        if candidate not in candidate_options:

            # adds new name to list
            candidate_options.append(candidate)

            # starts count for new name
            candidate_votes[candidate] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# exporting results
with open(file_to_output, "w") as txt_file:

    # sending final vote count to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # saving results to txt file
    txt_file.write(election_results)

    # reading through totals to find winner
    for candidate in candidate_votes:

        # finding vote count and percentage for each candidate
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # finding the winner
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # printing results to terminal
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # saving results to txt file
        txt_file.write(voter_output)

    # printing winner to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # saving winner to txt file
    txt_file.write(winning_candidate_summary)
