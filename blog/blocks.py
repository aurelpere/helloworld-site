from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DateTimeBlock,
    FieldBlock,
    IntegerBlock,
    ListBlock,
    PageChooserBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    StructValue,
    TextBlock,
    URLBlock,
)
from wagtail.core.models import Orderable, Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

class CustomImageChooserBlock(ImageChooserBlock): 
    pass
class ImageText(StructBlock):
    reverse = BooleanBlock(required=False) 
    text = RichTextBlock()
    image = CustomImageChooserBlock()
class BodyBlock(StreamBlock): 
    h1 = CharBlock()
    h2 = CharBlock()
    paragraph = RichTextBlock()
    image_text = ImageText()
    image_carousel = ListBlock(CustomImageChooserBlock()) 
    thumbnail_gallery = ListBlock(CustomImageChooserBlock())