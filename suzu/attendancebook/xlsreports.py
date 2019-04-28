# coding=utf-8
"""
Copyright (c) 2014 The Suzu Team

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE
"""
from django.db import connection
import xlwt
from models import Event

styles = dict(
    bold = 'font: bold 1',
    italic = 'font: italic 1',
    # Wrap text in the cell
    wrap_bold = 'font: bold 1; align: wrap 1;',
    # White text on a blue background
    reversed = 'pattern: pattern solid, fore_color blue; font: color white;',
    # Light orange checkered background
    light_orange_bg = 'pattern: pattern fine_dots, fore_color white, back_color orange;',
    # Heavy borders
    bordered = 'border: top thin, right thin, bottom thin, left thin;',
    # 16 pt red text
    big_bold = 'font: height 320, bold 1;',
    big_italic = 'font: height 320, italic 1;',
)

big_bold = xlwt.easyxf('font: height 320, bold 1;')
big_italic = xlwt.easyxf('font: height 320, italic 1;')
bordered = xlwt.easyxf('border: top thin, right thin, bottom thin, left thin;')

def single_event_report(event_id):
    """
    Relatório de presenças de um único evento
    :param event_id:
    :return: um xlwt.Workbook;
    """
    cursor = connection.cursor()
    cursor.execute(
        'SELECT p.complete_name as nome, h.name as han, p.is_mikumite as mikumite, p.is_first_time as firsttime from attendancebook_presence p inner join attendancebook_yokoshi y on y.id = p.yokoshi_id inner join attendancebook_han h on h.id = p.han_id where p.event_id = %s order by h.name asc, p.complete_name asc',
        (event_id,))

    presences = cursor.fetchall()

    event = Event.objects.filter(pk=event_id).all()[0]

    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Presenças")

    sheet1.write(0,0,"Relatório de Presenças", big_bold)

    sheet1.write(1,0, event.event_type.name, big_italic)
    sheet1.write(2,0, event.begin_date_time.strftime("%d/%m/%Y"), big_italic)

    sheet1.write(4,0,"", bordered)
    sheet1.write(4,1, "Yokoshi", bordered)
    sheet1.write(4,2, "Núcleo", bordered)
    sheet1.write(4,3, "", bordered)

    line = 5
    yokoshi_count = 1

    for yokoshi, han, is_mikumite, is_first_time in presences:
        sheet1.write(line, 0, yokoshi_count, bordered)
        sheet1.write(line, 1, yokoshi, bordered)
        sheet1.write(line, 2, han, bordered)

        presence_status = 'Kumite'

        if(is_mikumite):
            if(is_first_time):
                presence_status = 'Primeira Vez'
            else:
                presence_status = 'Mi-Kumite'

        sheet1.write(line, 3, presence_status, bordered)
        yokoshi_count+=1
        line+=1

    # book.save("teste.xls")
    return book


def mikumite_report(start_date, end_date):
    """
    Relatório de MiKumite
    :param start_date:
    :param end_date:
    :return:
    """
    cursor = connection.cursor()
    cursor.execute((
        "select count(1) as resultnumber, "
        "y.complete_name as mikumite_name, "
        "coalesce(y.email, ' ') as email, "
        "coalesce(y.phone, ' ') as phone, "
        "coalesce(indication.complete_name, ' ') as indication_name, "
        "coalesce(indicationhan.name, ' ') as indication_han_name, "
        "count(p.id) as number_presences "
        "from attendancebook_presence p "
        "inner join attendancebook_yokoshi y on y.id = p.yokoshi_id "
        "left outer join attendancebook_yokoshi indication on indication.id = y.indication_id "
        "left outer join attendancebook_han indicationhan on indicationhan.id = indication.han_id "
        "where y.is_mikumite = 1 "
        "and p.begin_date_time >= %s "
        "and p.begin_date_time <= %s"
        "group by y.complete_name, y.email, y.phone, indication.complete_name, indicationhan.name "
        "order by y.complete_name asc"
        ""
    ), [start_date, end_date]
    )

    lines = cursor.fetchall()

    book = xlwt.Workbook(encoding="utf-8")

    sheet1 = book.add_sheet("Frequência de MiKumite")

    sheet1.write(0,0,"Relatório de Frequência de Mi-Kumite", big_bold)

    sheet1.write(1,0, start_date, big_italic)
    sheet1.write(2,0, end_date, big_italic)

    sheet1.write(4,0,"", bordered)
    sheet1.write(4,1, "Mi-Kumite", bordered)
    sheet1.write(4,2, "E-mail", bordered)
    sheet1.write(4,3, "Telefone", bordered)
    sheet1.write(4,4, "Encaminhado por", bordered)
    sheet1.write(4,5, "Han", bordered)
    sheet1.write(4,6, "Número de Presenças", bordered)

    line = 5

    for row_number, mikumite_name, email, phone, indication_name, indication_han_name, number_presences in lines:
        sheet1.write(line, 0, row_number, bordered)
        sheet1.write(line, 1, mikumite_name, bordered)
        sheet1.write(line, 2, email, bordered)
        sheet1.write(line, 3, phone, bordered)
        sheet1.write(line, 4, indication_name, bordered)
        sheet1.write(line, 5, indication_han_name, bordered)
        sheet1.write(line, 6, number_presences, bordered)

        line+=1

    return book