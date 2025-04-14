from transformers import pipeline

def analyze_sentiment(posts):
    # Initialize sentiment analyzer
    sentiment_analyzer = pipeline("sentiment-analysis")
    sentiment_counts = {"POSITIVE": 0, "NEGATIVE": 0}
    sentiments = []

    print("Analyzing sentiment...")
    for post in posts:
        sentiment = sentiment_analyzer(post["text"])[0]
        sentiment_counts[sentiment["label"]] += 1
        sentiments.append({
            "id": post["id"],
            "text": post["text"],
            "sentiment": sentiment["label"],
            "score": sentiment["score"]
        })
        if post["id"] <= 5:
            print(f"Post ID={post['id']}: {post['text'][:50]}... Sentiment={sentiment['label']}, Score={sentiment['score']:.2f}")

    print(f"Sentiment summary: {sentiment_counts['POSITIVE']} POSITIVE, {sentiment_counts['NEGATIVE']} NEGATIVE")
    return sentiments, sentiment_counts