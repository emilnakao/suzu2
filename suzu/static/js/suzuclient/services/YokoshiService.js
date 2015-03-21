/**
 *
 * Copyright (c) 2013 The Suzu Team
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE
 *
 */
suzuClientApp.factory('yokoshiService', ['$http', function ($http) {
    return {
        findByName: function (searchToken, clbk) {
            var hans = [];

            $http.get('/api/v1/yokoshi/?format=json&complete_name__iregex=' + searchToken.replace(' ', '.*')).success(function (data) {
                clbk(data.objects);

            });

        },

        /**
         * Envia uma solicitação para salvar um yokoshi no servidor
         * @param yokoshiObj um objeto que representa um yokoshi
         *
         */
        saveYokoshi: function (yokoshiObj, successClbk) {
            var data = JSON.stringify(yokoshiObj);

            $.ajax({
                url: '/api/v1/yokoshi/',
                type: 'POST',
                contentType: 'application/json',
                data: data,
                dataType: 'json',
                processData: false

            }).success(function(successClbck){
                var clbk = successClbk;
                    return function(data) {
                        $.pnotify({
                            title: 'Parabéns!!',
                            text: _.template('<%=name%> cadastrado com sucesso!')({name: yokoshiObj.complete_name}),
                            type: 'success',
                            styling: 'bootstrap'
                        });
                        clbk(data);
                    }
                }(successClbk)
             ).fail(function () {
                    $.pnotify({
                        title: 'Oh nãoo!',
                        text: 'Nos desculpe, não foi possível completar a solicitação.',
                        type: 'error',
                        styling: 'bootstrap'
                    });
                });
        }

    };
}]);
