# Email Log Analysis Script

This Python script processes pseudo email log files, combining events based on session IDs, calculating the duration of each session, and outputting a JSON-formatted array with detailed session information.

## Requirements

- Python 3.6 or later.
- A pseudo email log file in a specified tab-separated format.

## Installation

No additional installation beyond a standard Python environment is required. Ensure Python 3.6 or later is installed on your system.

## Usage

1. Ensure your log file is in the same directory as the script or update the `log_file_path` variable with the correct path to your log file. The expected file name is `email.log`.
2. Run the script with Python from the terminal or command prompt:

```bash
python log_automation.py
```

The script will process the log file and output the combined session data in JSON format to the console.

## Functions Documentation

### parse_log_file

Parses the provided log file, combining events based on session IDs.

```python
def parse_log_file(log_file_path: str) -> Dict[str, Any]:
```

**Parameters:**

- `log_file_path` (str): Path to the log file to be processed.

**Returns:**

- A dictionary keyed by session ID, with each value being a dictionary containing the session's start and end times, and other fields.

### calculate_durations_and_format

Calculates the duration of each session and formats the data for output.

```python
def calculate_durations_and_format(sessions: Dict[str, Any]) -> List[Dict[str, Any]]:
```

**Parameters:**

- `sessions` (Dict[str, Any]): A dictionary of session data, as returned by `parse_log_file`.

**Returns:**

- A list of dictionaries, each representing a session's combined events in a structured format, suitable for JSON output. Only sessions with all required fields are included.

