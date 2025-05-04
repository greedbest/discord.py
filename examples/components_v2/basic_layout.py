"""
An example showing how to use Discord's Components V2 system for message layouts.
"""

import discord
from discord.ext import commands
from discord import MessageFlags
from discord.components_v2 import Section, TextDisplay, Container, Thumbnail, Button

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def v2layout(ctx):
    """Shows a basic Components V2 layout with text, thumbnail, and button."""
    
    # Create text components
    title = TextDisplay(content="# Welcome to Components V2!")
    description = TextDisplay(content="This is a demonstration of Discord's new message layout system.")
    
    # Create a thumbnail
    thumbnail = Thumbnail(
        media_url="https://example.com/image.png",
        description="Example thumbnail"
    )
    
    # Create a button
    button = Button(style=discord.ButtonStyle.primary, label="Click me!", custom_id="demo_button")
    
    # Create sections
    header_section = Section(components=[title])
    content_section = Section(
        components=[description],
        accessory=thumbnail
    )
    button_section = Section(
        components=[TextDisplay(content="Try the button:")],
        accessory=button
    )
    
    # Create container with all sections
    container = Container(
        components=[header_section, content_section, button_section],
        accent_color=0x5865F2  # Discord Blurple
    )
    
    # Send the message with Components V2
    await ctx.send(
        components=[container],
        flags=MessageFlags.IS_COMPONENTS_V2
    )

@bot.event
async def on_interaction(interaction: discord.Interaction):
    """Handle button clicks"""
    if interaction.data.get("custom_id") == "demo_button":
        await interaction.response.send_message("Button clicked!", ephemeral=True)

bot.run('your token here') 