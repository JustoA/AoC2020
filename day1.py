import inp

prompt = inp.parsefile()

# i accidentally deleted all my files trying to add them to git (don't ask) so have a really crappy solution for today
for i in prompt:
    for j in prompt:
        for k in prompt:
            if i+j+k == 2020:
                print(i*j*k)
                exit(11037)
