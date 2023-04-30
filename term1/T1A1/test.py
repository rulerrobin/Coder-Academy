# # Define the skill options and their scores
# skills = {
#     'Python': 1,
#     'Ruby': 2,
#     'Bash': 4,
#     'Git': 8,
#     'HTML': 16,
#     'TDD': 32,
#     'CSS': 64,
#     'JavaScript': 128
# }

# # Get the user's skills as input
# user_input = input("Enter your skills separated by commas (e.g. Python, Git, CSS): ")
# user_skills = []
# skill = ''
# for char in user_input:
#     if char != ',':
#         skill += char
#     else:
#         user_skills.append(skill)
#         skill = ''
# user_skills.append(skill)

# # Calculate the user's skill score
# score = 0
# for skill in user_skills:
#     if skill in skills:
#         score += skills[skill]

# # Print the user's overall skill score
# print(f"Your overall coding skill score is {score}.")

# # Print suggestions for skills to learn
# # suggestions = []
# # for skill, value in skills.items():
# #     if value > score:
# #         suggestions.append(f"{skill} (+{value - score})")
# # if suggestions:
# #     print("You may want to learn:")
# #     for suggestion in suggestions:
# #         print(suggestion)
# # else:
# #     print("You're a coding wizard! Keep it up!")

# declare list of skills with a given score for each

