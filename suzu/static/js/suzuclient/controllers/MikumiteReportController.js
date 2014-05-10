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
suzuClientApp.controller('MikumiteReportController', function ($scope, $http, $cookieStore, notificationService) {


    $scope.generateReport = function () {
        $http.get(_.template('/registration/mikumite_report/?start=<%=start%>&end=<%=end%>')({start: $scope.start, end: $scope.end})).success(function (data) {
            $scope.data = data;
            notificationService.success("Relatório gerado!", "Presenças de Mikumite");
            $scope.itemsPerPage = data.length;
            $scope.total = data.length;
            $scope.table_headers = _.keys(data[0]);
            $scope.items = data;
            $scope.currentEvent = $cookieStore.get('event');

        });
    };

});