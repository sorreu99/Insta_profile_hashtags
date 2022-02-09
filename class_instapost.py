import re

import requests


class InstaPost:
    def __init__(self, jason):
        self.jason = jason
        self.number_of_views = self.get_number_of_views()
        self.number_of_likes = self.get_number_of_likes()
        self.number_of_comments = self.get_number_of_comment()
        self.first_comment = self.get_first_comment()
        # self.comment_max_likes = self.get_comment_max_likes()
        self.get_display_url = self.get_display_url()
        self.first_comment_by = self.get_first_comment_by()
        self.video_url = self.get_video_url()
        self.caption = self.get_caption()
        self.caption_without_hashtags = self.get_caption_without_hashtag()
        self.hashtags = self.get_hashtags()

    #  to get the total number of views in the post
    def get_number_of_views(self):

        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["is_video"]
        if value2:
            value3 = value1["video_view_count"]
            return value3
        else:
            return "picture doesn't show number of views"

    #  to get the display url of the post
    def get_display_url(self):

        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["display_url"]
        return value2

    #  to get the total number of likes in the post
    def get_number_of_likes(self):

        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_preview_like"]
        value3 = value2["count"]
        return value3

    #  To get the count of total comments in the post
    def get_number_of_comment(self):

        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_to_parent_comment"]
        value3 = value2["count"]
        return value3

    def get_first_comment(self):

        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_to_parent_comment"]
        value3 = value2["edges"][0]
        value4 = value3["node"]
        value5 = value4["text"]
        return value5

    #  username of the person who commented first on the post
    def get_first_comment_by(self):

        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_to_parent_comment"]
        value3 = value2["edges"][0]
        value4 = value3["node"]
        value5 = value4["owner"]
        value6 = value5["username"]
        return value6

    #  to get the url of the video
    def get_video_url(self):
        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["is_video"]
        if value2:
            value3 = value1["video_url"]
            return value3
        else:
            return "Not a video"

    #  to get the captions
    def get_caption(self):
        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_to_caption"]
        value3 = value2["edges"][0]
        value4 = value3["node"]
        value5 = value4["text"]
        return value5

    # to get the caption without hashtags

    def get_caption_without_hashtag(self):
        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_to_caption"]
        value3 = value2["edges"][0]
        value4 = value3["node"]
        text = value4["text"]
        x = re.findall("#\w+\s", text)
        for i in x:
            text = re.sub(i, "", text)
        x = re.findall("#\w+", text)
        text = re.sub(x[0], "", text)
        return text

    def get_hashtags(self):
        value = self.jason['graphql']
        value1 = value["shortcode_media"]
        value2 = value1["edge_media_to_caption"]
        value3 = value2["edges"][0]
        value4 = value3["node"]
        text = value4["text"]
        hashtags = re.findall("#\w+", text)
        return hashtags
