from logging import getLogger

from osmium_chat import commands, Message, Context

logger = getLogger("osmium_chat")


class GeneralCommands(commands.Commands):
    @commands.listen("connect")
    async def on_connect(self) -> None:
        logger.info("Bot connected to WebSocket server")
        await self.bot.use_invite("xYnNrbRy20ZSS4rS")

    @commands.listen("message")
    async def on_message(self, message: Message) -> None:
        who = message.author.name if message.author else "someone"
        logger.info("message from %s: %s", who, message.content)

    @commands.listen("guild_message")
    async def on_guild_message(self, message: Message) -> None:
        logger.info("guild message: %s", message.content)

    @commands.listen("dm_message")
    async def on_dm_message(self, message: Message) -> None:
        logger.info("dm message: %s", message.content)

    @commands.command("say")
    async def say(self, ctx: Context, *, words: str | None = None) -> None:
        await ctx.channel.send(words or "You didn't say anything!")

    @commands.dm_command("dm")
    async def dm(self, ctx: Context) -> None:
        await ctx.channel.send("This command only works in DMs!")

    @commands.guild_command("community")
    async def community(self, ctx: Context) -> None:
        await ctx.channel.send("This command only works in community channels!")
