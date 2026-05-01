import csv
import os

def pick(num,choice) -> None:
    """
    Function takes the users vote and stores it within the CSV file "voting.csv".
    :param num: This is the voters ID.
    :param choice: This is the voters selected canidate.
    """
    file = "voting.csv"

    try:
        num = int(num)
    except:
        raise TypeError
    
    if num < 1 or num > 9999:
        raise TypeError
    
    if choice not in [1, 2]:
        raise NameError
    
    if not os.path.exists(file):
        open(file, 'w').close()


    with open (file, 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for line in content:
            if line[0] == str(num):
                raise ValueError
     
    with open('voting.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([num, choice])

def total() -> int:
    """
    Function used to return current voting polls, when called, function reads the current
    total votes for the canidate Jane, John, and total votes for both canidates stored in "voting.csv"
    These values are returned as integers.
    """
    jane = 0
    john = 0
    with open('voting.csv', 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=',')
        for line in content:
            if line[1] == "1":
                jane += 1
            elif line[1] == "2":
                john += 1

    total = jane + john
    return jane, john, total


      

        

