import os
import json
from google_docs import *

# current_dir = os.getcwd().replace('misc-python')
host_url = 'https://lovesexfandom.theeyeopener.com'
# host_url = '.'
main_title = 'Love Sex and Fandom'

# data_json = open('./room_data.json')
# article_data = json.load(data_json)

def create_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
    print("File written to {path}".format(path = path))


def format_template( dek, title, by_words, by_visuals, content, img_name = "bg_placeholder.jpeg", slug = 'test'):
    template_file = open('../article.html')
    template = template_file.read()
    
    template = template.replace('<!--TITLE-->', title)
    template = template.replace('<!--MAIN_TITLE-->', main_title)

    template = template.replace('<!--DEK-->', dek)

    # meta img
    # https://humannature.theeyeopener.com/images/NoahsArc_VedangiPatel_Oct27.jpg
    meta_img = "{host_url}/assets/{img_name}".format(host_url = host_url, img_name = img_name)

    template = template.replace('<!--MAIN_IMG-->', meta_img)


    url = "{host_url}/{slug}.html".format(host_url = host_url, slug = slug)
    template = template.replace('<!--ATC_URL-->', url)

    # Words
    template = template.replace('<!--WORDS-->', by_words, 1)

    # Visual
    template = template.replace('<!--VISUALS-->', by_visuals, 1)
    #Content

    template = template.replace('<!--CONTENT-->', content, 1)

    return template


def main(doc_id):
    data = get_content_from_google_doc(doc_id)
    template = format_template(data['dek'], data['title'], data['by_words'], data['by_visuals'], data['content'], slug_converter(data['title']))
    file_name = slug_converter(data['title'])
    cur_dir = os.getcwd().replace('misc-python', file_name)

    create_file(cur_dir, template)