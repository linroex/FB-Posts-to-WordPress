from facebook import Facebook
from custom_object import Facebook_Post
from config import config

import json

def main():
    fb = Facebook(config['access_token'])
    # print(posts['paging']['next'])

    for i in range(1,20):
        
        if i == 1:
            posts = fb.api('get', '/859728857453185/posts')
        else:
            if 'paging' not in posts.keys():
                break
            else:
                posts = fb.next(posts['paging']['next'])

        for item in posts['data']:
            # print(item)
            pass
        
        print(i)

if __name__ == '__main__':
    main()