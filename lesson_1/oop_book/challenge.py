class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, new_votes):
        self.votes += new_votes

class Election:
    
    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        for candidate in self.candidates:
            print (f'{candidate.name}: {candidate.votes} votes')
        
        winner = max(self.candidates, key=lambda candidate: candidate.votes)
        vote_total = sum(candidate.votes for candidate in self.candidates)
        print(f'\n{winner.name} won: {100 * winner.votes/vote_total:.1f}% of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()