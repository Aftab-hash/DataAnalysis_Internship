import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Medical_Appointment_No_Shows.csv")

# 2. Inspect the dataset
print("Initial shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
print(df.info())

# 3. Check for missing values
print("Missing values:\n", df.isnull().sum())

# 4. Remove duplicate rows
df = df.drop_duplicates()

# 5. Standardize categorical text values
# For 'Gender' and 'No-show' columns
df['Gender'] = df['Gender'].str.upper().str.strip()
df['No-show'] = df['No-show'].str.strip().str.capitalize()

# 6. Convert date columns to datetime
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], errors='coerce')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], errors='coerce')

#7. Format to 'dd-mm-yyyy HH:MM:SS+00:00'
# Custom formatting function to get '+00:00' style
def format_datetime_with_colon(dt):
    if pd.isna(dt):
        return None
    return dt.strftime('%d-%m-%Y %H:%M:%S') + dt.strftime('%z')[:3] + ':' + dt.strftime('%z')[3:]

# Apply the custom format
df['ScheduledDay'] = df['ScheduledDay'].apply(format_datetime_with_colon)
df['AppointmentDay'] = df['AppointmentDay'].apply(format_datetime_with_colon)

# 8. Rename columns to be clean and uniform
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 9. Check and fix data types
# Ensure 'age' is integer
df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

# 10. Check again for missing values after conversion
print("Missing values after type conversion:\n", df.isnull().sum())

# 11. Optional: Drop rows with critical missing values (e.g., missing age or appointment date)
df = df.dropna(subset=['age', 'appointmentday'])

# 12. Save cleaned dataset
df.to_csv("Cleaned_Medical_Appointment_No_Shows.csv", index=False)

