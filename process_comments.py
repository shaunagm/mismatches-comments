import json


new_dict = {"data": []}

with open('comments.txt') as json_file:
    data = json.load(json_file)
    for page in data:
        for comment in page:
            new_dict["data"].append({
                "body": comment['body'],
                "url": comment['html_url'].replace("commitcomment-", "r"),
                "interview": comment['path']
            })

with open('processed_comments.txt', 'w') as outfile:
    json.dump(new_dict, outfile)

# TODO: process body to generate a list of hashtags?

