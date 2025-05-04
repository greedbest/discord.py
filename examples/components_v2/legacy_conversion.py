"""
An example showing that legacy components work without changes and Components V2 is completely opt-in.
This example demonstrates using both V1 and V2 components in the same bot.
"""

import discord
from discord.ext import commands
from discord import MessageFlags
from discord.components_v2 import Section, TextDisplay, Container
from discord.ui import Button, View, Select

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class LegacyView(View):
    """A normal V1 view - no changes needed for V2 compatibility"""
    def __init__(self):
        super().__init__()
        # Regular V1 components work as normal
        self.add_item(Button(label="Legacy Button", custom_id="legacy_button"))
        self.add_item(Select(
            placeholder="Legacy Select",
            options=[
                discord.SelectOption(label="Option 1"),
                discord.SelectOption(label="Option 2")
            ]
        ))

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.data.get("custom_id") == "legacy_button":
            await interaction.response.send_message("Legacy button works normally!", ephemeral=True)
        return True

@bot.command()
async def legacy(ctx):
    """A normal command using legacy components - no changes needed"""
    view = LegacyView()
    await ctx.send("This message uses legacy components:", view=view)

@bot.command()
async def v2(ctx):
    """A command using Components V2 - explicitly opt-in with the flag"""
    # Create V2 components
    text = TextDisplay(content="This message uses Components V2!")
    section = Section(components=[text])
    container = Container(components=[section])
    
    # Send with V2 flag
    await ctx.send(
        components=[container],
        flags=MessageFlags.IS_COMPONENTS_V2
    )

@bot.command()
async def both(ctx):
    """Demonstrates that the same bot can handle both V1 and V2 messages"""
    # First send a legacy message
    view = LegacyView()
    await ctx.send("This is a legacy message with V1 components:", view=view)
    
    # Then send a V2 message
    text = TextDisplay(content="This is a V2 message!")
    section = Section(components=[text])
    container = Container(components=[section])
    
    await ctx.send(
        components=[container],
        flags=MessageFlags.IS_COMPONENTS_V2
    )

@bot.event
async def on_interaction(interaction: discord.Interaction):
    """Regular interaction handling works for both V1 and V2"""
    # The bot handles interactions normally, regardless of component version
    view = discord.utils.get(bot._views.values(), custom_id="legacy_button")
    if view:
        await view.interaction_check(interaction)

bot.run('your token here') 