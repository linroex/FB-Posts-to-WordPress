from facebook import Facebook
from custom_object import Facebook_Post
from config import config

def main():
    fb = Facebook(config['access_token'])
    print(fb.api('get', '/859728857453185/posts'))

if __name__ == '__main__':
    main()