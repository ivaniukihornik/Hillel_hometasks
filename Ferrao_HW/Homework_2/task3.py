# 3
# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = {'Mandy Miller', 'Jack Richmond', 'Jonny Fade', 'Amelia Lincoln', 'Richard Dawson', 'Ben Diamond'}
poker_blacklist = {'Jack Richmond', 'Amanda Spurs', 'Jonny Fade', 'Jayden Sanches', 'Kortney Gilmor', 'Ben Diamond'}
alcohol_blacklist = {'Felix Well', 'Paul Madisson', 'Nick Close', 'Jack Richmond', 'Ben Diamond'}

all_blacklist = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)

print(all_blacklist)
