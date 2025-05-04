"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations
from typing import ClassVar, List, Literal, Optional, TYPE_CHECKING, Tuple, Union, Dict, Any

from .components import Component, Button
from .enums import ComponentType
from .utils import MISSING

if TYPE_CHECKING:
    from typing_extensions import Self
    from .types.components import Component as ComponentPayload

__all__ = (
    'Section',
    'TextDisplay',
    'Container',
    'MediaGalleryItem',
    'MediaGallery',
    'File',
    'SeparatorSpacing',
    'Separator',
)

class Section(Component):
    """Represents a Discord Bot UI Kit Section Component (V2).

    A Section is a top-level layout component that allows you to join text
    contextually with an accessory.

    This inherits from :class:`Component`.

    Parameters
    -----------
    components: List[:class:`TextDisplay`]
        One to three text components to display in the section.
    accessory: Optional[Union[:class:`Button`, :class:`Thumbnail`]]
        A thumbnail or button component to display as an accessory.
    id: Optional[:class:`int`]
        The identifier for the section component.

    Attributes
    -----------
    components: List[:class:`TextDisplay`]
        The text components in this section.
    accessory: Optional[Union[:class:`Button`, :class:`Thumbnail`]]
        The accessory component, if any.
    id: Optional[:class:`int`]
        The identifier for this section, if any.
    """

    __slots__: Tuple[str, ...] = (
        'components',
        'accessory',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(
        self, 
        *, 
        components: List[TextDisplay], 
        accessory: Optional[Union[Button, Thumbnail]] = None, 
        id: Optional[int] = None
    ) -> None:
        if not components:
            raise ValueError('Section must contain at least one text component')
        if len(components) > 3:
            raise ValueError('Section can only contain up to 3 text components')
        if not all(isinstance(comp, TextDisplay) for comp in components):
            raise TypeError('All components must be TextDisplay instances')
        if accessory is not None and not isinstance(accessory, (Button, Thumbnail)):
            raise TypeError('Accessory must be either a Button or Thumbnail instance')
        
        self.components = components
        self.accessory = accessory
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.section]:
        return ComponentType.section

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
            'components': [component.to_dict() for component in self.components],
        }
        
        if self.accessory is not None:
            payload['accessory'] = self.accessory.to_dict()
            
        if self.id is not None:
            payload['id'] = self.id
            
        return payload

class TextDisplay(Component):
    """Represents a text display component in Discord Bot UI Kit V2.
    
    This component is used to display text content in V2 messages with markdown support.

    Parameters
    -----------
    content: :class:`str`
        The text content to display. Supports markdown formatting.
    id: Optional[:class:`int`]
        The identifier for this component.

    Attributes
    -----------
    content: :class:`str`
        The text content being displayed.
    id: Optional[:class:`int`]
        The identifier for this component, if any.
    """

    __slots__: Tuple[str, ...] = (
        'content',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(self, *, content: str, id: Optional[int] = None) -> None:
        self.content = content
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.text_display]:
        return ComponentType.text_display

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
            'content': self.content,
        }
        
        if self.id is not None:
            payload['id'] = self.id
            
        return payload

