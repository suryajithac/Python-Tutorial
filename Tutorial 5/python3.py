import pandas as pd
info = {'Student Name': ['arun', 'bala'], 'Score': [60, 80]}
sheet = pd.DataFrame(info)
sheet.to_excel('student_data.xlsx', index=False)
print("Excel file created successfully.")