from logging import getLogger

from osmium_chat import commands, Message, Context

logger = getLogger("osmium_chat")


class LastFMCommands(commands.Commands):
    @commands.command("c")
    async def c(self, ctx: Context, *, words: str | None = None) -> None:
        await ctx.reply(words or "no args")

    @commands.command("login")
    async def login(self, ctx: Context) -> None:
        await ctx.channel.send("this should send the auth url")

    @commands.command("join")
    async def join(self, ctx: Context, code: str) -> None:
        await ctx.bot.use_invite(code)
        await ctx.reply(f"Joined via {code}.")
