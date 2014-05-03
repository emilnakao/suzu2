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
from django.core.exceptions import ValidationError

from .models import Country, State, Neighborhood, City, Address, Yokoshi, Regional, Han

__author__ = 'emilnakao'

from xlrd import open_workbook
from dateutil import parser

class XLSImporter():
    """
    Utility class for excel file imports. You need to run this by the command line
    """

    @classmethod
    def import_suzu2(cls, workbook_path):
        """
        para importacao_suzu2:

        python manage.py shell --settings=suzu.settings.dev
        from registration.xlsimport import XLSImporter
        XLSImporter.import_suzu2('importacao_suzu2.xls')
        """
        book = open_workbook(workbook_path)
        sheet = book.sheet_by_index(0)
        for row_index in range(sheet.nrows):
            XLSImporter.import_yokoshi(sheet=sheet, row=row_index, name_idx=6, han_idx=7, kumite_code_idx=1, email_idx=5)

    @classmethod
    def import_kumite_pinheiros_from_livia_xls(cls, workbook_path):
        book = open_workbook(workbook_path)
        sheet = book.sheet_by_index(0)
        for row_index in range(sheet.nrows):
            XLSImporter.import_yokoshi(sheet=sheet, row=row_index,name_idx=0, neighborhood_idx=1, city_idx=2, additional_info='Dados importados do excel - arquivo da Livia - Banco de Dados.')

    @classmethod
    def import_other_regionals_from_livia_xls(cls, workbook_path):
        book = open_workbook(workbook_path)
        sheet = book.sheet_by_index(1)
        for row_index in range(sheet.nrows):
            XLSImporter.import_yokoshi(sheet=sheet, row=row_index,name_idx=0, regional_idx=1, city_idx=2, additional_info='Dados importados do excel - arquivo da Livia - Outras Regionais.')

    @classmethod
    def import_guests_from_livia_xls(cls, workbook_path):
        book = open_workbook(workbook_path)
        sheet = book.sheet_by_index(2)
        for row_index in range(sheet.nrows):
            XLSImporter.import_yokoshi(sheet=sheet, row=row_index,name_idx=0, neighborhood_idx=1, city_idx=1, additional_info='Dados importados do excel - arquivo da Livia - Convidados.')

    @classmethod
    def import_new_yokoshis_from_livia_xls(cls, workbook_path):
        book = open_workbook(workbook_path)
        sheet = book.sheet_by_index(3)
        for row_index in range(sheet.nrows):
            XLSImporter.import_yokoshi(sheet=sheet, row=row_index,name_idx=0, neighborhood_idx=1, city_idx=2, additional_info='Dados importados do excel - arquivo da Livia - Nomes Novos.')

    @classmethod
    def put_surname_at_name_end(cls, name_beginning_surname):
        '''

        '''
        tokens = name_beginning_surname.partition(',')
        return tokens[2].strip() + ' ' + tokens[0].strip()

    @classmethod
    def import_new_yokoshis_from_ono_xls(cls, workbook_path):
        book = open_workbook(workbook_path)
        sheet = book.sheet_by_index(0)
        for row_index in range(sheet.nrows):
            XLSImporter.import_yokoshi(sheet=sheet, row=row_index, name_idx=0, kumite_code_idx=1, han_idx=2, name_treatment_function=cls.put_surname_at_name_end)

    @classmethod
    def import_yokoshi(cls, sheet, row, name_idx, regional_idx=-1, neighborhood_idx = -1, city_idx = -1, country_idx = -1, state_idx = -1, han_idx=-1, street_idx=-1, additional_info='', kumite_code_idx=-1, email_idx=-1, birthday_idx=-1, name_treatment_function = lambda x: x):

        # Country data initialization
        if country_idx < 0:
            country_name = 'Brasil'
        else:
            country_name = sheet.cell(row, country_idx).value

        country = Country.objects.get_or_create(name=country_name)[0]

        # State data initialization
        if state_idx < 0:
            state_name = u'S\u00e3o Paulo'
        else:
            state_name = sheet.cell(row, state_idx).value

        state = State.objects.get_or_create(name=state_name, country=country)[0]

        # City data initialization
        if city_idx < 0:
            city_name = u'S\u00e3o Paulo'
        else:
            city_name = sheet.cell(row, city_idx).value

        city = City.objects.get_or_create(name=city_name, state=state)[0]

        # Neighborhood data initialization
        if neighborhood_idx < 0:
            neighborhood_name = u'N\u00e3o Informado'
        else:
            neighborhood_name = sheet.cell(row, neighborhood_idx).value

        neighborhood = Neighborhood.objects.get_or_create(name=neighborhood_name, city=city)[0]

        # Regional data initialization
        if regional_idx < 0:
            regional_name = 'Pinheiros'
        else:
            regional_name = sheet.cell(row, regional_idx).value

        regional = Regional.objects.get_or_create(name=regional_name)[0]

        # Han data initialization
        if han_idx < 0:
            han_name = u'N\u00e3o Informado'
        else:
            han_name = sheet.cell(row, han_idx).value

        han = Han.objects.get_or_create(name=han_name, regional=regional)[0]

        # Kumite code initialization
        if kumite_code_idx < 0:
            kumite_code = ''
        else:
            kumite_code = sheet.cell(row, kumite_code_idx).value

        # email initialization
        if email_idx < 0:
            email = ''
        else:
            email = sheet.cell(row, email_idx).value

        # birthday initialization
        if birthday_idx < 0:
            birthday = None
        else:
            try:
                birthday = parser.parse(sheet.cell(row, birthday_idx).value)
                if birthday.year > 2006:
                    birthday.replace(year=birthday.year-100)
            except ValidationError:
                print 'Data invalida detectada. Ignorando.'

        yokoshi_name = sheet.cell(row, name_idx).value

        yokoshi_name = name_treatment_function(yokoshi_name)

        yokoshi = Yokoshi.objects.create(complete_name = yokoshi_name, han = han, additional_information=additional_info, seminary_number=kumite_code, email = email, birthday=birthday)

        # Street data initialization
        if street_idx < 0:
            street_name = u'N\u00e3o Informado'
        else:
            street_name = sheet.cell(row, street_idx).value

        #address = Address.objects.get_or_create(street_name=street_name, neighborhood = neighborhood, yokoshi=yokoshi)[0]

        print(yokoshi_name + ' foi importado!')



    @classmethod
    def create_pinheiros_yokoshi(cls, complete_name, neighborhood_name,city_name):
        state_name = 'Sao Paulo'
        regional_name = 'Pinheiros'
        country_name = 'Brasil'

        country_tuple = Country.objects.get_or_create(name = country_name)
        country = country_tuple[0]

        state_tuple = State.objects.get_or_create(name = state_name, country = country)
        state = state_tuple[0]

        if city_name:
            city_tuple = City.objects.get_or_create(name = city_name, state = state)
            city = city_tuple[0]

        regional_tuple = Regional.objects.get_or_create(name = regional_name)
        regional = regional_tuple[0]

        if city and neighborhood_name:
            neighborhood_tuple = Neighborhood.objects.get_or_create(name = neighborhood_name, city = city)
            neighborhood = neighborhood_tuple[0]

            address = Address.objects.create(neighborhood = neighborhood)

        Yokoshi.objects.create(complete_name = complete_name, regional = regional, address = address, additional_information='Dados importados via excel' )



