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
suzuClientApp.controller('YokoshiHistoryReportController', function ($scope, $http, $cookieStore, notificationService, yokoshiService,eventService) {

    /**
     * Texto de busca digitado pelo usuário no modal de seleção de yokoshi
     * @type {string}
     */
    $scope.searchText = '';

    $scope.generateReport = function () {
        $http.get(_.template('/attendancebook/yokoshi_history/?yokoshi=<%=yokoshiId%>&start=<%=start%>&end=<%=end%>')({yokoshiId: $scope.yokoshi.id, start: $scope.start, end: $scope.end})).success(function (data) {
            $scope.data = data;
            notificationService.success("Relatório gerado!", "Histórico de presenças de " + $scope.yokoshi.complete_name);
            $scope.itemsPerPage = data.length;
            $scope.total = data.length;
            $scope.table_headers = _.keys(data[0]);
            $scope.items = data;
            $scope.currentEvent = $cookieStore.get('event');

        });


    };

    /**
     *
     */
    $scope.search = function () {
        eventService.findYokoshiForCheckin($scope.searchText, function (data) {
            $scope.yokoshis = data;
        });
    };

    /**
     * Marca um yokoshi como selecionado.
     * @param yokoshi um objeto yokoshi que será selecionado
     */
    $scope.selectYokoshi = function(yokoshi){
        $scope.yokoshi = yokoshi;
    }


});