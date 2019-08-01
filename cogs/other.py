import discord
from discord.ext import commands
import json

class other(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.errorcolor = 0xFF2B2B
        self.blurple = 0x7289DA

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def prefix(self, ctx, *, pre):
        with open(r"PREFIXESJSONPATHHERE", "r") as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        embed = discord.Embed(
            title = "Prefix",
            description = f"{ctx.message.guild}'s prefix is  now `{pre}`",
            color = self.blurple
        )
        await ctx.send(embed = embed)

        with open(r"PREFIXESJSONPATHHERE", "w") as f:
            json.dump(prefixes, f, indent = 4)

    @commands.command()
    async def help(self, ctx, module = None):
        with open(r"PREFIXESJSONPATHHERE", "r") as f:
            prefixes = json.load(f)
        if str(ctx.message.guild.id) not in prefixes:
            prefix = "b!"
        else:
            prefix = prefixes[str(ctx.message.guild.id)]
        if module == None:
            embed = discord.Embed(
                title = "Bump",
                description = "`5 Total Commands`",
                color = self.blurple
            )
            embed.set_author(name = "Categorys")
            embed.add_field(name = "Other", value = "`3 Total Command`")
            embed.set_footer(text = f"For more information on each category do {prefix}help (Category).")
            await ctx.send(embed = embed)
        elif module.lower() == "bump":
            embed = discord.Embed(
                title = "Commands",
                description = "**Bump** - Bumps your server to bump channels.\n**Preview** - Preview your bump message.\n**Title** - Set the title for your bump message.\n**Description** - Set the description for your bump message.\n**Invite** - Set the invite for your bump message.",
                color = self.blurple
            )
            embed.set_footer(text = f"For more information on each command do {prefix}help (Command).")
            await ctx.send(embed = embed)
        elif module.lower() == "other":
            embed = discord.Embed(
                title = "Commands",
                description = "**Help** - Shows the help message.",
                color = self.blurple
            )
            embed.set_footer(text = f"For more information on each command do {prefix}help (Command).")
            await ctx.send(embed = embed)
        elif module.lower() == "bump":
            embed = discord.Embed(
                title = "Description",
                description = "Bump your server to other servers.",
                color = self.blurple
            )
            ember.set_author(name = "Bump")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
            await ctx.send(embed = embed)
        elif module.lower() == "preview":
            embed = discord.Embed(
                title = "Description",
                description = "Preview your bump message.",
                color = self.blurple
            )
            ember.set_author(name = "Preview")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
            await ctx.send(embed = embed)
        elif module.lower() == "title":
            embed = discord.Embed(
                title = "Description",
                description = "Set the title for your bump message.",
                color = self.blurple
            )
            ember.set_author(name = "Title")
            embed.add_field(name = "Usage", value = f"{prefix}title (Title)")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
            await ctx.send(embed = embed)
        elif module.lower() == "description":
            embed = discord.Embed(
                title = "Description",
                description = "Sets the description for your bump message.",
                color = self.blurple
            )
            ember.set_author(name = "Description")
            embed.add_field(name = "Usage", value = f"{prefix}description (Description)")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
            await ctx.send(embed = embed)
        elif module.lower() == "invite":
            embed = discord.Embed(
                title = "Description",
                description = "Sets the description for your bump message.",
                color = self.blurple
            )
            ember.set_author(name = "Invite")
            embed.add_field(name = "Usage", value = f"{prefix}invite (Invite Link)")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
            await ctx.send(embed = embed)
        elif module.lower() == "support":
            embed = discord.Embed(
                title = "Description",
                description = "Invites you to the bot support server.",
                color = self.blurple
            )
            ember.set_author(name = "Support")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
        elif module.lower() == "botinvite":
            embed = discord.Embed(
                title = "Description",
                description = "Gives you the link to invite the bot.",
                color = self.blurple
            )
            ember.set_author(name = "Botinvite")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
        elif module.lower() == "prefix":
            embed = discord.Embed(
                title = "Description",
                description = "Set your server's prefix.",
                color = self.blurple
            )
            ember.set_author(name = "Prefix")
            embed.add_field(name = "Usage", value = f"{prefix}prefix (New Prefix)")
            embed.set_footer(text = f"For more information join the support server with {prefix}support.")
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = "Help Error",
                description = f"{module} is not a category/command!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)

    @commands.command()
    async def botinvite(self, ctx):
        embed = discord.Embed(
            title = "Feel free to invite me!",
            url = "https://discordapp.com/api/oauth2/authorize?client_id=606029148162490369&permissions=8&scope=bot",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            title = "Feel free to join the support server!",
            url = "https://discord.gg/r6e3CNq",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    #Ping command
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title = f"Pong! {round(self.bot.latency * 1000)} ms",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    #Leave command
    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def leave(self, ctx):
        embed = discord.Embed(
            title = "Leave",
            description = "I have left this server, please let the devs know why you wanted to remove the bot by joining the [Support Server](https://discordapp.com/invite/tjA5ssJ).",
            color = self.errorcolor
        )
        await ctx.send(embed = embed)
        await ctx.guild.leave()

    @commands.command()
    async def github(self, ctx):
        embed = discord.Embed(
            title = "Feel free to view the github!",
            url = "https://github.com/xPolar/WumpusBump",
            color = self.blurple
        )
        await ctx.send(embed = embed)

    @leave.error
    async def leave_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You are missing the **Manage Server** permission!",
                color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(other(bot))
