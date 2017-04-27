#!/usr/bin/env python3

import json
from findspam import FindSpam
from classes import Post


def metasmoke_json_post(post_data):
    """
    Given a JSON representation of a post from Metasmoke, return a Post
    object.
    """
    # Hack in the missing field
    #if 'score' not in post_data:
    post_data['score'] = '0'
    return Post(api_response=post_data)
    
def metasmoke_json_results(json_file):
    """
    Read a file of JSON post data (such as from a Metasmoke search)
    and yield the Post object and FindSpam().test_post(Post) result.
    """
    with open(json_file) as json_handle:
        post_data = json.load(json_handle)
    find_spam = FindSpam()
    for item in post_data:
        post = metasmoke_json_post(item)
        yield post, find_spam.test_post(post)
