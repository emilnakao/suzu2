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
suzuClientApp.controller('ReportController', function ($scope, $http, $cookieStore, notificationService, reportService) {
    $http.get('/registration/presence_by_event/?event=' + $cookieStore.get('event').id).success(function (data) {
        $scope.data = data;
        notificationService.success("Relatório gerado!", "Presenças por evento");
        $scope.itemsPerPage = data.length;
        $scope.total = data.length;
        $scope.table_headers = _.keys(data[0]);
        $scope.items = data;

        $scope.sort = {
            column: 'nome',
            descending: false
        };

        $scope.sort_by = function(column){
            var sort = $scope.sort;

            if(sort.column == column){
                sort.descending = !sort.descending;
            }else{
                sort.column = column;
                sort.descending = false;
            }
        };

        $scope.chartObj = {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Presença de Yokoshis'
            },
            subtitle: {
                text: $cookieStore.get('event').name
            },
            xAxis: {
                categories: [
                    'evento'
                ],
                labels: {
                    rotation: -45,
                    align: 'right',
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }}
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Quantidade de Pessoas'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>{point.y} pessoas</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: []
        }

        var allByHan = _.countBy(data, function(presence){
           return presence.han;
        });

        var allByStatus = _.countBy(data, function(presence){
           if(presence.mikumite == true){
               return 'mikumite';
           }

            return 'kumite';
        });

        $scope.kumiteTotal = allByStatus.kumite;
        $scope.mikumiteTotal = allByStatus.mikumite;

        // recuperando nomes dos hans
        var kumiteByHan = _.countBy(data, function(presence){
            if(presence.mikumite === false){
                return presence.han;
            }

            return 'omitme';

        });

        var mikumiteByHan = _.countBy(data, function(presence){
            if(presence.mikumite === true){
                return presence.han;
            }

            return 'omitme';
        });

        mikumiteByHan = _.omit(mikumiteByHan, 'omitme');
        kumiteByHan = _.omit(kumiteByHan, 'omitme');

        // refactoring
        $scope.chartObj.xAxis.categories = _.keys(allByHan);
        $scope.chartObj.series = [{data:_.values(kumiteByHan), color:'#07C', name:'Kumite',dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    x: 4,
                    y: 1,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif',
                        textShadow: '0 0 3px black'
                    }
                }},
        {data:_.values(mikumiteByHan), name:'Mi-Kumite', color: '#0C7', dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    x: 4,
                    y: 1,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif',
                        textShadow: '0 0 3px black'
                    }
                }}];

        $('#chart').highcharts($scope.chartObj);
    });
});