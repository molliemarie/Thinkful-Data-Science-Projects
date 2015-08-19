# Translate the Markov chain below to a matrix. 

df = pd.DataFrame({'Bull': [.9, .15, .25], 
                   'Bear': [.075, .8, .25],
                   'Stagnant': [.025, .05, .5]
                  }, 
                  index=["Bull", "Bear", "Stagnant"])

# What are the transition probabilities after 1 transition?

print(df)

#            Bear  Bull  Stagnant
# Bull      0.075  0.90     0.025
# Bear      0.800  0.15     0.050
# Stagnant  0.250  0.25     0.500

# What are the transition probabilities after 2 transitions? 
df2=df
print('After two transitions:')
print(df.dot(df2))

df2=df
for i in range(1): df2 = df2.dot(df2)
print('After two transitions:')
print(df2)

# After two transitions:
#              Bear    Bull  Stagnant
# Bull      0.13375  0.8275   0.03875
# Bear      0.66375  0.2675   0.06875
# Stagnant  0.34375  0.3875   0.26875
# After two transitions:
#              Bear    Bull  Stagnant
# Bull      0.13375  0.8275   0.03875
# Bear      0.66375  0.2675   0.06875
# Stagnant  0.34375  0.3875   0.26875

# After three transitions:
df2=df
print('After three transitions:')
print(df2.dot(df2.dot(df2)))

df2=df
for i in range(2): df2 = df2.dot(df)
print('After three transitions:')
print(df2)

# After three transitions:
#              Bear    Bull  Stagnant
# Bull      0.17875  0.7745   0.04675
# Bear      0.56825  0.3575   0.07425
# Stagnant  0.37125  0.4675   0.16125
# After three transitions:
#               Bear     Bull  Stagnant
# Bull      0.212775  0.73555  0.051675
# Bear      0.499975  0.42555  0.074475
# Stagnant  0.372375  0.51675  0.110875

df2=df
print('After four transitions:')
print(df2.dot(df2.dot(df2.dot(df2))))

df2=df
for i in range(3): df2 = df2.dot(df)
print('After four transitions:')
print(df2)

# After four transitions:
#               Bear     Bull  Stagnant
# Bull      0.212775  0.73555  0.051675
# Bear      0.499975  0.42555  0.074475
# Stagnant  0.372375  0.51675  0.110875
# After four transitions:
#               Bear     Bull  Stagnant
# Bull      0.212775  0.73555  0.051675
# Bear      0.499975  0.42555  0.074475
# Stagnant  0.372375  0.51675  0.110875

# After 5? 
df2=df
print('After five transitions:')
print(df.dot(df.dot(df.dot(df.dot(df2)))))

df2=df
for i in range(4): df2 = df2.dot(df)
print('After four transitions:')
print(df2)


# After five transitions:
#               Bear     Bull  Stagnant
# Bull      0.238305  0.70683  0.054865
# Bear      0.450515  0.47661  0.072875
# Stagnant  0.364375  0.54865  0.086975
# After four transitions:
#               Bear     Bull  Stagnant
# Bull      0.238305  0.70683  0.054865
# Bear      0.450515  0.47661  0.072875
# Stagnant  0.364375  0.54865  0.086975

# After 10? 
df2=df
for i in range(9): df2 = df2.dot(df)
print('After ten transitions:')
print(df2)


# After ten transitions:
#               Bear      Bull  Stagnant
# Bull      0.295793  0.643289  0.060919
# Bear      0.343096  0.591585  0.065319
# Stagnant  0.326594  0.609186  0.064220

# After 
df2=df
for i in range(47): df2 = df2.dot(df)
print('After forty-eight transitions:')
print(df2)

# What are the steady state probabilities 
# (try raising the matrix to a higher and numbers until the probabilities converge)?

# After forty-eight transitions, all of the probabilities converge. See below

df2=df
for i in range(46): df2 = df2.dot(df)
print('After forty-seven transitions:')
print(df2)

df2=df
for i in range(47): df2 = df2.dot(df)
print('After forty-eight transitions:')
print(df2)

# After forty-seven transitions:
#             Bear      Bull  Stagnant
# Bull      0.3125  0.625000    0.0625
# Bear      0.3125  0.624999    0.0625
# Stagnant  0.3125  0.625000    0.0625
# After forty-eight transitions:
#             Bear   Bull  Stagnant
# Bull      0.3125  0.625    0.0625
# Bear      0.3125  0.625    0.0625
# Stagnant  0.3125  0.625    0.0625


# Can you a name some real-life examples that could be modeled by Markov chains? 
# Black jack, google search 

# Can you name examples that cannot be treated as Markov chains?
# ?

# Can you name an example of finite probabilistic states that cannot be modeled as Markov chains?
# ?



