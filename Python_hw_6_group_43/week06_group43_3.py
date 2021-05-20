# Assignment 3

# import necessary modules
import csv
import random

# Say hello and ask for name
name = input("Hello Happy Quiz Friend! What is your name? ")

# try to get number of questions as user integer input from specified range
n_questions = None
while type(n_questions) != int or n_questions not in range(5,8):
    try:
        # ask how many questions user wants to answer
        n_questions = input("Alright, good to see you " + name + ". How many questions do you want to answer (min 5, max 7)? ")
        n_questions = int(n_questions)
    except ValueError:
        print(str(n_questions) + " is not an integer.")

# ask questions and save answers
with open("questions_answers.csv", "r") as questions:
    csv_reader = csv.DictReader(questions)
    score = 0
    count = 0

    # get all questions and ask one by one
    for line in csv_reader:
        # get answer as keyboard input
        answer = None
        while answer not in ["a","b","c"]:
            try:
                answer = input(line["question"] + "\n" + line["answer a"] + "\n" + line["answer b"] + "\n" + line["answer c"] + "\n")
                print("")
            except ValueError:
                print("This is not a valid answer.")

        # Tell the user if the answer is right; if yes add to score
        if answer == line["correct"]:
            print("You're answer is right!\n")
            score += 1
        else:
            print("You're answer is wrong!\n")
        count += 1

        # end of quiz: present score and save result to csv file
        if count == n_questions:
            # present user score
            print("You got " + str(score) + " out of " + str(n_questions) + " right!")

            # save score
            with open("result.csv", "a") as result:
                csv_writer = csv.DictWriter(result, fieldnames=["name", "score"])
                #csv_writer.writeheader()
                csv_writer.writerow({"name":name, "score":str(score)})

            break
