"""Connection lifecycle, message logging and utility commands."""

from logging import getLogger

from osmium_chat import Context, commands

logger = getLogger("osmium_chat")


class CoreCommands(commands.Commands):
    """Connection lifecycle listeners + general-purpose commands."""

    @commands.listen("connect")
    async def on_connect(self) -> None:
        """Log a successful connection to the gateway."""
        logger.info("Bot connected to WebSocket server")

    @commands.command("say")
    async def say(self, ctx: Context, *, words: str | None = None) -> None:
        """Echo the given words back into the channel."""
        await ctx.channel.send(words or "You didn't say anything!")

    @commands.command("join")
    async def join(self, ctx: Context, code: str) -> None:
        """Join a community via an invite code."""
        await ctx.bot.use_invite(code)
        await ctx.reply(f"Joined via {code}.")
