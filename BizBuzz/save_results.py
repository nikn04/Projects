def save_sentiments(sentiments, sentiment_counts, filename="sentiments_full.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for s in sentiments:
            f.write(f"Post ID={s['id']}: {s['text'][:50]}...\n")
            f.write(f"Sentiment={s['sentiment']}, Score={s['score']:.2f}\n\n")
        f.write(f"Summary: {sentiment_counts['POSITIVE']} POSITIVE, {sentiment_counts['NEGATIVE']} NEGATIVE\n")
    print(f"Sentiments saved to {filename}")