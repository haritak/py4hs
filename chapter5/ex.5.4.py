import random
import datetime


'''
Ασκηση 5.4
Mερικές ενδεικτικές ερωτήσεις: 
1. Ποιά από τις παρακάτω μέρες δεν πηγαίνουμε σχολείο; 
2. Ποια μέρα είναι πριν ή μετά τη x; 
3. Αν σήμερα η μέρα είναι x,ποια ημέρα εννοούμε όταν λέμε 
“αύριο”, “μεθαύριο”, “χθες” ή “προχθές”; 
4. Αν σήμερα η μέρα είναι x, τι μέρα θα είναι σε n μέρες; 
5. Αν σήμερα η μέρα είναι y, πόσες ημέρες έχουν περάσει από τη x; 
6. Βάλτε στη σειρά τις παρακάτω ημέρες της εβδομάδας.
'''


workdays = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή"]
weekend = ["Σάββατο", "Κυριακή"]
weekdays = workdays + weekend
three_weeks = weekdays*3

daypredicate = [ "αύριο", "μεθαύριο", "χθές", "προχθές"]
daypredicate_increment = [ 1, 2, -1, -2]

def showChoices(message, choices):
    print("")
    print(message)
    i=1
    for c in choices:
        print("(",i,")-",c,sep="", end=" ")
        i+=1

    print(":")

def getAnswer(choices):
    answer=''
    while answer not in choices:
        answer=int(input())
        if answer>0 and answer<=len(choices):
            answer=choices[answer-1]
        else:
            print("Δώσε μου κάποιο νούμερο μεταξύ του 1 και του",
                    len(choices))

    return answer


def question4():
    today_idx = random.randint(7,14)

    afterbefore = random.randint(-7,+7)
    correct_index = today_idx+afterbefore

    message = "είναι μετά απο " + str(afterbefore)
    if afterbefore<0:
        message = "ήταν πριν απο " + str(abs(afterbefore))

    showChoices("Αν σήμερα είναι "+three_weeks[today_idx]+" τότε τί μέρα "+message+" μέρες;", 
            weekdays)
    answer=getAnswer(weekdays)

    return answer==three_weeks[correct_index]

def question3():
    pi = random.randint(0, len(daypredicate))

    message = daypredicate[pi]
    if daypredicate_increment[pi]>0:
        message = "θα είναι "+message
    else:
        message = "ήταν "+message

    today = datetime.datetime.today().weekday()
    correct_index = 7+today+daypredicate_increment[pi]

    random_weekdays = weekdays.copy()
    random.shuffle( random_weekdays )
    showChoices("Ποιά μέρα " +message+";", random_weekdays)
    answer=getAnswer(random_weekdays)

    return answer==three_weeks[correct_index]

    
def question2(after=True):
    correct_index = random.randint(7,14)

    message='πριν'
    message_index=-1
    if after :
        message='μετά'
        message_index = correct_index-1
    else:
        message='πριν'
        message_index = correct_index+1

    random_weekdays = weekdays.copy()
    random.shuffle( random_weekdays )

    showChoices("Ποιά μέρα είναι "+ message+" την "+ three_weeks[message_index], 
            random_weekdays)
    answer=getAnswer(random_weekdays)

    return answer==three_weeks[correct_index]

def question1():
    correct = random.sample(weekend,1)
    choices = random.sample(workdays, 3) + correct
    random.shuffle(choices)
    showChoices("Ποιά μέρα απο τις παρακάτω δεν πάμε σχολείο;",
            choices)

    answer = getAnswer(choices)
    return answer==correct[0]



    
if question4():
    print("Σωστά")
else:
    print("Λάθος")

if question3():
    print("Σωστά")
else:
    print("Λάθος")


if question2():
    print("Σωστά")
else:
    print("Λάθος")

if question2(False):
    print("Σωστά")
else:
    print("Λάθος")


if question1():
    print("Σωστά")
else:
    print("Λάθος")


