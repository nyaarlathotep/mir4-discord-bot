import requests
import urllib.parse
from rich import print
import nextcord
from nextcord.ext import commands
from lib.base_cog import BaseCog

class Mir4(BaseCog):
    """
    This cog interacts with the mir4 tracker API (https://api.mir4.gq/).
    """
    def __init__(self, bot):
        super().__init__(bot)
        self.api_base_url = "https://api.mir4.gq/v1"

    #==========================================================
    #=====================Helper Methods=======================
    #==========================================================

    async def search(self, ctx, query):
        """
        Queries API for character data and returns first result.
        """
        url_encoded_query = urllib.parse.quote(query) # make sure raw string is safe for API query
        response = requests.get(f'{self.api_base_url}/search/{url_encoded_query}') # make a GET query to API
        if response.status_code != 200:
            await ctx.send(f"Could not retrieve data from API. (Server Status Code: {response.status_code})")
            return
        data = response.json()
        if "characters" not in data.keys():
            await ctx.send("Could not retrieve character data.")
            return
        if len(data["characters"]) <= 0:
            await ctx.send("Character data contains no characters.")
            return
        first_result = data["characters"][0]
        await ctx.send(embed=self.get_search_embed(first_result))

    def get_search_embed(self, character_data):
        """
        Returns an embed instance with formatted query data.
        """
        embed_color = 0x20406b
        embed = nextcord.Embed(
                title=character_data["name"],
                description=
                f'{character_data["data"]["class"]["name"]} {character_data["data"]["power"]} PS\n' + \
                f'Clan: {character_data["data"]["clan"]["name"]}\n' + \
                f'Clan Rank: {character_data["data"]["clan"]["rank"]}\n' + \
                f'Server: {character_data["data"]["server"]["name"]}\n' + \
                f'Server Rank: {character_data["data"]["server"]["rank"]}\n' + \
                f'Region: {character_data["data"]["region"]["name"]}\n' + \
                f'Region Rank: {character_data["data"]["region"]["rank"]}\n' + \
                f'Global Rank: {character_data["data"]["global_rank"]}\n',
                color = embed_color
              )
        return embed

    #==========================================================
    #=========================EVENTS===========================
    #==========================================================

    #==========================================================
    #========================TASKS=============================
    #==========================================================

    #==========================================================
    #=======================COMMANDS===========================
    #==========================================================

    @commands.command(name='rank')
    async def get_rank(self,ctx, query):
        embed = nextcord.Embed(
            title='Searching for character... 🔎',
            color = 0xffb247)
        await ctx.send(embed=embed)
        await self.search(ctx, query)

# === Module Method(s) ===
def setup(bot):
    """
    A module method to add this module's cog to a discord bot.
    To be used by a factory module.
    """
    bot.add_cog(Mir4(bot))