import pandas as pd

# Correct file path formatting
df = pd.read_csv(r'C:\Users\ashish thakral\OneDrive\Desktop\DA\Absenteeismdata.csv')

# Display all columns and rows
pd.options.display.max_columns = None
pd.options.display.max_rows = None

# Print the DataFrame information
#print(df.info())

# Check if the 'ID' column exists and drop it if it does
if 'ID' in df.columns:
    df = df.drop('ID', axis=1)
else:
    print("Column 'ID' not found in the DataFrame.")

# Print the DataFrame to verify changes
#print(df)

pd.unique(df['Reason for Absence']) #sorted(df['Reason for Absence'].unique())

reason_columns=pd.get_dummies(df['Reason for Absence'],drop_first=True)
reason_columns['check']=reason_columns.sum(axis=1)
reason_columns['check'].sum(axis=0)
reason_columns['check'].unique()

#print(reason_columns)

reason_columns=reason_columns.drop(['check'],axis=1)

df.columns.values
reason_columns.columns.values

df=df.drop(['Reason for Absence'],axis=1)
df

#reason_columns.loc[:,1:14].max(axis=1)
#reason_columns.loc[:,15:17]
#reason_columns.loc[:,18:21]
#reason_columns.loc[:,19:22]

reason_type1=reason_columns.loc[:,1:14].max(axis=1)
reason_type2=reason_columns.loc[:,15:17].max(axis=1)
reason_type3=reason_columns.loc[:,18:21].max(axis=1)
reason_type4=reason_columns.loc[:,19:22].max(axis=1)
#print(reason_type2)

df=pd.concat([df,reason_type1,reason_type2,reason_type3,reason_type4],axis=1)
df.columns.values
column_names= ['Date' ,'Transportation Expense' ,'Distance to Work' ,'Age',
'Daily Work Load Average' ,'Body Mass Index', 'Education' ,'Children' ,'Pets',
'Absenteeism Time in Hours' ,'reason_1','reason_2','reason_3','reason_4' ]
df.columns = column_names
df.head()
column_names_reordered=['reason_1','reason_2','reason_3','reason_4','Date' ,'Transportation Expense' ,'Distance to Work' ,'Age',
'Daily Work Load Average' ,'Body Mass Index', 'Education' ,'Children' ,'Pets',
'Absenteeism Time in Hours']
df=df[column_names_reordered]
df.head()

df_reason_mod=df.copy()
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], dayfirst=True, errors='coerce', infer_datetime_format=True)

# Display the DataFrame information
#df_reason_mod.info()

# Print the first value of the 'Date' column to verify
df_reason_mod['Date'][0].month

list_months=[]

for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)
list_months

df_reason_mod['Month Values']=list_months
#print(df_reason_mod.head(20))
df_reason_mod['Education'].unique()
df_reason_mod['Education'].value_counts()
df_reason_mod['Education'] = df_reason_mod['Education'].map({1:0, 2:1, 3:1, 4:1})
print(df_reason_mod['Education'].value_counts())