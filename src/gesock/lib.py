import re
import tomllib
from textwrap import wrap
from wand.color import Color
from wand.drawing import Drawing
from gesock.model import Style


def word_wrap(image, ctx, text, roi_width, roi_height):
    """Break long text to multiple lines, and reduce point size
    until all text fits within a bounding box."""
    mutable_message = text
    iteration_attempts = 100

    def eval_metrics(txt):
        """Quick helper function to calculate width/height of text."""
        metrics = ctx.get_font_metrics(image, txt, True)
        return (metrics.text_width, metrics.text_height)

    while ctx.font_size > 0 and iteration_attempts:
        iteration_attempts -= 1
        width, height = eval_metrics(mutable_message)
        if height > roi_height:
            ctx.font_size -= 0.75  # Reduce pointsize
            mutable_message = text  # Restore original text
        elif width > roi_width:
            columns = len(mutable_message)
            while columns > 0:
                columns -= 1
                mutable_message = "\n".join(wrap(mutable_message, columns))
                wrapped_width, _ = eval_metrics(mutable_message)
                if wrapped_width <= roi_width:
                    break
            if columns < 1:
                ctx.font_size -= 0.75  # Reduce pointsize
                mutable_message = text  # Restore original text
        else:
            break
    if iteration_attempts < 1:
        raise RuntimeError("Unable to calculate word_wrap for " + text)
    return mutable_message


def generate_slug(text):
    """Takes a string and converts it to a dashed version of the string in
    lowercase"""

    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    prep_str = text.strip().lower()

    return _RE_COMBINE_WHITESPACE.sub(" ", prep_str).replace(" ", "-")


def draw_on_image(img, data):

    if data is None:
        return

    input, file = data

    with file as fp:
        raw_config = tomllib.load(fp)

    config = Style(**raw_config)

    with Drawing() as ctx:
        ctx.fill_color = Color(config.color)
        ctx.font_family = config.font.family
        ctx.font_style = config.font.style
        ctx.font_weight = config.font.weight
        ctx.text_interline_spacing = config.font.leading
        ctx.font_size = config.font.size
        mutable_message = word_wrap(img, ctx, input,
                                    config.max_width,
                                    config.max_height)
        ctx.text(config.x_position, config.y_position,
                 mutable_message)
        ctx.draw(img)
