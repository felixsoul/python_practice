import pandas as pd
import os

current_dir = os.path.dirname(__file__)
print(current_dir)
file_path = os.path.join(current_dir,
                         "../xl/course_participants.xlsx")
print(pd.read_excel(file_path))
