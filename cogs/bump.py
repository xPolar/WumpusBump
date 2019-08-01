import datetime
import discord
from discord.ext import commands
import json

class bump(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.errorcolor = 0xFF2B2B
        self.blurple = 0x7289DA

    @commands.command()
    @commands.cooldown(rate = 1, per = 3600, type = commands.BucketType.guild)
    async def bump(self, ctx):
        with open(r"DESCRIPTIONJSONFILEPATHERE", "r") as f:
            descriptions = json.load(f)
        with open(r"TITLEJSONPATHHERE", "r") as f:
            titles = json.load(f)
        with open(r"INVITEJSONFILEPATHERE", "r") as f:
            invites = json.load(f)
        channels = [606032079783723035]
        if str(ctx.message.guild.id) not in descriptions and str(ctx.message.guild.id) not in titles and str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description**, **Title**, and an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in descriptions and str(ctx.message.guild.id) not in titles:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description** and **Title** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in descriptions and str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description** and an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in titles and str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Title** and an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in descriptions:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in titles:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Title** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            title = titles[str(ctx.message.guild.id)]
            description = descriptions[str(ctx.message.guild.id)]
            invite = invites[str(ctx.message.guild.id)]
            bots = 0
            for member in ctx.guild.members:
                if member.bot == True:
                    bots += 1
            embed = discord.Embed(
                title = title,
                description = description,
                timestamp = datetime.datetime.utcnow(),
                color = self.blurple
            )
            embed.set_author(name = ctx.guild.name)
            embed.add_field(name = "Other", value = f"👥 {len(ctx.guild.members)} Total Members\n<:BotIndicator:606238977720320051> {bots} Total Bots\n😀 {len(ctx.guild.emojis)} Total Emotes\n\nFeel free to [join]({invite}) {ctx.guild.name}!")
            embed.set_footer(text = f"Currently bumping {len(self.bot.guilds)} servers!")
            for id in channels:
                channel = self.bot.get_channel(id)
                await channel.send(embed = embed)

    @bump.error
    async def bump_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
            title = "Cooldown",
            description = f"Each server can only be bumped every 6 hours! This server can be bumped again in {int(error.retry_after)}s.",
            color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def preview(self, ctx):
        with open(r"DESCRIPTIONJSONFILEPATHERE", "r") as f:
            descriptions = json.load(f)
        with open(r"TITLEJSONPATHHERE", "r") as f:
            titles = json.load(f)
        with open(r"INVITEJSONFILEPATHERE", "r") as f:
            invites = json.load(f)
        if str(ctx.message.guild.id) not in descriptions and str(ctx.message.guild.id) not in titles and str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description**, **Title**, and an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in descriptions and str(ctx.message.guild.id) not in titles:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description** and **Title** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in descriptions and str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description** and an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in titles and str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Title** and an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in descriptions:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Description** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in titles:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing a **Title** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        elif str(ctx.message.guild.id) not in invites:
            embed = discord.Embed(
                title = "Bump Error",
                description = "You are missing an **Invite** for your bump message",
                color = self.errorcolor
            )
            await ctx.send(embed = embed)
        else:
            title = titles[str(ctx.message.guild.id)]
            description = descriptions[str(ctx.message.guild.id)]
            invite = invites[str(ctx.message.guild.id)]
            bots = 0
            for member in ctx.guild.members:
                if member.bot == True:
                    bots += 1
            embed = discord.Embed(
                title = title,
                description = description,
                timestamp = datetime.datetime.utcnow(),
                color = self.blurple
            )
            embed.set_author(name = ctx.guild.name)
            embed.add_field(name = "Other", value = f"👥 {len(ctx.guild.members)} Total Members\n<:BotIndicator:606238977720320051> {bots} Total Bots\n😀 {len(ctx.guild.emojis)} Total Emotes\n\nFeel free to [join]({invite}) {ctx.guild.name}!")
            embed.set_footer(text = f"Currently bumping {len(self.bot.guilds)} servers!")
            await ctx.send(embed = embed)

    @preview.error
    async def preview_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title = "Preview Error",
            description = f"You are missing the **Manage Server** permission!",
            color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def description(self, ctx, *, description = None):
        if description == None:
            embed = discord.Embed(
                title = "Description Error",
                description = "Please provide a description!",
                color = self.errorcolor
            )
        else:
            with open(r"DESCRIPTIONJSONFILEPATHERE", "r") as f:
                descriptions = json.load(f)

            descriptions[str(ctx.guild.id)] = description
            embed = discord.Embed(
                title = "Description",
                description = f"{ctx.message.guild}'s description is  now {description}",
                color = self.blurple
            )
            await ctx.send(embed = embed)

            with open(r"DESCRIPTIONJSONFILEPATHERE", "w") as f:
                json.dump(descriptions, f, indent = 4)

    @description.error
    async def description_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title = "Description Error",
            description = f"You are missing the **Manage Server** permission!",
            color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def title(self, ctx, *, title = None):
        if title == None:
            embed = discord.Embed(
                title = "Title Error",
                description = "Please provide a title!",
                color = self.errorcolor
            )
        else:
            with open(r"TITLEJSONPATHHERE", "r") as f:
                titles = json.load(f)

            titles[str(ctx.guild.id)] = title
            embed = discord.Embed(
                title = "title",
                description = f"{ctx.message.guild}'s title is  now {title}",
                color = self.blurple
            )
            await ctx.send(embed = embed)

            with open(r"TITLEJSONPATHHERE", "w") as f:
                json.dump(titles, f, indent = 4)

    @title.error
    async def title_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title = "Title Error",
            description = f"You are missing the **Manage Server** permission!",
            color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def invite(self, ctx, *, invite = None):
        if invite == None:
            embed = discord.Embed(
                title = "Invite Error",
                description = "Please provide an invite!",
                color = self.errorcolor
            )
        else:
            with open(r"INVITEJSONFILEPATHERE", "r") as f:
                invites = json.load(f)

            invites[str(ctx.guild.id)] = invite
            embed = discord.Embed(
                title = "Invite",
                description = f"{ctx.message.guild}'s invite is now {invite}",
                color = self.blurple
            )
            await ctx.send(embed = embed)

            with open(r"INVITEJSONFILEPATHERE", "w") as f:
                json.dump(invites, f, indent = 4)

    @invite.error
    async def invite_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
            title = "Invite Error",
            description = f"You are missing the **Manage Server** permission!",
            color = self.errorcolor
            )
            await ctx.send(embed = embed, delete_after = 5.0)
            await ctx.message.delete()

def setup(bot):
    bot.add_cog(bump(bot))
