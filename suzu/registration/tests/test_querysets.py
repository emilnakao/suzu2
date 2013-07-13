"""
Copyright (c) 2013 The Suzu Team

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
from django.test import TestCase

from model_mommy.recipe import Recipe, seq
from ..models import Yokoshi


class YokoshiQuerySetTest(TestCase):
    def setUp(self):
        self.advanced_kumite_recipe = Recipe(Yokoshi, is_mikumite=False, complete_name=seq('Kumite Sup '),
                                             omitama_level=Yokoshi.OMITAMA_LEVEL.advanced)
        self.intermediate_kumite_recipe = Recipe(Yokoshi, is_mikumite=False, complete_name=seq('Kumite Int '),
                                                 omitama_level=Yokoshi.OMITAMA_LEVEL.intermediate)
        self.basic_kumite_recipe = Recipe(Yokoshi, is_mikumite=False, complete_name=seq('Kumite Bas '),
                                          omitama_level=Yokoshi.OMITAMA_LEVEL.basic)
        self.mikumite_recipe = Recipe(Yokoshi, is_mikumite=True, complete_name=seq('Kumite Bas '),
                                      omitama_level=Yokoshi.OMITAMA_LEVEL.none)

        self.advanced_kumite_recipe.make(_quantity=5)
        self.intermediate_kumite_recipe.make(_quantity=6)
        self.basic_kumite_recipe.make(_quantity=7)
        self.mikumite_recipe.make(_quantity=4)

    def test_filter_mikumite(self):
        list = Yokoshi.objects.all().mikumite()
        self.assertEquals(4, list.count())

    def test_filter_advanced(self):
        list = Yokoshi.objects.all().advanced()
        self.assertEquals(5, list.count())

    def test_nofilter(self):
        list = Yokoshi.objects.all()
        self.assertEquals(22, list.count())

    def test_filter_intermediate(self):
        list = Yokoshi.objects.all().intermediate()
        self.assertEquals(6, list.count())

    def test_filter_basic(self):
        list = Yokoshi.objects.all().basic()
        self.assertEquals(7, list.count())

    def test_filter_kumite(self):
        list = Yokoshi.objects.all().kumite()
        self.assertEquals(18, list.count())