stack = []
brackets = "()[]{}"

s = "{[()]}"

for char in s:
    if char in "([{":
        stack.append(char)
    else:
        if not stack:
            print("Invalid")
            break

        top = stack.pop()

        if (char == ")" and top != "(") or \
           (char == "]" and top != "[") or \
           (char == "}" and top != "{"):
            print("Invalid")
            break
else:
    if not stack:
        print("Valid")
    else:
        print("Invalid")
