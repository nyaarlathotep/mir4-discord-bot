# mir4-discord-bot
A Discord bot that interacts with the Mir4 API.

```
https://api.mir4.gq/v1/
```

# Before Running...

Make sure to create a **.env** file and place your Discord token inside there, like so:

```
DISCORD_TOKEN=your_discord_token_goes_here
```

Then place this **.env** file in the root of the app subdirectory *(i.e. app/.env)*:

```
.
├── ...
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── app/
      ├── .env <---- [PLACE FILE HERE]
      ├── main.py
      ├── cogs/
      |     └── ...
      ├── lib/
      |     └── ...
     ...
```

# **Running Bot Natively**

Bot requires Python 3.8 installed on your system.

Install project dependecies through PIP:

```
pip install -r requirements.txt
```

Run bot with command:

```
python app/main.py
```



# **Running Bot Through Docker [Compose]

Run the bot by simply entering the following command in the root directory:

```
docker-compose up
```
