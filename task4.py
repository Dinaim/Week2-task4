guests = ["Nurayim", "Dastan", "Janar"]
letter = "You are invited to home party "
print(letter + guests[0])
print(letter + guests[1])
print(letter + guests[2])

a = guests.pop()
print(guests)
print(a)
b = guests.append("Asan")
print(guests)

print(letter + guests[0])
print(letter + guests[1])
print(letter + guests[2])