# Task 2

class Team:
    def __init__(self, country_name, name_of_player, age, no_of_matches, batting_avg, bowling_avg):
        self.country_name = country_name
        self.name_of_player = name_of_player
        self.age = age
        self.no_of_matches = no_of_matches
        self.batting_avg = batting_avg
        self.bowling_avg = bowling_avg

    def display(self):
        print(f"{self.country_name:<15} {self.name_of_player:<20} {self.age:<5} {self.no_of_matches:<20} {self.batting_avg:<15} {self.bowling_avg:<15}")

# team array
teams = [
    Team("India", "Sachin ", 30, 295, 45.51, 53.00),
    Team("Australia", "Ricky", 28, 160, 41.00, 67.00),
    Team("England", "Joe Root", 31, 230, 40.95, 30.00),
    
]

# Table
print("\n")
print(f"{'Country Name':<15} {'Name of Player':<20} {'Age':<5} {'No. of Matches':<20} {'Batting Avg.':<15} {'Bowling Avg.':<15}")
print("-" * 90)
for team in teams:
    team.display()
