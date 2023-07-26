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

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """ I wonder what this will do... """
        await ctx.send("pong")

    @commands.group(name="nsfw", aliases=[])
    async def nsfw(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await ctx.channel.send(":-1:")

    @nsfw.command(name="hass")
    async def _hass(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?hass", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="assgif")
    async def _assgif(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?assgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="ass")
    async def _ass(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?ass", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="boobs")
    async def _boobs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?boobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="hboobs")
    async def _hboobs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?hboobs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="bbw")
    async def _bbw(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?bbw", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="bdsm")
    async def _bdsm(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?bdsm", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="blow")
    async def _blow(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?blow", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="feet")
    async def _feet(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?feet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="hfeet")
    async def _hfeet(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?hfeet", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="furfuta")
    async def _furfuta(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?furfuta", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="furgif")
    async def _furgif(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?furgif", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="futa")
    async def _futa(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?futa", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="hthighs")
    async def _hthighs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?athighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="thighs")
    async def _thighs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?thighs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="gifs")
    async def _gifs(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?gifs", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="sex")
    async def _sex(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?sex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="femboy")
    async def _femboy(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?irlfemb", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="hfemboy")
    async def _hfemboy(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?femboy", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="slime")
    async def _slime(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?slime", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="pantsu")
    async def _pantsu(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?pantsu", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="milk")
    async def _milk(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?milk", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="latex")
    async def _latex(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?latex", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="hentai")
    async def _hentai(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?hentai", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")

    @nsfw.command(name="yuri")
    async def _yuri(self, ctx: commands.Context):
        """ Posts the requested type of NSFW Image """
        if ctx.channel.nsfw:
            await randomimageapi(ctx, "https://kyra.tk/nsfw/?yuri", "file")
        else:
            return await ctx.channel.send("This channel must be an NSFW channel for this to work!")


async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, config.revolt_token)
        await client.start()

try:
    asyncio.run(main())
except:
    ""
