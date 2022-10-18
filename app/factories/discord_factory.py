from lib.discord_bot import DiscordBot
from cogs import mir4

def create_instance():
    """
    Returns a configured instance of a Discord bot.
    """
    # create a bot instance
    bot = DiscordBot()
    # load cogs into bot instance
    cogs_to_add_to_bot = [mir4]
    for i in range(len(cogs_to_add_to_bot)):
        cogs_to_add_to_bot[i].setup(bot)
    # return bot instance
    return bot