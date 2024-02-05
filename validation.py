import requests
import json
import pathlib
import argparse
import sys

def extractPath():
    path = []
    for p in pathlib.Path("./").rglob('*.tsv'):
        temp_path = "{}/{}".format(p.parent, p.stem)
        if(p.stem == "i18nlanguages"): 
            continue
        path.append(temp_path[len(""):])
    return path

def validate(lang, path, tag, service_url):
    is_valid = True
    for ns in path:
        url = "{}/{}.tsv?tag={}&lang={}".format(service_url, ns, tag, lang)
        #print(url)
        response = requests.get(url)
        #print(response)
        if(response.status_code != 200):
            print("error with ns {} lang {}".format(ns, lang))
            is_valid = False
            continue
    return is_valid

parser = argparse.ArgumentParser(description='Validate TSV')
parser.add_argument("-b", "--branch", required=True)
parser.add_argument("-u", "--url", required=True)
args = parser.parse_args()
tag = args.branch
service_url = args.url
lang = "en"
path = extractPath()
is_valid = validate(lang, path, tag, service_url)

if is_valid :
    sys.exit(0)
else :
    sys.exit(1)

print(is_valid)