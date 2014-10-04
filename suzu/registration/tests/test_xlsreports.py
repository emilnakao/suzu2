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
import datetime
from django.test import TransactionTestCase
from model_mommy.recipe import Recipe
from registration.models import Yokoshi, EventType, Event, Presence
import registration.xlsreports as xls


class PresenceReportTest(TransactionTestCase):

    def setUp(self):
        # Populando o banco com Yokoshis
        self.joao_recipe_recipe = Recipe(Yokoshi, is_mikumite=False, complete_name='Joao')
        self.maria_recipe_recipe = Recipe(Yokoshi, is_mikumite=False, complete_name='Maria')
        self.pedro_recipe_recipe = Recipe(Yokoshi, is_mikumite=False, complete_name='Pedro')
        self.caio_recipe_recipe = Recipe(Yokoshi, is_mikumite=True, complete_name='Caio')

        self.joao = self.joao_recipe_recipe.make()
        self.maria = self.maria_recipe_recipe.make()
        self.pedro = self.pedro_recipe_recipe.make()
        self.caio = self.caio_recipe_recipe.make()

        # Criando tipo de evento e evento
        self.ceremony_type_recipe = Recipe(EventType, name="Monthly Ceremony")
        self.normal_day_type_recipe = Recipe(EventType, name="Normal Day")
        self.ceremony_type = self.ceremony_type_recipe.make()
        self.normal_day_type = self.normal_day_type_recipe.make()

        october_5 = datetime.datetime(2014, 10, 5)
        october_6 = datetime.datetime(2014, 10, 6)

        self.ceremony_event_recipe = Recipe(Event, event_type=self.ceremony_type, begin_date_time=october_5, id=1)
        self.normal_day_event_recipe = Recipe(Event, event_type=self.normal_day_type, begin_date_time=october_6, id=2)

        self.ceremony_event = self.ceremony_event_recipe.make()
        self.normal_day_event = self.normal_day_event_recipe.make()

        # Criando presencas

        self.presence1_recipe = Recipe(Presence, event=self.ceremony_event, begin_date_time=october_5, yokoshi=self.joao)
        self.presence2_recipe = Recipe(Presence, event=self.ceremony_event, begin_date_time=october_5, yokoshi=self.maria)
        self.presence3_recipe = Recipe(Presence, event=self.normal_day_event, begin_date_time=october_6, yokoshi=self.pedro)
        self.presence4_recipe = Recipe(Presence, event=self.normal_day_event, begin_date_time=october_6, yokoshi=self.caio)

        self.presence1_recipe.make()
        self.presence2_recipe.make()
        self.presence3_recipe.make()
        self.presence4_recipe.make()



    def test_day_report(self):
        """

        :return:
        """
        list = Yokoshi.objects.all()
        self.assertEquals(4, list.count())

        xls.single_event_report(1)