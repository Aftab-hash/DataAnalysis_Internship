#-> Task 1: Data Cleaning and Preprocessing Summary.
<br>
#-> Objective: Clean and prepare the raw Medical_Appointment_No_Shows.csv dataset for analysis.
<br>
#-> Summary of Changes and Fixes Made:<br>
#-> Step	Action	Description

1.	Loaded dataset	Loaded the raw dataset using pandas.read_csv() for efficient handling.
<br>
2.	Inspected structure	Checked initial shape, column names, and data types using .shape, .columns, and .info() to understand the dataset.
<br>
3.	Handled missing values	Used .isnull().sum() and errors='coerce' in datetime conversion to safely convert or mark invalid entries as missing (NaT).
<br>
4.	Removed duplicates	Dropped 100% identical rows using df.drop_duplicates() to avoid redundancy in analysis.
<br>
5.	Standardized categorical values	Standardized 'gender' (e.g., 'f', 'F' → 'F'; 'm', 'M' → 'M') and 'no-show' column to consistent 'Yes' / 'No' format for clarity.
<br>
6.	Converted date columns	Converted 'ScheduledDay' and 'AppointmentDay' to proper UTC-aware datetime objects using pd.to_datetime(..., utc=True).
Also formatted to human-readable dd-mm-yyyy HH:MM:SS+00:00 using .apply() with strftime().
<br>
7.	Cleaned column names	Renamed all columns to lowercase, stripped spaces, and replaced spaces with underscores (e.g., 'ScheduledDay' → 'scheduledday') using: df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').
<br>
8.	Fixed data types	Ensured age is an integer using pd.to_numeric(df['age'], errors='coerce').
<br>
9.	Dropped invalid rows	Removed rows with missing or corrupted critical fields like 'age', 'appointmentday', or 'gender' using df.dropna(subset=[...]).
<br> 
10.	Exported cleaned data	Saved the cleaned dataset as Cleaned_Medical_Appointment_No_Shows.csv using df.to_csv(..., index=False) for downstream analysis or modeling.
<br>
#-> Additional Notes:<br>
-> Timezone-aware formatting (with +00:00) ensures compatibility for time-based analysis.
-> errors='coerce' was essential to gracefully handle bad or malformed data instead of raising errors.
-> All preprocessing steps followed good data hygiene practices for machine learning or statistical workflows.
