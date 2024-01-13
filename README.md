# template-bot
A template Telegram bot using aiogram. Can be deployed with a PostgreSQL database and a Redis cache using Docker Compose.

## Deploy locally
1. Write your Bot API token to `secrets/telegram_api_token`.
2. Run `docker compose up --build`.

## Known issues
- First `docker compose up` execution will need to generate `cache/` and `data/` directories, which may cause Redis and PostgreSQL services to be temporarily unavailable and crash the bot.
