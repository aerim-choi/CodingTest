S = input()
ch = S[0]
S0 = list(filter(lambda ch: ch!='', S.split('0')))
S1 = list(filter(lambda ch: ch!='',S.split('1')))

print(min(len(S0),len(S1)))