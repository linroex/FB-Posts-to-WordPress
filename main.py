from facebook import Facebook
from custom_object import Facebook_Post as Post
from config import config

def main():
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
                if 'full_picture' in item.keys():
                    posts.append(Post(item['message'], item['created_time'], item['full_picture']))
                else:
                    posts.append(Post(item['message'], item['created_time']))
                print(len(posts))
    
    print(posts)
        

if __name__ == '__main__':
    main()