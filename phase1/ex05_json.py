import json

def load_data(location: str):
  try:
    with open(location, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    print(f"File '{location}' not locationound.")
    return []
  except json.JSONDecodeError as e:
    print(f"File '{location}' undecodable. Invalid JSON: {e}")
    return []
  
data = load_data('data.json')

print(data)
