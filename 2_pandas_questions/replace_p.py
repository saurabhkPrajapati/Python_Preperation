# Creating new dataframe
import pandas as pd
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
				'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
				'Age': [42, 52, 36, 21, 23],
				'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}

df = pd.DataFrame(initial_data, columns = ['First_name', 'Last_name',
													'Age', 'City'])

# Create new column using dictionary
new_data = { "Ram":"Shyam",
			"Tina":"Riya",
			"Jeetu":"Jitender" }

print(df, end ="\n\n")

# combine this new data with existing DataFrame
# df['First_name'] = df['First_name'].replace(new_data)
df = df.replace(new_data)
print(df)


# importing pandas as pd
import pandas as pd
df = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})
index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]
df.index = index_
print(df)
df_updated = df.replace(to_replace='[nN]ew', value='New_', regex=True)
print(df_updated)

