# Task 1: Data Cleaning and Preprocessing Summary

## Objective
Clean and prepare the raw `Medical_Appointment_No_Shows.csv` dataset for analysis.

## Summary of Changes and Fixes Made

| Step | Action                        | Description |
|------|-------------------------------|-------------|
| 1    | Loaded dataset                | Loaded the raw dataset using `pandas.read_csv()` for efficient handling. |
| 2    | Inspected structure           | Checked initial shape, column names, and data types using `.shape`, `.columns`, and `.info()` to understand the dataset. |
| 3    | Handled missing values        | Used `.isnull().sum()` and `errors='coerce'` in datetime conversion to safely convert or mark invalid entries as missing (`NaT`). |
| 4    | Removed duplicates            | Dropped 100% identical rows using `df.drop_duplicates()` to avoid redundancy in analysis. |
| 5    | Standardized categorical values | Standardized 'gender' (e.g., 'f', 'F' → 'F'; 'm', 'M' → 'M') and 'no-show' column to consistent 'Yes' / 'No' format for clarity. |
| 6    | Converted date columns        | Converted `ScheduledDay` and `AppointmentDay` to proper UTC-aware datetime objects using `pd.to_datetime(..., utc=True)` and formatted them to `dd-mm-yyyy HH:MM:SS+00:00` using `.apply()` with `strftime()`. |
| 7    | Cleaned column names          | Renamed all columns to lowercase, stripped spaces, and replaced spaces with underscores (e.g., `ScheduledDay` → `scheduledday`) using: `df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')`. |
| 8    | Fixed data types              | Ensured age is an integer using `pd.to_numeric(df['age'], errors='coerce')`. |
| 9    | Dropped invalid rows          | Removed rows with missing or corrupted critical fields like `age`, `appointmentday`, or `gender` using `df.dropna(subset=[...])`. |
| 10   | Exported cleaned data         | Saved the cleaned dataset as `Cleaned_Medical_Appointment_No_Shows.csv` using `df.to_csv(..., index=False)` for downstream analysis or modeling. |

## Additional Notes

- Timezone-aware formatting (`+00:00`) ensures compatibility for time-based analysis.
- `errors='coerce'` was essential to gracefully handle bad or malformed data instead of raising errors.
- All preprocessing steps followed good data hygiene practices for machine learning or statistical workflows.
