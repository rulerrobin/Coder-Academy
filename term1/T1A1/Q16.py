# declare list of skills with a given score for each
skills = [
    {'code': 'python', 'score': 1},
    {'code': 'ruby', 'score': 2},
    {'code': 'bash', 'score': 4},
    {'code': 'git', 'score': 8},
    {'code': 'html', 'score': 16},
    {'code': 'tdd', 'score': 32},
    {'code': 'css', 'score': 64},
    {'code': 'javascript', 'score': 128}
]

# get input from user of skills
selection = input ("What code skills do you have (nothing to exit)")
# compare input to skills and add score from list of skills if not part of list ask if anything else they use or to end
for option in skills:
    if option['code'].lower() == selection.lower():
        print (f"{option['code']} is {option['score']} points")

# remove from list to not be selected anymore
# give user score check if user wants to input more skills if yes repeat
# if not list out the skills not selected and how much each is worth

