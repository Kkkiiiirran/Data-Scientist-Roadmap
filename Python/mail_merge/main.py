PLACEHOLDER ="[name]"
with open("Python/mail_merge/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Python/mail_merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("Python/mail_merge/Output/ReadyToSend/letter_for_"+stripped_name+".txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
