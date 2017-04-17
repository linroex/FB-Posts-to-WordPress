from urllib.request import urlretrieve
import json

from facebook import Facebook
from config import config

def get_all_posts():
    fb = Facebook(config['access_token'])
    posts = []

    for i in range(1,20):
        
        if i == 1:
            response = fb.api('get', '/859728857453185/posts', {'fields': 'message,full_picture,created_time', 'limit': '100'})
        else:
            if 'paging' not in response.keys():
                break
            else:
                response = fb.next(response['paging']['next'])

        for item in response['data']:
            if 'message' in item.keys():
                id = str(len(posts))

                if 'full_picture' in item.keys():
                    urlretrieve(item['full_picture'], 'images/' + id + '.jpg')
                    
                    posts.append({
                        'id': id,
                        'message': item['message'],
                        'created_time': item['created_time'],
                        'full_picture': 'images/' + id + '.jpg'
                    })
                else:
                    posts.append({
                        'id': len(posts) - 1,
                        'message': item['message'],
                        'created_time': item['created_time'],
                    })
                print(len(posts))

    return posts

def main():
    posts = get_all_posts()

    with open('posts.json', 'w', encoding='utf8') as f:
        f.write(json.dumps(posts))

if __name__ == '__main__':
    main()