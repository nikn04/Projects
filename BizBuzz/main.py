from fetch_posts import fetch_4chan_posts
from analyze_sentiment import analyze_sentiment
from save_results import save_sentiments
import time

def main():
    # Fetch posts with retry
    print("Fetching 4chan posts...")
    max_retries = 3
    for attempt in range(max_retries):
        posts = fetch_4chan_posts(max_posts=1000)
        if posts:
            break
        print(f"Retry {attempt + 1}/{max_retries}...")
        time.sleep(5)
    if not posts:
        print("Failed to fetch posts after retries, exiting.")
        return

    # Analyze sentiment
    sentiments, sentiment_counts = analyze_sentiment(posts)

    # Save results
    save_sentiments(sentiments, sentiment_counts)

if __name__ == "__main__":
    main()