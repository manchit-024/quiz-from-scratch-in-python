#----------------QUIZ-------------------




print("===== ENTER YOUR DETAILS =====")

father_name = input("Father's Name: ")
your_name = input("Your Name: ")
mother_name = input("Mother's Name: ")
mob_no=int(input("enter your mobile no:"))
d_o_b=int(input("enter your date of birth:"))
edu=input("enter your current education:")
stu_id=int(input("enter your student id:"))



age = int(input("enter your age: "))

if age <= 18:
    print("you are not eligible for quiz")
else:

    
    chances = 3

    while chances > 0:
        password = input("enter password: ")
        confirm_password = input("confirm password: ")

        if password == confirm_password:
            print("password verified successfully!")
            break
        else:
            chances -= 1
            print("password does not match.")
            print("attempts left:", chances)

    if chances == 0:
        print("password verification failed.")

    else:

        
        t1=input("do you accept the terms and conditions? (yes/no): ")
        t2=input("do you agree to the quiz rules? (yes/no): ")
        t3=input("do you accept the privacy policy? (yes/no): ")
        t4=input("do you accept out time limitation?(yes/no):")
        t5=input("do you limited chances?(yes/no)")
        t6=input("you cant leave it in between!(yes/no)")
        t7=input("you have to complete quiz!(yes/no)")

        if t1 == "yes" and t2 == "yes" and t3 == "yes" and t4=="yes"and t5=="yes"and t6=="yes"and t7=="yes":

            print("you are eligible for quiz.")

            score = 0

            questions = [
                "what is python?",
                "who invented python?",
                "what is the use of pyhton?",
                "what is the lastest version of python?",
                "pyhton is known as?",
                "what is the extension used for python file?",
                "who built python langauge?"
            ]

            answers = [
                "a programming language",
                "guido van rossum",
                "both a and b",
                "python 3",
                "interpreted language",
                ".py",
                "guido van rossum"
            ]

            options = [
                ["a programming language", "a snake", "a movie"],
                ["guido van rossum", "elon musk", "mark zuckerberg"],
                ["web development", "data analysis", "both a and b"],
                ["python 2", "python 3", "python 4"],
                ["interpreted language", "compiled language", "both"],
                [".py", ".pyth", ".pt"],
                ["guido van rossum", "bjarne stroustrup", "dennis ritchie"]
            ]

            for i in range(questions):

                print("Question", i + 1)
                print(questions[i])

                for op in options[i]:
                    print("-: ", op)

                attempt = 3

                while attempt > 0:
                    user_answer = input("your answer: ")

                    if user_answer== answers[i]:
                        print("correct answer!")
                        score += 1
                        break
                    else:
                        attempt -= 1

                        if attempt > 0:
                            print("wrong answer!")
                            print("attempts left:", attempt)
                        else:
                            print("correct answer is:", answers[i])

            print("===== QUIZ COMPLETED =====")
            print("your score =", score, "out of", (questions))

        
