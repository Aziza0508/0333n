import random

with open("nemes.txt", "r") as f:
    names = f.read().splitlines()

# Generates bigrams
def generate_bigrams(string):
    bigrams = []
    for i in range(len(string) - 1):
        if i == 0:
            bigrams.append(f'^{string[i]}')
        bigrams.append(f'{string[i]}{string[i+1]}')
        if i == len(string) - 2:
            bigrams.append(f'{string[i+1]}$')
    return bigrams

# Get a random starting letter from the names
starting_letters = [name[0] for name in names]
starting_letter = random.choice(starting_letters)

# Calculate the count of each bigram starting with the chosen letter
bigram_counts = {}
for name in names:
    if name[0] != starting_letter:
        continue
    bigrams = generate_bigrams(name)
    for bigram in bigrams:
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1

# Calculating probabilities
bigram_probabilities = {}
total_bigrams = sum(bigram_counts.values())
for bigram, count in bigram_counts.items():
    probability = count / total_bigrams
    bigram_probabilities[bigram] = probability

# generating random
name = starting_letter
while name[-1] != '$':
    possible_bigrams = [bigram for bigram in bigram_probabilities.keys() if bigram.startswith(name[-1])]
    chosen_bigram = random.choices(possible_bigrams, [bigram_probabilities[bigram] for bigram in possible_bigrams])[0]
    next_letter = chosen_bigram[-1]
    name += next_letter

name = name[1:-1]

# Print out the random name
print(f"Random name: {name}")
