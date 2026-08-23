from logging import getLogger

from osmium_chat import commands, Message, Context

logger = getLogger("osmium_chat")


class LastFMCommands(commands.Commands):
    @commands.command("c")
    async def c(self, ctx: Context, *, size: str | None = "3x3", ) -> None:
        await ctx.reply("this should send the default 3v3 weekly")

    @commands.command("login")
    async def login(self, ctx: Context) -> None:
        await ctx.channel.send("this should send the auth url")

    @commands.command("w")
    async def w(self, ctx: Context) -> None:
        await ctx.channel.send("this should send the weekly 3v3 poster")

    #NOTE: this should, by default, send the profile of the user who casted the command, or the mentioned user as an arg.
    @commands.command("profile")
    async def profile(self, ctx: Context) -> None:
        await ctx.channel.send("this should send, by default, the user who casted ")
