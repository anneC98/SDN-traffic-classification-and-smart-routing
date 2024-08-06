import pandas as pd

def calculate_duration_average(file_path):
  """Calculates the average of the 'Duration' column in a CSV file.

  Args:
    file_path: The path to the CSV file.

  Returns:
    The average of the 'Duration' column.
  """

  try:
    df = pd.read_csv(file_path)
    df['Label'] = 'Low'

# Optionally, save the updated dataset to a new file
    df.to_csv('updated_dataset.csv', index=False)
    print(df['Duration'].sum())
    duration_average = df['Duration'].mean()
    return duration_average
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    return None
  except KeyError:
    print("Error: Column 'Duration' not found in the CSV file.")
    return None
  except ValueError:
    print("Error: Values in the 'Duration' column are not numeric.")
    return None



# Example usage:
file_path = "customClass1Traffic.csv"  # Replace with your file path
average_duration = calculate_duration_average(file_path)
if average_duration is not None:
  print("Average Duration:", average_duration)
  

  
