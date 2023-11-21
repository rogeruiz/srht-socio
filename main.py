from textwrap import wrap
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


def draw_roi(contxt, roi_width, roi_height):
    """Let's draw a blue box so we can identify what
    our region of interest is."""
    ctx.push()
    ctx.stroke_color = Color('BLUE')
    ctx.fill_color = Color('TRANSPARENT')
    ctx.rectangle(left=75, top=255, width=roi_width, height=roi_height)
    ctx.pop()


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
                mutable_message = '\n'.join(wrap(mutable_message, columns))
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


message = """This is some really long sentence with the
 word "Mississippi" in it."""

ROI_SIDE = 175

with Image(filename='logo:') as img:
    with Drawing() as ctx:
        draw_roi(ctx, ROI_SIDE, ROI_SIDE)
        # Set the font style
        ctx.fill_color = Color('RED')
        ctx.font_family = 'Times New Roman'
        ctx.font_size = 32
        mutable_message = word_wrap(img,
                                    ctx,
                                    message,
                                    ROI_SIDE,
                                    ROI_SIDE)
        ctx.text(75, 275, mutable_message)
        ctx.draw(img)
        img.save(filename='draw-word-wrap.png')
