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
import unittest
from splinter import Browser

LOCALHOST_YOKOSHI_CREATE = 'http://localhost:8000/yokoshi/create'


class YokoshiRegistrationTest(unittest.TestCase):

    def setUp(self):
        # for chrome: http://www.gjdb.nl/?p=214
        self.browser = Browser()

    def tearDown(self):
        self.browser.quit()

    def test_can_register_information_with_minimal_information(self):
        # Receptionist opens yokoshi create url
        self.browser.visit(LOCALHOST_YOKOSHI_CREATE)

        # Has opened the right page

        # Receptionist fills complete name field
        self.browser.fill('yokoshi_name', 'John Galt')

        # Receptionist clicks in "Click" button
        self.browser.find_by_name('create').click()

        # A success message is displayed
        self.browser.is_text_present('Yokoshi "John Galt" criado com sucesso!')

if __name__ == '__main__':
    unittest.main()

