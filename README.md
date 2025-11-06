# X-OnePiece-Bot

A Twitter bot that monitors and retrieves tweets from the WorstGenHQ account, designed to track One Piece related content and discussions.

## Features

- Fetches recent tweets from specified Twitter accounts
- Retrieves up to 20 most recent tweets
- Rate limit handling with detailed error reporting
- Shows reset time when rate limits are exceeded

## Prerequisites

- Python 3.7+
- Twitter API Developer Account with API credentials
- tweepy library
- python-dotenv library

## Installation

1. Clone the repository:
```bash
git clone git@github.com:nrcisst/X-OnePiece-Bot.git
cd X-OnePiece-Bot
```

2. Install required dependencies:
```bash
pip install tweepy python-dotenv
```

3. Create a `.env` file in the root directory with your Twitter API credentials:
```env
API_KEY=your_api_key_here
SECRET_API=your_api_secret_here
BEARER_TOKEN=your_bearer_token_here
ACCESS_TOKEN=your_access_token_here
SECRET_ACCESS=your_access_token_secret_here
```

## Configuration

To get your Twitter API credentials:

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new project and app
3. Generate your API keys and tokens
4. Copy them to your `.env` file

## Usage

Run the bot:
```bash
python OPBot.py
```

The bot will:
1. Connect to the Twitter API using your credentials
2. Fetch the latest 20 tweets from WorstGenHQ
3. Display each tweet in the console

## Project Structure

```
X-OnePiece-Bot/
├── OPBot.py          # Main bot script
├── .env              # Environment variables (not tracked in git)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Rate Limits

The bot handles Twitter API rate limits gracefully. When a rate limit is exceeded, it will display:
- Total request limit
- Remaining requests
- Reset time in local timezone

## Future Enhancements

- [ ] Implement tweet filtering based on keywords
- [ ] Add support for multiple accounts
- [ ] Store tweets in a database
- [ ] Add automated posting functionality
- [ ] Implement scheduling for regular checks

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Disclaimer

This bot is for educational purposes. Make sure to comply with Twitter's API Terms of Service and rate limits when using this bot.
