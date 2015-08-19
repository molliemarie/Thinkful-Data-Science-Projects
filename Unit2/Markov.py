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
print('After two transitions:')
print(df.dot(df))

# After two transitions:
#              Bear    Bull  Stagnant
# Bull      0.13375  0.8275   0.03875
# Bear      0.66375  0.2675   0.06875
# Stagnant  0.34375  0.3875   0.26875

# After 5? 
print('After five transitions:')
print(df.dot(df.dot(df.dot(df.dot(df)))))

# After five transitions:
#               Bear     Bull  Stagnant
# Bull      0.238305  0.70683  0.054865
# Bear      0.450515  0.47661  0.072875
# Stagnant  0.364375  0.54865  0.086975

# After 10? 
print('After ten transitions:')
print(df.dot(df.dot(df.dot(df.dot(df.dot(df.dot(df.dot(df.dot(df.dot(df))))))))))

# After ten transitions:
#               Bear      Bull  Stagnant
# Bull      0.295793  0.643289  0.060919
# Bear      0.343096  0.591585  0.065319
# Stagnant  0.326594  0.609186  0.064220

# What are the steady state probabilities 
# (try raising the matrix to a higher and numbers until the probabilities converge)?

# Can you a name some real-life examples that could be modeled by Markov chains? 
# Black jack, google search 

# Can you name examples that cannot be treated as Markov chains?
# ?

# Can you name an example of finite probabilistic states that cannot be modeled as Markov chains?
# ?



