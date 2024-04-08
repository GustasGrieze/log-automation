import json
from datetime import datetime
from typing import Dict, List, Any

def parse_log_file(log_file_path: str) -> Dict[str, Any]:
    sessions: Dict[str, Any] = {}
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            parts = line.strip().split('\t')
            if len(parts) < 3:  # Ensuring there are enough parts to parse
                continue
            
            timestamp, session_id, info = parts
            key_value = info.split('=', 1)  # Splitting the info part into key and value
            
            if session_id not in sessions:
                sessions[session_id] = {
                    "start": timestamp,
                    "end": timestamp,
                    "fields": {}
                }
                
            sessions[session_id]["end"] = timestamp
            
            if len(key_value) == 2:
                key, value = key_value
                sessions[session_id]["fields"][key] = value

    return sessions

def calculate_durations_and_format(sessions: Dict[str, Any]) -> List[Dict[str, Any]]:
    output: List[Dict[str, Any]] = []
    for session_id, data in sessions.items():
        start = datetime.strptime(data["start"], "%Y-%m-%dT%H:%M:%S.%f")
        end = datetime.strptime(data["end"], "%Y-%m-%dT%H:%M:%S.%f")
        duration = end - start
        
        fields = data["fields"]
        # Checking for completeness: all required fields must be present
        required_fields = ["client", "message-id", "from", "to", "status"]
        if all(field in fields for field in required_fields):
            session_data: Dict[str, Any] = {
                "time": {"start": data["start"], "duration": str(duration)},
                "sessionid": session_id,
                "client": fields["client"],
                "messageid": fields["message-id"],
                "address": {
                    "from": fields["from"],
                    "to": fields["to"]
                },
                "status": fields["status"]
            }
            output.append(session_data)
    return output

log_file_path: str = 'email.log'
sessions: Dict[str, Any] = parse_log_file(log_file_path)
combined_events: List[Dict[str, Any]] = calculate_durations_and_format(sessions)
json_output: str = json.dumps(combined_events, indent=2)
print(json_output)