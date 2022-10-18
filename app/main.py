import os
import factories.discord_factory as discord_factory

# create a discord bot instance using factory function
discord_bot = discord_factory.create_instance()

# Start bot if module is program entry point.
if __name__ == '__main__':
    """
    Get Discord token from environment variable.
    DO NOT HARD CODE TOKENS INTO SOURCE CODE!!!
    """
    discord_bot.run(os.environ["DISCORD_TOKEN"])