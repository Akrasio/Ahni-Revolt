from revolt.ext import commands
import aiohttp
import revolt
import asyncio
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
        r = await http.get(url, res_method="json")
        async with aiohttp.ClientSession() as session:
            async with session.get(r.response) as resp:
                buffer = BytesIO(await resp.read())
                await session.close()
    except aiohttp.ClientConnectorError:
        return await ctx.channel.send("The API seems to be down...")
    except aiohttp.ContentTypeError:
        return await ctx.channel.send("The API returned an error...")

    fileinfo = filetype.guess(buffer)
    fileExt = fileinfo.extension
    await ctx.channel.send(attachments=[revolt.File(buffer.read(), filename=f"SPOILER_NSFW.{fileExt}")])
    return resp.close()


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
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hass", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="assgif")
    async def _assgif(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?assgif", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?assgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="ass")
    async def _ass(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?ass", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?ass", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="boobs")
    async def _boobs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?boobs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hboobs")
    async def _hboobs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hboobs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="bbw")
    async def _bbw(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?bbw", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?bbw", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="bdsm")
    async def _bdsm(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?bdsm", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?bdsm", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="blow")
    async def _blow(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?blow", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?blow", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="feet")
    async def _feet(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?feet", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?feet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hfeet")
    async def _hfeet(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hfeet", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hfeet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="furfuta")
    async def _furfuta(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?furfuta", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?furfuta", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="furgif")
    async def _furgif(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?furgif", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?furgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="futa")
    async def _futa(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?futa", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?futa", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hthighs")
    async def _hthighs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?athighs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?athighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="thighs")
    async def _thighs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?thighs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?thighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="gifs")
    async def _gifs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?gifs", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?gifs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="sex")
    async def _sex(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?sex", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?sex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="femboy")
    async def _femboy(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?irlfemb", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?irlfemb", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hfemboy")
    async def _hfemboy(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?femboy", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?femboy", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="slime")
    async def _slime(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?slime", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?slime", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="pantsu")
    async def _pantsu(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?pantsu", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?pantsu", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="milk")
    async def _milk(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?milk", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?milk", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="latex")
    async def _latex(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?latex", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?latex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="hentai")
    async def _hentai(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hentai", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?hentai", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")

    @nsfw.command(name="yuri")
    async def _yuri(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.server_id and ctx.channel.nsfw:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?yuri", "file")
        elif not ctx.server_id and ctx.channel.channel_type != revolt.ChannelType.group:
            await randomimageapi(ctx, "https://revoltbots.org/nsfw/?yuri", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel or Private DM for this to work!")


async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, config.revolt_token, api_url=config.revolt_api_url or "https://api.revolt.chat")
        await client.start()

try:
    asyncio.run(main())
except:
    ""
