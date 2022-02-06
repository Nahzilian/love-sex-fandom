from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json
import os

import requests


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
DOCUMENT_ID = '1wT5zAcybPtTpcqShCo03NYDPP3G7ED34hK7dHI1CYGU'

SEC_1 = [0, 204]
SEC_2 = [204, 408]
SEC_3 = [408, 612]

p_breaker = '<br><br>'


def get_creds () -> Credentials:
    """
    Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def create_json_file(path, content):
    """
    Write content to json file for analyzing
    """
    with open(path, 'w') as f:
        f.write(content)
    print("File written to {path}".format(path = path))

def slug_converter(title: str):
    """convert title to string"""
    t = title.replace('?','')
    t = t.replace(':','')
    t = t.replace("'",'')
    t = t.replace(",",'')
    t = t.replace("’",'')
    t = t.replace("‘",'')
    t = t.replace("é",'e')
    

    return t.lower().strip().replace(' ','-') + '.html'


def get_docs_content(creds, document_id):
    """
    Retrieve raw content from google doc with given credential and document ID
    """
    try:
        service = build('docs', 'v1', credentials=creds)

        document = service.documents().get(documentId=document_id).execute()
        cur_dir = os.getcwd() + '/assets/test.json'
        content = json.dumps(document, indent = 4) 
        create_json_file(cur_dir, content)
        data = {}
        # create_file()
        data["body"] = document.get('body')
        # data["img"]["main_img"] = document.get('inlineObjects')
        # data["img"]["inline"] = document.get('positionedObjects')


        return data
    except HttpError as err:
        print(err)

def retrieve_text(d):
    content = d.get('content')

    data = {}
    template_text = ''

    counter = 0
    for paragraph in content:
        p_text = ''
        if paragraph.get('paragraph'):
            
            elements = paragraph.get('paragraph').get('elements')
            c = ''
            for element in elements:
                text_run =  element.get('textRun')
                if text_run:
                    p_content = text_run.get('content')
                    if p_content != '\n':
                        c += element.get('textRun').get('content')
            
            p_text += c
            
            if counter == 0:
                data['title'] = p_text
            elif counter == 1:
                data['dek'] = p_text
            elif counter == 2:
                data['by_words'] = p_text
            elif counter == 3:
                data['by_visuals'] = p_text
            else:
                template_text += p_text
                if not c == '':
                    template_text += p_breaker
                template_text += '\n'
            counter +=1

    data['content'] = content_clean_up(template_text)
    print(data)
    return data

def retrieve_imgs(imgs, slug):
    formatted_img = {}
    # Retrieve inline img
    inline_img = imgs['main_img']
    for key, val in inline_img:
        url = val['inlineObjectProperties']['embeddedObject']['imageProperties']['contentUri']
        name = 'cover-' + slug
        download_img(url, name)
        formatted_img[key] = {"name": name, "float": None, "is_main": True, "slug": slug}

    # Retrive position img
    positioned_img = imgs['positionedObjects']
    for key, val in positioned_img:
        url = val['positionedObjectProperties']['embeddedObject']['imageProperties']['contentUri']
        name = 'pos-' + slug
        download_img(url, name)

        pos = val['positionedObjectProperties']['positioning']['leftOffset']['magnitude']
        width = val['positionedObjectProperties']['embeddedObject']['size']['width']['magnitude']
        
        mean = (pos * 2 + width) / 2

        float_pos = ""
        if mean in range(SEC_1[0], SEC_1[1]):
            float_pos = "left"
        elif mean in range(SEC_2[0], SEC_2[1]):
            float_pos = "center"
        else:
            float_pos = "right"

        formatted_img[key] = {"name": name, "float": float_pos, "is_main": False, "slug": slug}

    return formatted_img

def google_doc_data_filter(content: dict, type: str, slug=""):
    if type == "text":
        return retrieve_text(content)
    else: 
        return retrieve_imgs(content, slug)
    


def download_img(img_url, name):
    """Download missing images"""
    response = requests.get(img_url)
    file = open(name, 'wb')
    file.write(response.content)
    file.close()


def content_clean_up(content):
    """Special function to clean up text"""

    cleaned = content.replace('<i>', '<em>')
    cleaned = cleaned.replace('</i>', '</em>')

    return cleaned

def img_builder(link, pos):
    return '<img src="{link}" width="300" class="float-{pos}">'.format(link = link, pos = pos)

def get_content_from_google_doc(doc_id):
    creds = get_creds()
    data = get_docs_content(creds, doc_id)

    print(data)
    return retrieve_text(data["body"])


# get_content_from_google_doc()

# NEED TO ORGANIZE THE DAMM THINGY
# DEACTIVATED the img scrapper