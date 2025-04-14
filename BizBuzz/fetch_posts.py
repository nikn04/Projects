import requests
import json
import time
import re

def fetch_4chan_posts(board="biz", max_posts=1000):
    base_url = f"https://a.4cdn.org/{board}"
    headers = {"User-Agent": "4chanSentimentBot/1.0"}
    posts = []
    post_id = 1

    # Geting thread IDs from catalog
    catalog_url = f"{base_url}/catalog.json"
    try:
        time.sleep(1)
        response = requests.get(catalog_url, headers=headers, timeout=5)
        response.raise_for_status()
        threads = response.json()
        thread_ids = []
        for page in threads:
            for thread in page.get("threads", []):
                if "no" in thread:
                    thread_ids.append(thread["no"])
                if len(thread_ids) >= 50:
                    break
            if len(thread_ids) >= 50:
                break
    except requests.RequestException as e:
        print(f"Error fetching catalog: {e}")
        return []

    # Fetching posts from each thread
    for thread_id in thread_ids:
        thread_url = f"{base_url}/thread/{thread_id}.json"
        try:
            time.sleep(1)
            response = requests.get(thread_url, headers=headers, timeout=5)
            response.raise_for_status()
            thread_data = response.json()
            for post in thread_data.get("posts", []):
                if "com" in post and post["com"].strip():
                    text = re.sub(r"<[^>]+>", " ", post["com"])
                    text = text.replace(">", ">").replace("\n", " ").strip()
                    if len(text) > 10:
                        posts.append({"id": post_id, "text": text[:280]})
                        post_id += 1
                if len(posts) >= max_posts:
                    break
            if len(posts) >= max_posts:
                break
        except requests.RequestException as e:
            print(f"Error fetching thread {thread_id}: {e}")
            continue

    if not posts:
        print("No valid posts found.")
    else:
        print(f"Fetched {len(posts)} posts.")
    return posts