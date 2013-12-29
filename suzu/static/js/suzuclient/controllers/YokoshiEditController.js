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
suzuClientApp.controller('YokoshiEditController', function ($scope, $http, hanService) {

    hanService.findAll(function (data) {
        $scope.hans = data
    });

    $scope.save = function () {
        var data = JSON.stringify({
            "complete_name": $scope.completeName,
            "is_mikumite": $scope.isMikumite,
            "is_mtai": $scope.isMtai,
            "is_ossuewanin": $scope.isOssuewanin,
            "han":'/api/v1/han_read_only/' + $scope.hanId + '/'
        });

        $.ajax({
            url: 'http://localhost:8000/api/v1/yokoshi/',
            type: 'POST',
            contentType: 'application/json',
            data: data,
            dataType: 'json',
            processData: false

        }).success(function(){
                $.pnotify({
                    title: 'Parabéns!!',
                    text: 'Yokoshi cadastrado com sucesso!',
                    type: 'success',
                    styling: 'bootstrap'
                });
            }).fail(function(){
                $.pnotify({
                    title: 'Oh nãoo!',
                    text: 'Nos desculpe, não foi possível completar a solicitação.',
                    type: 'error',
                    styling: 'bootstrap'
                });
            });

    }

    $scope.clear = function () {
        alert('clear');
    }
})
