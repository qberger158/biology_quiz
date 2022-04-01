# Author: Quentin Bergeron
# File: multiple_choice.py
# Date started: 30 September 2021
# Description: create a multiple choice quiz that focuses on molecular biology questions.
# The quiz then gives the user a percentage score of how many questions they answered
# correctly.

def start_quiz():
    total_attempts = []
    correct_attempts = 0
    question_number = 1

    for key in questions:
        print("-----------------------------------------------------------------------------------")
        print(key)
        for each_choice in choices[question_number-1]:
            print(each_choice)
        attempt = input("Enter (A, B, C, or D): ")
        attempt = attempt.upper()
        total_attempts.append(attempt)

        correct_attempts += check_answer(questions.get(key), attempt)
        question_number += 1

    show_grade(correct_attempts, total_attempts)


def check_answer(answer, attempt):
    if answer == attempt:
        print("You are CORRECT!")
        return 1
    else:
        print("Sorry, that is not correct.")
        return 0

def show_grade(correct_attempts, total_attempts):
    print("*********************************************************************************")
    print("Grade  Review                  ")
    print("*********************************************************************************")

    print("Correct Answers: ", end="")
    for x in questions:
        print(questions.get(x), end=" ")
    print()

    print("Your Answers: ", end="")
    for x in total_attempts:
        print(x, end=" ")
    print()

    score = int((correct_attempts/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def retake_quiz():
    reply = input("Would you like to retake the quiz?")
    reply = reply.upper()

    if reply == "YES":
        return True
    else:
        return False

questions = {
    "1. The human body is composed of: ": "B",
    "2. Which of the following statements is incorrect?: ": "D",
    "3. The 5' capping process creates what type of linkage?: ": "A",
    "4. Which of the following is not a DNA base?: ": "E",
    "5. Which of the following is the enzyme responsible for unwinding helical DNA \n"
    "for replication?: ": "C",
    "6. What does splicing do?: ": "D",
    "7. Which of the following is not an RNA base?": "B",
    "8. What occurs at the ribosomes?: ": "C",
    "9. Amino acids are the building blocks of: ": "A",
    "10. Which enzyme is responsible for stitching together Okazaki fragments?: ": "C"
}

choices = [["A. 88% Oxygen, 3% Carbon, 4.7% Hydrogen, 0.5% Nitrogen\n" 
            "B. 65% Oxygen, 18.5% Carbon, 9.5% Hydrogen, 3.2% Nitrogen\n"
            "C. 10% Oxygen, 33.7% Carbon, 48.2% Hydrogen, Nitrogen 4.3%\n" 
            "D. 63% Oxygen, 21.8% Carbon, 11% Hydrogen, 0.4% Nitrogen"],
           ["A. When protein synthesis starts, a fraction of a DNA molecule unwinds and unzips\n" 
            "B. DNA molecules are in the form of a double helix\n"
            "C. As a result of DNA replication, one DNA molecule becomes two identical molecules\n"
            "D. Every DNA molecule is one single gene"],
           ["A. 5'-5'", "B. 5'-3'", "C. 3'-3'", "D. 3'-5'"],
           ["A. Cytosine", "B. Thymine", "C. Guanine", "D. Adenine", "E. Uracil"],
           ["A. Guanylyl transferase", "B. Polymerase", "C. Helicase", "D. Ligase"],
           ["A. Remove mutated regions of primary transcript RNA\n"
            "B. Removes exons and conserves introns\n" 
            "C. Add multiple adenosine bases to the end of primary RNA transcript\n" 
            "D. Removes introns and conserves exons"],
           ["A. Cytosine", "B. Thymine", "C. Adenine", "D. Uracil"],
           ["A. DNA is damaged or changed", "B. DNA molecule storage\n" 
            "C. Production of proteins", "D. Production of mRNA"],
           ["A. Proteins", "B. carbohydrates", "C. DNA", "D. lipids", "E. RNA"],
           ["A. Primase", "B. Helicase", "C. Ligase", "D. Amylase", "E. Lipase"]]

start_quiz()

while retake_quiz():
    start_quiz()

print("Thank you for your participation with this quiz!")


