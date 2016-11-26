def checkio(words):
    words=words.split(" ")
    counter=0
    for word in words:
        counter+=1
        if word.isdigit():
            counter=0
        if counter==3:
            return True
    return False
