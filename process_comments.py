# load json file
import json

new_dict = {"data": []}

with open('comments.txt') as json_file:
    data = json.load(json_file)
    for comment in data:
        new_dict["data"].append({
            "body": comment['body'],
            "url": comment['url'].replace("commitcomment-", "r"),
            "interview": comment['path']
        })

with open('processed_comments.txt', 'w') as outfile:
    json.dump(new_dict, outfile)

# TODO: process body to generate a list of hashtags?

