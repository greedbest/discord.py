# Components V2 Examples

This directory contains examples demonstrating how to use Discord's Components V2 system with discord.py.

## Important Note About Compatibility

Components V2 is completely opt-in and won't affect your existing bot code:
- Legacy components (V1) continue to work exactly as before, no changes needed
- V2 components are only used when explicitly enabled with `MessageFlags.IS_COMPONENTS_V2`
- You can use both V1 and V2 components in the same bot - each message decides which system to use
- Legacy event handlers and interactions work without any changes

## Files

- `basic_layout.py`: Shows basic usage of Components V2 with sections, text displays, thumbnails, and buttons
- `media_and_files.py`: Demonstrates how to use media galleries and file components
- `legacy_conversion.py`: Shows how to use V1 and V2 components in the same bot

## Running the Examples

1. Install discord.py with Components V2 support
2. Replace 'your token here' with your bot token in each example
3. Run any example with Python:
   ```bash
   python basic_layout.py
   ```

## When to Use V2

Components V2 is optional and best used when you need:
- More complex message layouts
- Better text formatting and markdown support
- Media galleries or file displays
- Visual separators and containers
- Accent colors and styling

If you're happy with legacy components, you can continue using them as normal.

## Component Types

The examples demonstrate these V2 component types:
- Section (type 9): Layout component for text with accessories
- TextDisplay (type 10): Text content with markdown support
- Thumbnail (type 11): Small images for section accessories
- MediaGallery (type 12): Gallery for 1-10 media items
- File (type 13): File attachment display
- Separator (type 14): Visual divider with spacing options
- Container (type 17): Top-level layout with accent colors 