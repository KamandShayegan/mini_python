import pandas as pd
import random

print("Enter csv file path or Q anytime to exit")

# sample csv path:
# /home/.../Documents/interactive_flash_cards/abc.csv

fileInput = str(input())

if fileInput == "Q":
    exit()

df = pd.read_csv(fileInput)

df_len = len(df)

def learner(value):
    if value == 0:
        rand_int = random.randint(1, df_len-1)
    else:
        rand_int = value

    all_value = df.loc[[rand_int],:]
    
    question_col = all_value['Question']
    
    answer_col = all_value['Answer']
    
    question = question_col.values[0] 
    
    answer = answer_col.values[0]

    print("* ", question, " *")

    users_answer = str(input())

    users_answer = users_answer.lower()

    answer = answer.lower()

    if users_answer == "q":
        print("\n See you later ;)")
        exit()
    elif users_answer == answer:
        print("Good Job! \n\n")
        learner(0)
    else:
        print("Oops! The correct answer is: ", answer, "\n")
        learner(rand_int)
    
    


learner(0)