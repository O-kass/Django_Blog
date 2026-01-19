import random

import csv
from datetime import datetime
from blog.models import Post
from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_path = "blog/static/blog/Shares.csv"

        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            user = User.objects.get(username="Omar")

            for row in reader:
                text = row.get("ShareCommentary", "").strip()
                hashtags = text.split("#")[1:]

                if not text or len(text) < 100:
                    continue

                created_at = datetime.strptime(
                    row["Date"], "%Y-%m-%d %H:%M:%S"
                )

                Post.objects.get_or_create(
                    content=text, title = random.choice(hashtags) if hashtags else "LinkedIn-post", date_posted=created_at,  author=user
                )