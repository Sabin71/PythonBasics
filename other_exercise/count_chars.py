phrase = ("hellooo ")
vowels_counts = {}

for letter in phrase.lower():
    vowels_counts.setdefault(letter, 0)
    vowels_counts[letter] +=1

print(vowels_counts)

print("---------------------------")

print(f"{__file__} is completed")