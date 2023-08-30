from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ReportLab pdfs take in data as a list of lists, each list is a row
# This function creates the data for the pdf
def fix_data(data_unedited: dict()):
    a = data_unedited['A']
    b = data_unedited['B']
    c = data_unedited['C']
    d = data_unedited['D']
    e = data_unedited['E']
    f = data_unedited['F']
    g = data_unedited['G']

    time1 = '8:20 - 9:25'
    time2 = '9:31 - 10:31'
    time3 = '10:37 - 12:22'
    time4 = '12:28 - 1:28'
    time5 = '1:34 - 2:34'

    data = [['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
            [a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + time1, f[0] + '\n' + f[1] + '\n' + f[2] + '\n' + time1, d[0] + '\n' + d[1] + '\n' + d[2] + '\n' + time1, b[0] + '\n' + b[1] + '\n' + b[2] + '\n' + time1, g[0] + '\n' + g[1] + '\n' + g[2] + '\n' + time1, e[0] + '\n' + e[1] + '\n' + e[2] + '\n' + time1, c[0] + '\n' + c[1] + '\n' + c[2] + '\n' + time1],
            [b[0] + '\n' + b[1] + '\n' + b[2] + '\n' + time2, g[0] + '\n' + g[1] + '\n' + g[2] + '\n' + time2, e[0] + '\n' + e[1] + '\n' + e[2] + '\n' + time2, c[0] + '\n' + c[1] + '\n' + c[2] + '\n' + time2, a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + time2, f[0] + '\n' + f[1] + '\n' + f[2] + '\n' + time2, d[0] + '\n' + d[1] + '\n' + d[2] + '\n' + time2],
            [c[0] + '\n' + c[1] + '\n' + c[2] + '\n' + time3, a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + time3, f[0] + '\n' + f[1] + '\n' + f[2] + '\n' + time3, d[0] + '\n' + d[1] + '\n' + d[2] + '\n' + time3, b[0] + '\n' + b[1] + '\n' + b[2] + '\n' + time3, g[0] + '\n' + g[1] + '\n' + g[2] + '\n' + time3, e[0] + '\n' + e[1] + '\n' + e[2] + '\n' + time3],
            [d[0] + '\n' + d[1] + '\n' + d[2] + '\n' + time4, b[0] + '\n' + b[1] + '\n' + b[2] + '\n' + time4, g[0] + '\n' + g[1] + '\n' + g[2] + '\n' + time4, e[0] + '\n' + e[1] + '\n' + e[2] + '\n' + time4, c[0] + '\n' + c[1] + '\n' + c[2] + '\n' + time4, a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + time4, f[0] + '\n' + f[1] + '\n' + f[2] + '\n' + time4],
            [e[0] + '\n' + e[1] + '\n' + e[2] + '\n' + time5, c[0] + '\n' + c[1] + '\n' + c[2] + '\n' + time5, a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + time5, f[0] + '\n' + f[1] + '\n' + f[2] + '\n' + time5, d[0] + '\n' + d[1] + '\n' + d[2] + '\n' + time5, b[0] + '\n' + b[1] + '\n' + b[2] + '\n' + time5, g[0] + '\n' + g[1] + '\n' + g[2] + '\n' + time5]]

    return data

def convert_to_paragraphs(data: list()):
    for row in data:
        if row[0] == 'Day 1':
            continue

        for i in range(len(row)):
            row[i] = create_paragraph(row[i])

    return data

def create_paragraph(text):
    style = getSampleStyleSheet()['Normal']
    return Paragraph(text.replace('\n', '<br />'), style=style)
