"""Last.fm integration commands."""

from logging import getLogger

from osmium_chat import Context, commands

logger = getLogger("osmium_chat")


class LastFMCommands(commands.Commands):
    """Last.fm related commands"""
    @commands.command("c")
    async def c(self, ctx: Context, *, size: str | None = "3x3") -> None:
        """Send the weekly collage chart at the requested size."""
        await ctx.reply(f"this should send a {size} weekly collage")

    @commands.command("login")
    async def login(self, ctx: Context) -> None:
        """Send the Last.fm authentication URL."""
        await ctx.channel.send("this should send the auth url")

    @commands.command("w")
    async def w(self, ctx: Context) -> None:
        """Send the weekly 3x3 poster."""
        await ctx.channel.send("this should send the weekly 3v3 poster")

    @commands.command("profile")
    async def profile(self, ctx: Context) -> None:
        """Send the profile of the invoking user, or a mentioned user if given."""
        await ctx.channel.send("this should send the user profile")
