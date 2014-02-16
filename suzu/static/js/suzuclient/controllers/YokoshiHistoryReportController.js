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
suzuClientApp.controller('YokoshiHistoryReportController', function ($scope, $http, $cookieStore, notificationService, yokoshiService) {

    // inicialização
 // abortar typeahead; usar modal para seleção de yokoshi
   /* yokoshiService.findByName('', function (data) {
        $scope.everyone = [];
        _.each(data, function(yokoshi){
           $scope.everyone.push({value:yokoshi.id, tokens:[yokoshi.complete_name]});
        });
        $('#yokoshiTypeAheadInput').typeahead({
            name: 'yokoshis',
            local: $scope.everyone,
            limit: 20
        });
    });*/

    $scope.generateReport = function () {
        $http.get(_.template('/registration/yokoshi_history/?yokoshi=<%=yokoshiId%>&start=<%=start%>&end=<%=end%>')({yokoshiId: $scope.yokoshi.id, start: $scope.start, end: $scope.end})).success(function (data) {
            $scope.data = data;
            notificationService.success("Relatório gerado!", "Histórico de presenças de " + $scope.yokoshi.complete_name);
            $scope.itemsPerPage = data.length;
            $scope.total = data.length;
            $scope.table_headers = _.keys(data[0]);
            $scope.items = data;
            $scope.currentEvent = $cookieStore.get('event');

        });

    };


});