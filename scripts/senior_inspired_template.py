#!/usr/bin/env python3
"""Public-safe editable PowerPoint style primitives for the thesis proposal.

This is a content-free template. Do not copy private thesis source or the senior's
slides into this public repository. Uses python-pptx and a 20 x 11.25 in canvas.
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

WIDTH, HEIGHT = 20, 11.25
COLORS = {
    "background": "F8F8F8", "wine": "A31F34", "tan": "8C6E4A",
    "ink": "171717", "muted": "666461", "rule": "D9D4CE",
}
TITLE_FONT = "Georgia"  # substitution for unavailable Cormorant Garamond
BODY_FONT = "Times New Roman"
UI_FONT = "Lato"
NAV = ["Contents", "Introduction", "Literature Review",
       "Method", "Experimental Plan", "References"]
NAV_WIDTHS = [2.9, 3.0, 3.6, 2.3, 3.8, 2.3]

def color(key):
    return RGBColor.from_string(COLORS.get(key, key).lstrip("#"))

def add_text(slide, value, x, y, w, h, size=24, tone="ink",
             family=BODY_FONT, italic=False, bold=False, centered=False):
    s = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = s.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(value.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.CENTER if centered else PP_ALIGN.LEFT
        p.text = line
        for run in p.runs:
            run.font.name = family
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.italic = italic
            run.font.color.rgb = color(tone)
    return s

def rect(slide, x, y, w, h, fill, rounded=False):
    typ = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    s = slide.shapes.add_shape(typ, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = color(fill)
    s.line.fill.background()
    return s

def new_deck():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(WIDTH), Inches(HEIGHT)
    return prs

def new_blank(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = color("background")
    return slide

def add_footer(slide, current_section, index):
    rect(slide, 0, 10.56, WIDTH, 0.69, "wine")
    x = 1.05
    for name, width in zip(NAV, NAV_WIDTHS):
        if name == current_section:
            rect(slide, x - .13, 10.49, width - .19, .74, "background", True)
            tone = "wine"
        else:
            tone = "background"
        add_text(slide, name, x, 10.64, width - .44, .36, 19, tone,
                 UI_FONT, italic=True, bold=name == current_section, centered=True)
        x += width
    add_text(slide, f"{index:02d}", 18.76, 10.64, .70, .36, 21,
             "background", UI_FONT, bold=True, centered=True)

def add_section_header(slide, chapter, title, crumbs, active_crumb, section, page):
    add_text(slide, chapter.upper(), 1.06, .52, 6.3, .31, 15,
             "tan", UI_FONT, bold=True)
    add_text(slide, title, 1.03, 1.03, 17.9, 1.10, 53,
             "wine", TITLE_FONT, italic=True, bold=True)
    rect(slide, 1.06, 2.31, 2.25, .055, "wine")
    x = 10.48
    for index, crumb in enumerate(crumbs):
        w = 2.63 if len(crumbs) == 3 else 2.04
        active = index == active_crumb
        add_text(slide, crumb.upper(), x, .50, w, .29, 14.4,
                 "wine" if active else "muted", UI_FONT, bold=active,
                 centered=True)
        if active:
            rect(slide, x + .2, .86, w - .4, .033, "wine")
        x += w
    add_footer(slide, section, page)

if __name__ == "__main__":
    deck = new_deck()
    s = new_blank(deck)
    add_section_header(s, "Chapter / Section", "Editable Slide Title",
                       ["Context", "Method", "Evidence"], 0, "Introduction", 3)
    add_text(s, "Replace this placeholder with one verified claim.", 1.1,
             3.1, 17.0, .7, 30)
    deck.save("style_template_preview.pptx")
