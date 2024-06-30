# Purpose of Quiz:
# The purpose of this quiz is to help test the knowledge of Six60 fans from Aotearoa New Zealand.
# Six60 is a famous band that formed in NZ and topped global charts with their music. 
# Six60 shows great representation of people from NZ, giving a glimmer of hope for young artists from NZ.
#make a introoooooooooooo just make it so it gives a lil info
print("Welcome to the Six60 Quiz!")
print("This quiz is designed to test your knowledge of Six60, the famous band from Aotearoa New Zealand.")
print("Hope this quiz can educate you and even surprise the die-hearted fans.")
print("IMPORTANT: PLEASE ONLY USE THE FOLLOWING (A, B, C, or D).")
print("Good luck!")
print("~~~~~~~~~~~~~~~~~~~~~~")  # Separator line 

# List of questions (make less mrs said too much)
questions = [
    "What year was Six60 formed?",
    "Which university did the founding members of Six60 attend?",
    "What is the title of Six60's debut studio album?",
    "Which Six60 song includes the lyrics 'Don't forget your roots, my friend'?",
    "Who is the lead vocalist of Six60?",
    "Which member of Six60 plays the drums?",
    "What is the title of Six60's highest-charting single in New Zealand?",
    "Which Six60 song features a collaboration with Norwegian DJ and record producer Kygo?",
    "Which New Zealand city is Six60 originally from?",
    "What is the title of Six60's third studio album, released in 2019?"
]

# Dictionary of choices
choices = {
    1: ["A. 2004", "B. 2006", "C. 2008", "D. 2010"],
    2: ["A. University of Auckland", "B. University of Otago", "C. Victoria University of Wellington", "D. University of Canterbury"],
    3: ["A. 'Six60 (2011)'", "B. 'Six60 (2013)'", "C. 'Six60 (2015)'", "D. 'Six60 (2017)'"],
    4: ["A. 'Rise Up'", "B. 'Forever'", "C. 'Don't Forget Your Roots'", "D. 'White Lines'"],
    5: ["A. Matiu Walters", "B. Marlon Gerbes", "C. Eli Paewai", "D. Ji Fraser"],
    6: ["A. Matiu Walters", "B. Marlon Gerbes", "C. Eli Paewai", "D. Chris Mac"],
    7: ["A. 'Special'", "B. 'Rise Up'", "C. 'Don't Forget Your Roots'", "D. 'White Lines'"],
    8: ["A. 'Vibes'", "B. 'Don't Give It Up'", "C. 'Ghost'", "D. 'Fade Away'"],
    9: ["A. Auckland", "B. Wellington", "C. Christchurch", "D. Dunedin"],
    10: ["A. 'Six60 (2019)'", "B. 'Six60 III'", "C. 'Six60: The Next Chapter'", "D. 'Sixty60'"]
}

# List of correct answers
correct_answers = [
    "C",  # 2008
    "B",  # University of Otago
    "A",  # 'Six60 (2011)'
    "C",  # 'Don't Forget Your Roots'
    "A",  # Matiu Walters
    "C",  # Eli Paewai
    "D",  # 'White Lines'
    "D",  # 'Fade Away'
    "D",  # Dunedin
    "B"   # 'Six60 III'
]

# Function to get user input and check against correct answer
def get_user_input(question_num):
    while True:
        answer = input(f"Your answer for question {question_num}: ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

user_answers = []  # List to store user answers

# Display each question, get user input, and provide feedback
for i, question in enumerate(questions, 1):
    print(f"{i}. {question}")
    for choice in choices[i]:
        print(choice)
    user_answer = get_user_input(i)
    user_answers.append(user_answer)

    # Check user's answer against correct answer
    if user_answer == correct_answers[i-1]:
        print("Correct!")
    else:
        print("Wrong!")
    print("~~~~~~~~~~~~~~~~~~~~~~") #make the seperator line actuly work remember to indenttttttt

# Final score calculation and message (made the score with in-betweens)
score = sum(user_answer == correct_answers[i] for i, user_answer in enumerate(user_answers))
#convert weird percentages to actual proper scores
print(f"\nYour score is {score} out of {len(questions)}")
if score == len(questions):
    print("Excellent! You're a true Six60 fan!")
elif score >= 8:
    print("Great job! You know a lot about Six60.")
elif score >= 5:
    print("Good effort! You have a decent knowledge of Six60.")
elif score >= 2:
    print("You might want to listen to more Six60 songs.")
else:
    print("You know nothing about Six60.")