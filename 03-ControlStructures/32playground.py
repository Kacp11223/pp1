

survey = {"Interested in computer science:":None,"Playing computer games:":None,"Has an Instagram account:":None}

for key,value in survey.items():
    answer = input(key)
    if answer == 'Y':
        survey[key] = True
    if answer == 'N':
        survey[key] = False

for key,value in survey.items():
    print(f"{key} {survey[key]}")