class Container(Component):
    """Represents a container component in Discord Bot UI Kit V2.
    
    This component is used to group components with optional visual styling.
    Containers are visually distinct from surrounding components and can have
    a customizable color bar.

    Parameters
    -----------
    components: List[Union[:class:`ActionRow`, :class:`TextDisplay`, :class:`Section`, :class:`MediaGallery`, :class:`Separator`, :class:`File`]]
        The components to include in this container.
    accent_color: Optional[:class:`int`]
        Color for the accent on the container as RGB from 0x000000 to 0xFFFFFF.
    spoiler: :class:`bool`
        Whether the container should be marked as a spoiler. Defaults to False.
    id: Optional[:class:`int`]
        The identifier for this component.

    Attributes
    -----------
    components: List[Union[:class:`ActionRow`, :class:`TextDisplay`, :class:`Section`, :class:`MediaGallery`, :class:`Separator`, :class:`File`]]
        The components in this container.
    accent_color: Optional[:class:`int`]
        The accent color of the container, if any.
    spoiler: :class:`bool`
        Whether the container is marked as a spoiler.
    id: Optional[:class:`int`]
        The identifier for this component, if any.
    """

    __slots__: Tuple[str, ...] = (
        'components',
        'accent_color',
        'spoiler',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(
        self, 
        *, 
        components: List[Union[ActionRow, TextDisplay, Section, MediaGallery, Separator, File]],
        accent_color: Optional[int] = None,
        spoiler: bool = False,
        id: Optional[int] = None
    ) -> None:
        if not components:
            raise ValueError('Container must contain at least one component')
            
        valid_types = (ActionRow, TextDisplay, Section, MediaGallery, Separator, File)
        if not all(isinstance(comp, valid_types) for comp in components):
            raise TypeError('All components must be one of: ActionRow, TextDisplay, Section, MediaGallery, Separator, or File')
            
        if accent_color is not None and not 0 <= accent_color <= 0xFFFFFF:
            raise ValueError('accent_color must be between 0x000000 and 0xFFFFFF')
        
        self.components = components
        self.accent_color = accent_color
        self.spoiler = spoiler
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.container]:
        return ComponentType.container

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
            'components': [component.to_dict() for component in self.components],
        }
        
        if self.accent_color is not None:
            payload['accent_color'] = self.accent_color
            
        if self.spoiler:
            payload['spoiler'] = True
            
        if self.id is not None:
            payload['id'] = self.id
            
        return payload

class Thumbnail(Component):
    """Represents a thumbnail component in Discord Bot UI Kit V2.
    
    This component can be used as an accessory in sections to display small images.

    Parameters
    -----------
    media_url: :class:`str`
        The URL of the media to display.
    description: Optional[:class:`str`]
        Alt text for the media.
    spoiler: :class:`bool`
        Whether the thumbnail should be marked as a spoiler.
    id: Optional[:class:`int`]
        The identifier for this component.

    Attributes
    -----------
    media_url: :class:`str`
        The URL of the media being displayed.
    description: Optional[:class:`str`]
        Alt text for the media, if any.
    spoiler: :class:`bool`
        Whether the thumbnail is marked as a spoiler.
    id: Optional[:class:`int`]
        The identifier for this component, if any.
    """

    __slots__: Tuple[str, ...] = (
        'media_url',
        'description',
        'spoiler',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(
        self, 
        *, 
        media_url: str,
        description: Optional[str] = None,
        spoiler: bool = False,
        id: Optional[int] = None
    ) -> None:
        self.media_url = media_url
        self.description = description
        self.spoiler = spoiler
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.thumbnail]:
        return ComponentType.thumbnail

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
            'media': {
                'url': self.media_url
            }
        }
        
        if self.description is not None:
            payload['description'] = self.description
            
        if self.spoiler:
            payload['spoiler'] = True
            
        if self.id is not None:
            payload['id'] = self.id
            
        return payload 

@dataclass
class MediaGalleryItem:
    """Represents a media item in a MediaGallery component.
    
    Parameters
    -----------
    media_url: :class:`str`
        The URL of the media to display.
    description: Optional[:class:`str`]
        Alt text for the media.
    spoiler: :class:`bool`
        Whether the media should be marked as a spoiler.
    """
    
    media_url: str
    description: Optional[str] = None
    spoiler: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        payload = {
            'media': {
                'url': self.media_url
            }
        }
        
        if self.description is not None:
            payload['description'] = self.description
            
        if self.spoiler:
            payload['spoiler'] = True
            
        return payload

