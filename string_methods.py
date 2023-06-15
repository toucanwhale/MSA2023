sentence = "I have a dog. my dog is cute. do you want a dog?"
letters = len(sentence)
print(letters)
counter = 0
dog_count= 0

while counter <= letters:
    print(sentence.index("dog", counter))
    counter = counter+1