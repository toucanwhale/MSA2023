sentence = "iegiedvnoekfrgnerwp dogs. aswijfwikaognjkdsfgvneakf dogs. fnjerdwigfnsdik dog."

dog_count = 0
start_index = 0
more_dogs = True
while more_dogs:
    found_index = sentence.find("dog", start_index)
    if found_index != -1:
        dog_count += 1
        start_index = found_index +1
    else:
        more_dogs = False

print(f"Number of Dogs: {dog_count}")