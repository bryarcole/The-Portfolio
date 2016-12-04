from __future__ import print_function

from collections import defaultdict
import json
import sys
import praw

import praw as reddit

subreddit_tags = "all"

COMMENT_LIMIT = 1000
SUBMISSION_LIMIT = 1000


r = reddit.Reddit(user_agent='test')
redditors = defaultdict(lambda: defaultdict(int))
thing_count = 0
sr = r.get_subreddit(subreddit_tags)
new_submission = sr.get_top_from_day(limit=SUBMISSION_LIMIT)
for thing in new_submission:
    thing_count += 1
    flat_comments = praw.helpers.flatten_tree(thing.comments)
    for comment in flat_comments:
        if isinstance(comment, praw.objects.MoreComments):
            flat_comments=comment._continue_comments
            continue
        if comment.is_root:
            DRAMA_LIMIT = 0
            reply_comments = flat_comments = praw.helpers.flatten_tree(comment.replies)
            for reply in reply_comments:
                if isinstance(reply, praw.objects.MoreComments):
                    reply_comments = reply._continue_comments
                    continue
                if reply.score <= -3:
                    DRAMA_LIMIT += 1
            if DRAMA_LIMIT >= 5:
                print(comment.permalink)
                continue