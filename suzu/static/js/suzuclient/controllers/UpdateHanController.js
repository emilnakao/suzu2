/**
 *
 * Copyright (c) 2014 The Suzu Team
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
suzuClientApp.controller('UpdateHanController', function ($scope, $http, $cookieStore, hanService, yokoshiService, focusService, notificationService) {

    $scope.selectedHan = undefined;

    $scope.hans = [];

    $scope.selectedYokoshis = [];
    $scope.yokoshiList = [];

    $scope.loading = true;

    $scope.pageSize = 100;
    $scope.nextPageUrl = undefined;
    $scope.previousPageUrl = undefined;
    $scope.totalCount = undefined;
    $scope.currentPage = 1;
    $scope.numPages = 1;

    $scope.initHans = function () {

        return $http.get(
                '/api/v1/han_read_only/?format=json'
        ).then(function (response) {
                $scope.hans = response.data.objects;
            });
    };

    $scope.updateHan = function(yokoshi){
        yokoshi.loading = true;

        $http.post('/attendancebook/update_han/?yokoshi_id=' + yokoshi.id + '&han_id=' + yokoshi.han.id
            ).success(function(clbk){
                yokoshi.loading = false;
                yokoshi.done = true;

            })
    };

    $scope.searchYokoshi = function(page){
        $scope.loading = true;
        var offset = (page - 1) * $scope.pageSize;
        $http.get('/api/v1/yokoshi/?format=json&order_by=complete_name&limit=' + $scope.pageSize + '&offset=' +offset)
            .success(function(data){
                // inicializando metadados da busca
                $scope.nextPageUrl = data.meta.next;
                $scope.previousPageUrl = data.meta.previous;
                $scope.totalCount = data.meta.total_count;
                $scope.numPages = Math.ceil($scope.totalCount / $scope.pageSize);

                // para cada yokoshi, cria um atributo 'selected' dizendo se ele esta no han selecionado ou nao
                $scope.yokoshiList = data.objects;
                $scope.loading = false;

        });


    };

    $scope.pageChanged = function(page) {
        $scope.searchYokoshi(page);
    };

    $scope.initHans();
    $scope.searchYokoshi(1);

});