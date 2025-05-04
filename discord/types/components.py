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

from typing import List, Literal, TypedDict, Union, Optional
from typing_extensions import NotRequired

from .emoji import PartialEmoji
from .channel import ChannelType

ComponentType = Literal[1, 2, 3, 4]
ButtonStyle = Literal[1, 2, 3, 4, 5, 6]
TextStyle = Literal[1, 2]
DefaultValueType = Literal['user', 'role', 'channel']


class ActionRow(TypedDict):
    type: Literal[1]
    components: List[ActionRowChildComponent]


class ButtonComponent(TypedDict):
    type: Literal[2]
    style: ButtonStyle
    custom_id: NotRequired[str]
    url: NotRequired[str]
    disabled: NotRequired[bool]
    emoji: NotRequired[PartialEmoji]
    label: NotRequired[str]
    sku_id: NotRequired[str]


class SelectOption(TypedDict):
    label: str
    value: str
    default: bool
    description: NotRequired[str]
    emoji: NotRequired[PartialEmoji]


class SelectComponent(TypedDict):
    custom_id: str
    placeholder: NotRequired[str]
    min_values: NotRequired[int]
    max_values: NotRequired[int]
    disabled: NotRequired[bool]


class SelectDefaultValues(TypedDict):
    id: int
    type: DefaultValueType


class StringSelectComponent(SelectComponent):
    type: Literal[3]
    options: NotRequired[List[SelectOption]]


class UserSelectComponent(SelectComponent):
    type: Literal[5]
    default_values: NotRequired[List[SelectDefaultValues]]


class RoleSelectComponent(SelectComponent):
    type: Literal[6]
    default_values: NotRequired[List[SelectDefaultValues]]


class MentionableSelectComponent(SelectComponent):
    type: Literal[7]
    default_values: NotRequired[List[SelectDefaultValues]]


class ChannelSelectComponent(SelectComponent):
    type: Literal[8]
    channel_types: NotRequired[List[ChannelType]]
    default_values: NotRequired[List[SelectDefaultValues]]


class TextInput(TypedDict):
    type: Literal[4]
    custom_id: str
    style: TextStyle
    label: str
    placeholder: NotRequired[str]
    value: NotRequired[str]
    required: NotRequired[bool]
    min_length: NotRequired[int]
    max_length: NotRequired[int]


class SelectMenu(SelectComponent):
    type: Literal[3, 5, 6, 7, 8]
    options: NotRequired[List[SelectOption]]
    channel_types: NotRequired[List[ChannelType]]
    default_values: NotRequired[List[SelectDefaultValues]]


ActionRowChildComponent = Union[ButtonComponent, SelectMenu, TextInput]
Component = Union[ActionRow, ActionRowChildComponent]

class SectionComponent(TypedDict):
    type: Literal[9]
    id: Optional[int]
    components: List[Union['TextDisplayComponent', 'Component']]
    accessory: Optional[Union['ButtonComponent', 'ThumbnailComponent']]

class TextDisplayComponent(TypedDict):
    type: Literal[10]
    content: str

class ThumbnailComponent(TypedDict):
    type: Literal[11]
    url: str
    height: Optional[int]
    width: Optional[int]

class MediaGalleryItem(TypedDict):
    media: UnfurledMediaItem
    description: NotRequired[str]
    spoiler: NotRequired[bool]

class UnfurledMediaItem(TypedDict):
    url: str

class MediaGalleryComponent(TypedDict):
    type: Literal[12]
    id: NotRequired[int]
    items: List[MediaGalleryItem]

class FileComponent(TypedDict):
    type: Literal[13]
    id: NotRequired[int]
    file: UnfurledMediaItem
    spoiler: NotRequired[bool]

class SeparatorComponent(TypedDict):
    type: Literal[14]
    id: NotRequired[int]
    divider: NotRequired[bool]
    spacing: NotRequired[Literal[1, 2]]

class ContainerComponent(TypedDict):
    type: Literal[17]
    id: NotRequired[int]
    components: List[Union[ActionRow, TextDisplayComponent, SectionComponent, MediaGalleryComponent, SeparatorComponent, FileComponent]]
    accent_color: NotRequired[int]
    spoiler: NotRequired[bool]

ComponentV2 = Union[SectionComponent, TextDisplayComponent, ThumbnailComponent, MediaGalleryComponent, FileComponent, SeparatorComponent, ContainerComponent]
