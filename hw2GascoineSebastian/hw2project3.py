# avg2.py
#   A simple program to average two exam scores
#   Illustrates use of multiple input

def main():
    print("This program computes the average of exam scores.")
    examscores = 0;
    exams = eval(input("Enter how many exams there are: "))
    for x in range(1, (exams+1)):
        score = eval(input("Enter in score one by one: "))
        examscores += score
        score = 0

    average = examscores/exams 
    print("The average of the scores is:", average)

main()
