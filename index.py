from discord.ext import commands
import aiohttp
import discord
import asyncio
import filetype
from io import BytesIO
from discord import app_commands
from utils import http, config
from discord.ext.commands import CommandNotFound, when_mentioned_or, Group

config = config.Config.from_env(".env")
print("Logging in...")
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=0xbfdbff, description='**Help command!**\n ')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

client = commands.AutoShardedBot(case_insensitive=True, help_command=MyHelpCommand(), shard_count=config.shard_count,intents=intents,command_prefix=when_mentioned_or(config.revolt_prefix))

async def randomimageapi(
    ctx: discord.Message,
    url: str, *endpoint: str
) -> discord.Message:
    try:
        r = await http.get(url, res_method="json")
        async with aiohttp.ClientSession() as session:
            async with session.get(r.response) as resp:
                buffer = BytesIO(await resp.read())
                # buffer = await resp.read()
                await session.close()
    except aiohttp.ClientConnectorError:
        return await ctx.channel.send("The API seems to be down...")
    except aiohttp.ContentTypeError:
        return await ctx.channel.send("The API returned an error...")

    fileinfo = filetype.guess(buffer)
    fileExt = fileinfo.extension
    await ctx.channel.send(file=discord.File(buffer, filename=f"NSFW.{fileExt}", spoiler=True))
    # await ctx.channel.send(buffer)
    return resp.close()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.CustomActivity(name=f"@{client.user} help"))

@client.command()
async def ping( ctx: discord.Message):
        """ I wonder what this will do... """
        await ctx.channel.send("pong")

@client.group(invoke_without_command=True)
@commands.is_nsfw()
async def nsfw(ctx):
        """ Main command to invoke for NSFW Images """
        return

@nsfw.command(name="hass")
@commands.is_nsfw()
async def _hass( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hass", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="assgif")
@commands.is_nsfw()
async def _assgif( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?assgif", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?assgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="ass")
@commands.is_nsfw()
async def _ass( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?ass", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?ass", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="boobs")
@commands.is_nsfw()
async def _boobs( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?boobs", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="hboobs")
@commands.is_nsfw()
async def _hboobs( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hboobs", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="bbw")
@commands.is_nsfw()
async def _bbw( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?bbw", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?bbw", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="bdsm")
@commands.is_nsfw()
async def _bdsm( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?bdsm", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?bdsm", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="blow")
@commands.is_nsfw()
async def _blow( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?blow", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?blow", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="feet")
@commands.is_nsfw()
async def _feet( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?feet", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?feet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="hfeet")
@commands.is_nsfw()
async def _hfeet( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hfeet", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?hfeet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="furfuta")
@commands.is_nsfw()
async def _furfuta( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?furfuta", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?furfuta", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="furgif")
@commands.is_nsfw()
async def _furgif( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?furgif", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?furgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="futa")
@commands.is_nsfw()
async def _futa( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?futa", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?futa", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="hthighs")
@commands.is_nsfw()
async def _hthighs( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?athighs", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?athighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="thighs")
@commands.is_nsfw()
async def _thighs( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?thighs", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?thighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="gifs")
@commands.is_nsfw()
async def _gifs( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?gifs", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?gifs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="sex")
@commands.is_nsfw()
async def _sex( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?sex", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?sex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="femboy")
@commands.is_nsfw()
async def _femboy( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?irlfemb", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?irlfemb", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="hfemboy")
@commands.is_nsfw()
async def _hfemboy( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?femboy", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?femboy", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="slime")
@commands.is_nsfw()
async def _slime( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?slime", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?slime", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="pantsu")
@commands.is_nsfw()
async def _pantsu( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?pantsu", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?pantsu", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="milk")
@commands.is_nsfw()
async def _milk( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?milk", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?milk", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="latex")
@commands.is_nsfw()
async def _latex( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?latex", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?latex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="hentai")
@commands.is_nsfw()
async def _hentai( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx, f"{config.lewds_api_url}/nsfw/?hentai", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx, f"{config.lewds_api_url}/nsfw/?hentai", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

@nsfw.command(name="yuri")
@commands.is_nsfw()
async def _yuri( ctx: discord.Message):
        """ Posts an NSFW Image """
        if ctx.guild.id and ctx.channel.nsfw:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?yuri", "file")
        elif not ctx.guild.id and ctx.channel.type != discord.ChannelType.group:
            await randomimageapi(ctx,f"{config.lewds_api_url}/nsfw/?yuri", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

client.run(config.revolt_token)
