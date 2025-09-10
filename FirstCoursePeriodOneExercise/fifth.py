sender_id = input()
Content = input()

Is_sender_id_valid = lambda Id :  not Id.isdigit()

def ContentValid(text : str) -> bool :
    counter = 0
    for ch in text :
        if ch != " " and (not ch.isalpha()) and (not ch.isdigit()) :
            counter += 1
    if counter >= len(text) / 2  and text.lower().count("spam") :
        return False
    return True

if Is_sender_id_valid(sender_id) and ContentValid(Content):
    print("Not Spam")
elif not Is_sender_id_valid(sender_id) and ContentValid(Content) :
    print("Invalid Sender")
elif Is_sender_id_valid(sender_id) and not ContentValid(Content) :
    print("Invalid Content")
else:
    print("Fully Invalid")