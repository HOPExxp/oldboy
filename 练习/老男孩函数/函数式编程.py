movie_people = ['my','sb_my','you','sb_you']
res = filter(lambda x:x.startswith('sb'),movie_people)
print(list(res))