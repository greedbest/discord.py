"""
An example showing how to use media galleries and file components in Discord's Components V2 system.
"""

import discord
from discord.ext import commands
from discord import MessageFlags
from discord.components_v2 import Section, TextDisplay, Container, MediaGallery, File, Separator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def v2media(ctx):
    """Shows how to use media galleries and file components."""
    
    # Create header
    header = TextDisplay(content="# Media Gallery Example")
    header_section = Section(components=[header])
    
    # Create media gallery
    gallery = MediaGallery(
        media=[
            {"url": "https://example.com/image1.png"},
            {"url": "https://example.com/image2.png"},
            {"url": "https://example.com/image3.png"}
        ]
    )
    
    # Create description for gallery
    gallery_text = TextDisplay(content="Here's a gallery of images:")
    gallery_section = Section(components=[gallery_text])
    
    # Add separator
    separator = Separator(spacing="medium")
    
    # Create file section
    # Note: The file must be uploaded as an attachment to the message
    file_component = File(filename="document.pdf")
    file_text = TextDisplay(content="Here's an attached document:")
    file_section = Section(components=[file_text])
    
    # Create container with all components
    container = Container(
        components=[
            header_section,
            gallery_section,
            gallery,
            separator,
            file_section,
            file_component
        ],
        accent_color=0x5865F2
    )
    
    # Create the file to attach
    file = discord.File("path/to/document.pdf")
    
    # Send the message with Components V2 and file attachment
    await ctx.send(
        files=[file],
        components=[container],
        flags=MessageFlags.IS_COMPONENTS_V2
    )

bot.run('your token here') 