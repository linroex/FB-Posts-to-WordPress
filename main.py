from facebook import Facebook
from config import config

def main():
    fb = Facebook(config['access_token'])
    print(fb.api('get', '/859728857453185/posts'))

if __name__ == '__main__':
    main()