class MediaGallery(Component):
    """Represents a media gallery component in Discord Bot UI Kit V2.
    
    This component allows displaying 1-10 media items in an organized gallery format.

    Parameters
    -----------
    items: List[:class:`MediaGalleryItem`]
        A list of 1-10 media items to display.
    id: Optional[:class:`int`]
        The identifier for this component.

    Attributes
    -----------
    items: List[:class:`MediaGalleryItem`]
        The media items being displayed.
    id: Optional[:class:`int`]
        The identifier for this component, if any.
    """

    __slots__: Tuple[str, ...] = (
        'items',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(
        self, 
        *, 
        items: List[MediaGalleryItem],
        id: Optional[int] = None
    ) -> None:
        if not items:
            raise ValueError('MediaGallery must contain at least one item')
        if len(items) > 10:
            raise ValueError('MediaGallery can only contain up to 10 items')
        if not all(isinstance(item, MediaGalleryItem) for item in items):
            raise TypeError('All items must be MediaGalleryItem instances')
        
        self.items = items
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.media_gallery]:
        return ComponentType.media_gallery

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
            'items': [item.to_dict() for item in self.items],
        }
        
        if self.id is not None:
            payload['id'] = self.id
            
        return payload 

class File(Component):
    """Represents a file component in Discord Bot UI Kit V2.
    
    This component allows displaying a single file attachment in a message.
    The file must be uploaded as an attachment to the message.

    Parameters
    -----------
    filename: :class:`str`
        The name of the file attachment to reference.
    spoiler: :class:`bool`
        Whether the file should be marked as a spoiler.
    id: Optional[:class:`int`]
        The identifier for this component.

    Attributes
    -----------
    filename: :class:`str`
        The name of the file being referenced.
    spoiler: :class:`bool`
        Whether the file is marked as a spoiler.
    id: Optional[:class:`int`]
        The identifier for this component, if any.
    """

    __slots__: Tuple[str, ...] = (
        'filename',
        'spoiler',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(
        self, 
        *, 
        filename: str,
        spoiler: bool = False,
        id: Optional[int] = None
    ) -> None:
        self.filename = filename
        self.spoiler = spoiler
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.file]:
        return ComponentType.file

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
            'file': {
                'url': f'attachment://{self.filename}'
            }
        }
        
        if self.spoiler:
            payload['spoiler'] = True
            
        if self.id is not None:
            payload['id'] = self.id
            
        return payload 

class SeparatorSpacing:
    """Represents the spacing options for a Separator component.

    Attributes
    -----------
    SMALL: :class:`int`
        Small padding (1)
    LARGE: :class:`int`
        Large padding (2)
    """
    SMALL = 1
    LARGE = 2

class Separator(Component):
    """Represents a separator component in Discord Bot UI Kit V2.
    
    This component adds vertical padding and visual division between other components.

    Parameters
    -----------
    divider: :class:`bool`
        Whether a visual divider should be displayed. Defaults to True.
    spacing: :class:`int`
        Size of separator padding. Use :class:`SeparatorSpacing` constants.
        Defaults to :attr:`SeparatorSpacing.SMALL`.
    id: Optional[:class:`int`]
        The identifier for this component.

    Attributes
    -----------
    divider: :class:`bool`
        Whether a visual divider is displayed.
    spacing: :class:`int`
        The size of the separator padding.
    id: Optional[:class:`int`]
        The identifier for this component, if any.
    """

    __slots__: Tuple[str, ...] = (
        'divider',
        'spacing',
        'id',
    )

    __repr_info__: ClassVar[Tuple[str, ...]] = __slots__

    def __init__(
        self, 
        *, 
        divider: bool = True,
        spacing: int = SeparatorSpacing.SMALL,
        id: Optional[int] = None
    ) -> None:
        if spacing not in (SeparatorSpacing.SMALL, SeparatorSpacing.LARGE):
            raise ValueError('spacing must be either SeparatorSpacing.SMALL or SeparatorSpacing.LARGE')
        
        self.divider = divider
        self.spacing = spacing
        self.id = id

    @property
    def type(self) -> Literal[ComponentType.separator]:
        return ComponentType.separator

    def to_dict(self) -> ComponentPayload:
        payload = {
            'type': self.type.value,
        }
        
        if not self.divider:
            payload['divider'] = False
            
        if self.spacing != SeparatorSpacing.SMALL:
            payload['spacing'] = self.spacing
            
        if self.id is not None:
            payload['id'] = self.id
            
        return payload 