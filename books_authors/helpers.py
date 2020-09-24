import json

# Read notes from the file. Returns dict.
def readNotes():
    with open("./data.json", "r") as notes:
        data = json.load(notes)
        return data



# Add a note to the file
def addNote(note, author, rating):

    #Check for correct usage
    if type(note) != str or type(author) != str or type(rating) != int:
        print("Usage: addNote(note, author, rating)")
        exit(1)
    elif rating > 10:
        print("Max rating is 10")
        exit(1)

    #Add a new note
    newNote = {'author_name': author, 'note': note, 'rating': rating}
    data = readNotes()
    with open("./data.json", "w") as notes:       
        data['notes'].append(newNote)
        json.dump(data, notes, indent=4)
        print(f"You've added a note '{newNote['note']}' about {newNote['author_name']} to the list!")
    exit(0)



# Print notes to console
def printNotes():
    data = readNotes()
    print('All Notes:')
    for note in data['notes']:
        print(f"- {note['note']} (about {note['author_name']}) with {note['rating']} rating")



# Get author with the highest rating. Returns array of strings
def highestRated():
    data = readNotes()
    highestRating = 0

    #Retrieve highest rating possible
    for note in data['notes']:
        if note['rating'] > highestRating:
            highestRating = note['rating']
    
    #Retrieve highest rated authors
    highestRatedAuthors = list(filter(lambda note: note['rating'] == highestRating, data['notes']))
    
    return [note['author_name'] for note in highestRatedAuthors]



# Get author with the lowest rating. Returns array of strings
def lowestRated():
    data = readNotes()
    lowestRating = 10

    #Retrieve lowest rating possible
    for note in data['notes']:
        if note['rating'] < lowestRating:
            lowestRating = note['rating']
    
    #Retrieve lowest rated authors
    lowestRatedAuthors = list(filter(lambda note: note['rating'] == lowestRating, data['notes']))
    
    return [note['author_name'] for note in lowestRatedAuthors]
    


# Get average rating among all authors. Returns integer
def avgRating():
    data = readNotes()
    ratings = list([int(note['rating']) for note in data['notes']])
    return sum(ratings) / len(ratings)
