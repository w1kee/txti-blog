import re
import requests

def get_recommended_url(text):
    url = []
    for char in text:
        if re.match(char, '[A-Za-z0-9\-]'):
            url.append(char)
        elif re.match(char, '[\s_]'):
            url.append('-')
    return ''.join(url)

def main():
    blog_name = input('*Enter your blog name, cant be blank: ')
    if blog_name == '':
        raise Exception('Blog name is blank')
    while True:
        url = input('*Enter your blog url (must follow /a-z0-9\-/): ')
        for char in url:
            if re.match(char, r'[a-z0-9\-]':
                raise Exception('url doesnt follow rules')
        if not int(requests.get('http://txti.es/'+url).status_code) == 404:
            print('already taken, choose a different one')
            continue
        break
    author = input('Author, twitter handle recommended: ')
    while True:
        description = input('Description /.{0,200}/: ')
        if len(description) > 200:
            print('your description is too long')
            continue
        break




if __name__ == '__main__':
    main()
