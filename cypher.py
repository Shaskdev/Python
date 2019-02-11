# Create a simple Ceasar Cypher

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 12
newMessage = ''

message = input('please enter a message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        #print('the new character is : ', newCharacter)
        newMessage += newCharacter
        #print(newMessage)
    else:
        newMessage += character

print('Your new message is', newMessage)
