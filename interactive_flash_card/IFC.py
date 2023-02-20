import pandas as pd
from learner import *


print("Enter csv file path or Q anytime to exit")

# sample csv path:
# /home/.../Documents/interactive_flash_cards/abc.csv


fileInput = str(input())

if fileInput == "Q":
    exit()

df = pd.read_csv(fileInput)

learner(0, df)


