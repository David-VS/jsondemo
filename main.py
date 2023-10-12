import json
import requests
import posts as p
import dataclasses


try:
    http_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if http_response.status_code == 200:
        # deserialization
        posts = json.loads(http_response.text)
        print(type(posts))

        for post in posts:
            if post['userId'] == 2:
                print(post)

except:
    print("problem executing the request")


new_post = p.PostElement(2, 1021, 'original title', 'go with the flow')
json_string = json.dumps(dataclasses.asdict(new_post))
print(json_string)