from revolt.ext import commands
import aiohttp
import revolt
import asyncio
import requests
import filetype
from io import BytesIO
from utils import http, config

config = config.Config.from_env(".env")
print("Logging in...")


async def randomimageapi(
    ctx: revolt.Message,
    url: str, *endpoint: str
) -> revolt.Message:
    try:
        r = requests.get(url)
    except Exception as e:
        return print(e)
    await ctx.channel.send(f"[ ]({r.json()})")
    return

class Client(commands.CommandsClient):
    async def get_prefix(self, client: revolt.Client):
        return config.revolt_prefix

    async def on_ready(self):
        print(f"Ready as: {self.user.name}#{self.user.discriminator}")

    async def on_command(self, ctx: commands.Context):
        print(
            f" {ctx.channel.channel_type} [{ctx.channel.id}] | {ctx.author.name}#{ctx.author.discriminator} -> {ctx.command.name}")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """ I wonder what this will do... """
        await ctx.send("pong")

    @commands.group(name="nsfw", aliases=[])
    async def nsfw(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await ctx.channel.send(":-1:")

    @nsfw.command(name="hass")
    async def _hass(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hass", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="assgif")
    async def _assgif(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?assgif", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?assgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="ass")
    async def _ass(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?ass", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?ass", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="boobs")
    async def _boobs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?boobs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hboobs")
    async def _hboobs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hboobs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="bbw")
    async def _bbw(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?bbw", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?bbw", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="bdsm")
    async def _bdsm(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?bdsm", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?bdsm", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="blow")
    async def _blow(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?blow", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?blow", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="feet")
    async def _feet(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?feet", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?feet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hfeet")
    async def _hfeet(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hfeet", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hfeet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="furfuta")
    async def _furfuta(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?furfuta", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?furfuta", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="furgif")
    async def _furgif(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?furgif", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?furgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="futa")
    async def _futa(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?futa", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?futa", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hthighs")
    async def _hthighs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?athighs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?athighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="thighs")
    async def _thighs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?thighs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?thighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="gifs")
    async def _gifs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?gifs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?gifs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="sex")
    async def _sex(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?sex", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?sex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="femboy")
    async def _femboy(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?irlfemb", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?irlfemb", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hfemboy")
    async def _hfemboy(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?femboy", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?femboy", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="slime")
    async def _slime(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?slime", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?slime", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="pantsu")
    async def _pantsu(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?pantsu", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?pantsu", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="milk")
    async def _milk(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?milk", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?milk", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="latex")
    async def _latex(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?latex", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?latex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hentai")
    async def _hentai(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hentai", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?hentai", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="yuri")
    async def _yuri(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?yuri", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, config.lewds_api_url + "/nsfw/?yuri", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")


async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, config.revolt_token, api_url=config.revolt_api_url")
        await client.start()

try:
    asyncio.run(main())
except:
    ""
