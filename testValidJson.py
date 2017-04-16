import json
with open('volkswagen-reviews.json', 'r') as content_file:
    content = content_file.read()
    records = json.loads(content)
