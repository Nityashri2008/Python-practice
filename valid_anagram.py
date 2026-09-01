s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not an Anagram")
else:
    count = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        count[char] = count.get(char, 0) - 1

    if all(value == 0 for value in count.values()):
        print("Anagram")
    else:
        print("Not an Anagram")
