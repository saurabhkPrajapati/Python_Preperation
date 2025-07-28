import pandas as pd

initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
                'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
                'Age': [42, 52, 36, 21, 23],
                'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}

df = pd.DataFrame(initial_data, columns=['First_name', 'Last_name',
                                         'Age', 'City'])

new_data = {0: "Shyam",
            2: "Riya",
            3: "Jitender"}

# this returns none
# dont use assignment to df['First_name']
df["First_name"].update(new_data)
print(df)
