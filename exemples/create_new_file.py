#open text file
text_file = open("data.txt", "w")

#write string to file
text_file.write('Python Tutorial by TutorialKart.')

#close file
text_file.close()

# or
with open('data.txt', 'w') as text_file:
    text_file.write('Python Tutorial by TutorialKart.')
