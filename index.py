def main():
    # credit to Dhyanam for this part
    tutorGroup = input("Enter the name of your tutor group: ").upper()
    tutorGroupCheck = input("Enter the name of tutor group again: ").upper()
    while tutorGroup != tutorGroupCheck:
        print("1st Entry does not match 2nd Entry")
        tutorGroup = input("Enter the name of your tutor group: ").upper()
        tutorGroupCheck = input("Enter the name of tutor group again: ").upper()
        
    tutorGroup = tutorGroup.upper()

    numStudents = input('How many students are in ' + tutorGroup + '? ')
    while True:
        if not numStudents.isnumeric():
            numStudents = input("Please enter a valid number: ")
        elif int(numStudents) > 35:
            numStudents = input("Your class cannot have more than 35 students, please enter a valid number: ")
        elif int(numStudents) < 2: # CHANGE TO 28, 2 IS FOR TESTING
            numStudents = input("Your class cannot have less than 28 students, please enter a valid number: ")
        else:
            break
    numStudents = int(numStudents)

    numCandidates = input("How many candidates are there in " + tutorGroup + "? ")
    while True:
        if not numCandidates.isnumeric():
            numCandidates = input("Please enter a valid number: ")
        elif int(numCandidates) > 4:
            numCandidates = input("There cannot be more than 4 candidates, please enter a valid number: ")
        elif int(numCandidates) < 1:
            numCandidates = input("There must be at least one candidate, please enter a valid number: ")
        else:
            break
    numCandidates = int(numCandidates)

    candidates = {}
    for i in range(numCandidates):
        candidateNum = i + 1
        # [CANDIDATE_NAME] = NUM_OF_VOTES - this is how it looks in the candidates dictionary

        candidateName = input("What is the name of candidate #" + str(candidateNum) + "? ")
        while True:
            if not candidateName.isalpha(): # their name isn't completely letters
                candidateName = input("Please enter a valid candidate name: ")
            else:
                break
        candidates[candidateName] = 0

    print("-"*50)
    print("Voting".center(50))
    print("-"*50)

    while True:
        for candidateName, _ in candidates.items():
                candidates[candidateName] = 0

        usedKeys = [] # list: stores all the used keys

        abstentions = 0 # integer: stores total abstentions
        votes = 0 # integer: stores total votes

        for i in range(numStudents): # loop through every student
            print("\n" * 50)
            print("-"*50)
            print("VOTING".center(50))
            print("-"*50)
            studentKey = input("What is the code your teacher gave you? ")
            while True:
                if not studentKey.isnumeric(): # the key is not a valid number
                    print("\n" * 50)
                    print("-"*50)
                    print("VOTING".center(50))
                    print("-"*50)
                    print("Must be an actual number!")
                    studentKey = input("What is the code your teacher gave you? ")
                elif int(studentKey) in usedKeys: # the key the student gave has already been used!
                    print("\n" * 50)
                    print("-"*50)
                    print("VOTING".center(50))
                    print("-"*50)
                    print("You have already voted! Please let the next person vote.")
                    studentKey = input("What is the code your teacher gave you? ")
                else:
                    break
            usedKeys.append(int(studentKey)) # Add current key to the array of used keys

            print("\n")
            print("  Candidates  ".center(50, "-"))

            candidateCount = 1 # integer: will store the total amount of candidates there are
            pseudoCandidates = [] # list: will store the names of candidates to easily loop through

            for candidateName, _ in candidates.items():
                print(str(candidateCount).ljust(3), candidateName.title()) # print the candidate number on the left, their name next to it
                pseudoCandidates.append(candidateName) # add their name to this list for ease of access
                candidateCount += 1
            print("-"*50)
            candidateVote = input("Choose a number (1 - " + str(candidateCount - 1) + ") to vote for that person, or type 'A' to abstain: ")
            while True:
                if candidateVote.upper() == 'A': # student validly inputted an abstention
                    break
                elif not candidateVote.isnumeric(): # if the vote is not a number, we don't need to check it
                    candidateVote = input("Please enter a valid number: ")
                elif int(candidateVote) > candidateCount - 1 or int(candidateVote) < 1: # if the vote is outside of the valid range
                    candidateVote = input("Please enter a valid vote: ")
                else:
                    break
            if candidateVote.upper() == "A": # Student Abstained
                abstentions += 1 # Increment total abstentions
            else: # Student validly voted for a candidate
                candidates[pseudoCandidates[int(candidateVote) - 1]] += 1 # Add a vote to that certain candidate
                votes += 1 # Increment total votes
        
        # All students have voted
        print("\n"*50)
        print("-"*50)
        print(("Voting results for: " + tutorGroup).center(50))
        print("-"*50)

        print(str(votes) + " total votes")
        print(str(abstentions) + " total abstentions")

        print("-"*50)
        winners = []
        for candidateName, numOfVotes in candidates.items():
            print(candidateName.title().ljust(20) + 'received ' + str(numOfVotes / (votes if votes > 0 else abstentions) * 100) + '% of the votes.') # print the percentage of how many votes the candidate got
            if len(winners) == 0:
                winners.append(candidateName) # if there is no other winner, add this candidate as a winner to begin with
                continue
            if candidates[winners[0]] < numOfVotes: # if the first candidate in the array has less votes than the current one, 
                winners = []                        # that means that all the candidates have less votes than the current one.
                winners.append(candidateName)       # so, empty the array and add the current candidate to it
                continue
            elif candidates[winners[0]] == numOfVotes:  # if the first candidate in the array has the same number of votes
                winners.append(candidateName)           # than the current one, it's a tie. add the current one without
                continue                                # getting rid of the old one


        print("-"*50)
        print("Therefore, the winner" + ("s are..." if len(winners) > 1 else " is..."))
        
        for i in range(len(winners)):
            print(winners[i].title())

        print("-"*50)

        if len(winners) > 1: # If there is more than one winner - there is a tie
            tieVote = input("Would you like to re-vote to determine a winner? (Y/N) ")
            while True:
                if not tieVote.isalpha(): # Check if only valid letters are inputted
                    tieVote = input("Must be a letter (Y/N): ")
                elif not tieVote.lower()[0] in ['y', 'n']: # 
                    tieVote = input("Must be a letter (Y/N): ")
                else:
                    break
            if tieVote.lower()[0] == 'y':
                print("\n"*50)
                print("  Restarting Vote  ".center(50, "-"))
            else:
                break
        else:
            break
            
while True:
    main()

    # round up to 200