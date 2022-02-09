import json
from collections import Counter

import requests

from class_instapost import InstaPost


#  to extract the post id from the whole url
def get_post_id(post_url):  # to get the post id from the url

    try:
        if not post_url.startswith("https://www.instagram.com"):
            print("invalid URL")
            return None

        a = post_url.strip("https://www.instagram.com/p/")
        b = a.split("/")[0]
        return b

    except AttributeError:
        return None


def fetch_insta_post(post_id):
    post_url1 = "https://www.instagram.com/p/{0}?__a=1".format(post_id)
    return post_url1


def get_json_from_url(post_url):
    post_id = get_post_id(post_url)
    url = fetch_insta_post(post_id)
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("connection error")
        return
    if r.status_code != 200:
        print("invalid response")
        return
    j = r.json()
    return j


json_mwh = get_json_from_url("https://www.instagram.com/p/B1ggK9fB_Mi/?utm_source=ig_web_copy_link")
json_oojj = get_json_from_url("https://www.instagram.com/p/Bz-vHGlBJYG/?utm_source=ig_web_copy_link")
json_ho = get_json_from_url("https://www.instagram.com/p/By1vXKUBmzX/?utm_source=ig_web_copy_link")
if json_mwh:
    mwh = InstaPost(json_mwh)
    # print(candid.first_comment_by, "was the first one to comment on the post and the comment was: ",
    #       candid.first_comment)
    # print(candid.video_url)
    # print(candid.caption)
    # print(candid.caption_without_hashtags)
if json_oojj:
    oojj = InstaPost(json_oojj)

if json_ho:
    ho = InstaPost(json_ho)

total_hashtags = mwh.hashtags + oojj.hashtags + ho.hashtags
print("total hashtags from the posts has length", len(total_hashtags))
print(total_hashtags)
print("Number of times #dancer has been used:")
print(total_hashtags.count("#dancer"))
result = sorted(total_hashtags, key=total_hashtags.count, reverse=True)
print(result)
print(dict.fromkeys(result))
mylist = list(dict.fromkeys(result))
print("total hashtag after removing the duplicacy has length", len(mylist))
print(mylist)



