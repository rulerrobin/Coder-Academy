skills = {
    'python': 1,
    'ruby': 2,
    'bash': 4,
    'git': 8,
    'html': 16,
    'tdd': 32,
    'css': 64,
    'javascript': 128
}

# get input from user of skills
user_input = input("What code skills do you have please separate with commas no spaces e.g. CSS,HTML,Git(nothing to exit)")
user_skills = []
skill = ''

for input in user_input:
    if input != ',':  # gets input and separates between comma and words
        skill += input
    else:
        user_skills.append(skill)
        skill = ''
user_skills.append(skill)
# make non case sensitive
for i in range(len(user_skills)):
    user_skills[i] = user_skills[i].lower()
    
# print(user_skills)# debug
# print (skill) # debug

# check score for inputted skills
score = 0
for skill in user_skills:
    if skill in skills:
        score += skills[skill]

# give user score check if user wants to input more skills if yes repeat
print(f"Your overall coding skill score is {score}.")
# if not list out the skills not selected and how much each is worth

suggestions = []
for skill, value in skills.items(): # contains the key-value pairs of the dictionary, as tuples in a list
    if skill not in user_skills:
        suggestions.append(f"{skill} (+{value})")
if suggestions:
    print("You may want to learn:")
    for suggestion in suggestions:
        print(suggestion)