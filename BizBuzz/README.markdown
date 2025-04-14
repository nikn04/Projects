# BizBuzz: Decoding Sentiment on 4chan’s Crypto Frontier

## Overview

BizBuzz is a Python project that performs **sentiment analysis** on posts from 4chan’s `/biz/` board, a hub for discussions on business, finance, and cryptocurrency. Using the `distilbert-base-uncased-finetuned-sst-2-english` model, it classifies posts as `POSITIVE` or `NEGATIVE`, capturing the emotional pulse of `/biz/`’s chaotic community. The project fetches 1000+ posts via 4chan’s API, analyzes their sentiment, and saves results to `sentiments_full.txt` for further study.

### Features
- Fetches real-time posts from `/biz/` threads.
- Analyzes sentiment with a pre-trained `distilbert` model.
- Saves detailed results (post ID, text snippet, sentiment, score) and a summary (e.g., 200 `POSITIVE`, 800 `NEGATIVE`).
- Modular design with separate files for fetching, analyzing, and saving.

## Project Structure

- **`fetch_posts.py`**: Fetches posts from 4chan’s `/biz/` board using the API.
- **`analyze_sentiment.py`**: Analyzes sentiment of fetched posts using `distilbert`.
- **`save_results.py`**: Saves sentiment results to `sentiments_full.txt`.
- **`main.py`**: Orchestrates the pipeline, calling the above modules.
- **`sentiments_full.txt`**: Output file with sentiment analysis for all posts.

## Requirements

- Python 3.8+
- Conda (recommended for environment management)
- Libraries: `requests`, `transformers`

## Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd bizbuzz
   ```

2. **Create a Conda environment**:
   ```bash
   conda create -n bizbuzz python=3.8
   conda activate bizbuzz
   ```

3. **Install dependencies**:
   ```bash
   pip install requests transformers
   ```

## Usage

1. **Run the project**:
   ```bash
   conda activate bizbuzz
   set TF_ENABLE_ONEDNN_OPTS=0  # Optional: silences oneDNN warnings
   python main.py
   ```

2. **Expected output** (console):
   ```
   Fetching 4chan posts...
   Fetched 1000 posts.
   Analyzing sentiment...
   Post ID=1: This board is for the discussion of topics related... Sentiment=POSITIVE, Score=0.97
   Post ID=2: Check the  catalog  before posting a new thread!... Sentiment=NEGATIVE, Score=1.00
   ...
   Sentiment summary: 200 POSITIVE, 800 NEGATIVE
   Sentiments saved to sentiments_full.txt
   ```

3. **Check results**:
   - Open `sentiments_full.txt` to view sentiment analysis for all posts:
     ```
     Post ID=1: This board is for the discussion of topics related...
     Sentiment=POSITIVE, Score=0.97
     ...
     Summary: 200 POSITIVE, 800 NEGATIVE
     ```

## Notes

- **Runtime**: ~6-7 minutes on a standard CPU (e.g., 4-core i5/i7, 8GB RAM).
- **4chan API**: Respects rate limits (1 request/sec). Retries on failures.
- **Content Warning**: `/biz/` posts can be explicit or sensitive (e.g., financial rants, memes). Review `sentiments_full.txt` before sharing.
- **Customization**:
  - Change board: Edit `main.py` to use `fetch_4chan_posts(board="g")` for tech discussions.
  - Reduce posts: Set `max_posts=500` in `main.py` for faster runs (~3-4 min).
  - CSV output: Modify `save_results.py` to save as CSV (see comments).

## Troubleshooting

- **API errors (e.g., 403)**:
  - Increase `time.sleep(2)` in `fetch_posts.py`.
  - Check connectivity: `ping a.4cdn.org`.
- **Memory issues**:
  - Lower `max_posts=500` in `main.py`.
  - Close other applications to free RAM.
- **Warnings**:
  - `oneDNN` or `tf.losses`: Use `set TF_ENABLE_ONEDNN_OPTS=0` before running.

## Future Enhancements

- Support for multiple boards (e.g., `/g/`, `/pol/`).
- CSV output for easier data analysis.
- Keyword extraction to identify trending topics (e.g., “crypto,” “scam”).

## License

MIT License. See `LICENSE` file for details.

## Acknowledgments

- Built with [Hugging Face Transformers](https://huggingface.co/) for sentiment analysis.
- Inspired by the vibrant `/biz/` community’s unique voice.