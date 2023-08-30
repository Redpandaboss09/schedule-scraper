from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from configparser import ConfigParser

import data_cleaner as dc

config = ConfigParser()
config.read('../configs/pdf_config.ini')

def create_schedule(data: list()):
    # Create the pdf
    pdf = SimpleDocTemplate("schedule.pdf", pagesize=landscape(A4))

    # Convert the data to paragraphs
    data = dc.convert_to_paragraphs(data)

    # Create the table
    table = Table(data, colWidths=117)

    # Create custom colors
    color_days = colors.HexColor('#' + str(config['COLOR OPTIONS']['color_dayHeader']))
    color_day_text = colors.HexColor('#' + str(config['COLOR OPTIONS']['color_textDay']))
    color_blocks = [colors.HexColor('#' + value) for key, value in config.items('COLOR OPTIONS') if key.startswith('color_block')]

    # Add custom font
    pdfmetrics.registerFont(TTFont('Georgia-Bold', 'C:/Windows/Fonts/georgiab.ttf'))
    pdfmetrics.registerFont(TTFont('Georgia', 'C:/Windows/Fonts/georgia.ttf'))

    # Add style to the table
    style = TableStyle([
        # Black border around the table
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),

        # The top row where the labels are
        ('BACKGROUND', (0, 0), (6, 0), color_days),
        ('TEXTCOLOR', (0, 0), (6, 0), color_day_text),
        ('ALIGN', (0, 0), (6, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (6, 0), 'Georgia-Bold'),
        ('FONTSIZE', (0, 0), (6, 0), 12),
        ('BOTTOMPADDING', (0, 0), (6, 0), 7),
        ('TOPPADDING', (0, 0), (6, 0), 7),
        ('LEFTPADDING', (0, 0), (6, 0), 7),
        ('RIGHTPADDING', (0, 0), (6, 0), 7),

        # Grid styling around the table
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),

        # The rest of the rows
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 1), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 1), (-1, -1), 'Georgia'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('LEFTPADDING', (0, 1), (-1, -1), 2),

        # Colors for the blocks
        # FIRST ROW
        ('BACKGROUND', (0, 1), (0, 1), color_blocks[0]),
        ('BACKGROUND', (1, 1), (1, 1), color_blocks[5]),
        ('BACKGROUND', (2, 1), (2, 1), color_blocks[3]),
        ('BACKGROUND', (3, 1), (3, 1), color_blocks[1]),
        ('BACKGROUND', (4, 1), (4, 1), color_blocks[6]),
        ('BACKGROUND', (5, 1), (5, 1), color_blocks[4]),
        ('BACKGROUND', (6, 1), (6, 1), color_blocks[2]),

        # SECOND ROW
        ('BACKGROUND', (0, 2), (0, 2), color_blocks[1]),
        ('BACKGROUND', (1, 2), (1, 2), color_blocks[6]),
        ('BACKGROUND', (2, 2), (2, 2), color_blocks[4]),
        ('BACKGROUND', (3, 2), (3, 2), color_blocks[2]),
        ('BACKGROUND', (4, 2), (4, 2), color_blocks[0]),
        ('BACKGROUND', (5, 2), (5, 2), color_blocks[5]),
        ('BACKGROUND', (6, 2), (6, 2), color_blocks[3]),

        # THIRD ROW
        ('BACKGROUND', (0, 3), (0, 3), color_blocks[2]),
        ('BACKGROUND', (1, 3), (1, 3), color_blocks[0]),
        ('BACKGROUND', (2, 3), (2, 3), color_blocks[5]),
        ('BACKGROUND', (3, 3), (3, 3), color_blocks[3]),
        ('BACKGROUND', (4, 3), (4, 3), color_blocks[1]),
        ('BACKGROUND', (5, 3), (5, 3), color_blocks[6]),
        ('BACKGROUND', (6, 3), (6, 3), color_blocks[4]),

        # FOURTH ROW
        ('BACKGROUND', (0, 4), (0, 4), color_blocks[3]),
        ('BACKGROUND', (1, 4), (1, 4), color_blocks[1]),
        ('BACKGROUND', (2, 4), (2, 4), color_blocks[6]),
        ('BACKGROUND', (3, 4), (3, 4), color_blocks[4]),
        ('BACKGROUND', (4, 4), (4, 4), color_blocks[2]),
        ('BACKGROUND', (5, 4), (5, 4), color_blocks[0]),
        ('BACKGROUND', (6, 4), (6, 4), color_blocks[5]),

        # FIFTH ROW
        ('BACKGROUND', (0, 5), (0, 5), color_blocks[4]),
        ('BACKGROUND', (1, 5), (1, 5), color_blocks[2]),
        ('BACKGROUND', (2, 5), (2, 5), color_blocks[0]),
        ('BACKGROUND', (3, 5), (3, 5), color_blocks[5]),
        ('BACKGROUND', (4, 5), (4, 5), color_blocks[3]),
        ('BACKGROUND', (5, 5), (5, 5), color_blocks[1]),
        ('BACKGROUND', (6, 5), (6, 5), color_blocks[6]),
    ])

    table.setStyle(style)

    # Add data to the pdf
    elements = []
    elements.append(table)

    pdf.build(elements)