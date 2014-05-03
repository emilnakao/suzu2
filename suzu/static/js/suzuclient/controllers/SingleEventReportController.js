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
suzuClientApp.controller('SingleEventReportController', function ($scope, $http, $cookieStore, notificationService, reportService) {
    $http.get('/registration/presence_by_event/?event=' + $cookieStore.get('event').id).success(function (data) {
        $scope.data = data;
        notificationService.success("Relatório gerado!", "Presenças por evento");
        $scope.itemsPerPage = data.length;
        $scope.total = data.length;
        $scope.table_headers = _.keys(data[0]);
        $scope.items = data;
        $scope.currentEvent = $cookieStore.get('event');
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
                type: 'column',
                backgroundColor: '#F2F8F5'
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
           if(presence.mikumite == true && presence.firsttime == false){
               return 'mikumite';
           }else if(presence.mikumite == true && presence.firsttime == true){
               return 'firsttime';
           }

            return 'kumite';
        });

        $scope.kumiteTotal = allByStatus.kumite;
        $scope.mikumiteTotal = allByStatus.mikumite;
        $scope.firsttimeTotal = allByStatus.firsttime;

        // recuperando nomes dos hans
        var kumiteByHan = _.countBy(data, function(presence){
            if(presence.mikumite === false){
                return presence.han;
            }

            return 'omitme';

        });

        var mikumiteByHan = _.countBy(data, function(presence){
            if(presence.mikumite === true && presence.firsttime === false){
                return presence.han;
            }

            return 'omitme';
        });

        var firsttimeByHan = _.countBy(data, function(presence){
           if(presence.mikumite === true && presence.firsttime === true){
               return presence.han;
           }

            return 'omitme';
        });

        // omitme é um artifício para informar que uma presença não pertence a uma categoria, e deve ser removida depois
        mikumiteByHan = _.omit(mikumiteByHan, 'omitme');
        kumiteByHan = _.omit(kumiteByHan, 'omitme');
        firsttimeByHan = _.omit(firsttimeByHan, 'omitme');

        // tratando as séries: todas as séries precisam ter todas as categorias (hans), msm que a qtde. seja 0
        var categories =  _.keys(allByHan);

        var zeroSeries = {};

        _.each(categories, function(elem){
            zeroSeries[elem] = 0;
        });


        mikumiteByHan = _.defaults(mikumiteByHan, zeroSeries);
        kumiteByHan = _.defaults(kumiteByHan, zeroSeries);
        firsttimeByHan = _.defaults(firsttimeByHan, zeroSeries);

        // transformando os objetos em mapas e dps listas, para manter a ordem:
        mikumiteByHan = _.pairs(mikumiteByHan);
        kumiteByHan = _.pairs(kumiteByHan);
        firsttimeByHan = _.pairs(firsttimeByHan);

        mikumiteByHan = _.sortBy(mikumiteByHan, function(arr){return arr[0];});
        kumiteByHan = _.sortBy(kumiteByHan, function(arr){return arr[0];});
        firsttimeByHan = _.sortBy(firsttimeByHan, function(arr){return arr[0];});

        var mikumiteSeries = [];
        _.each(mikumiteByHan, function(keyValueArray){
            mikumiteSeries.push(keyValueArray[1]);
        });
        var kumiteSeries = [];
        _.each(kumiteByHan, function(keyValueArray){
            kumiteSeries.push(keyValueArray[1]);
        });
        var firsttimeSeries = [];
        _.each(firsttimeByHan, function(keyValueArray){
            firsttimeSeries.push(keyValueArray[1]);
        });

        // refactoring
        $scope.chartObj.xAxis.categories = categories;
        $scope.chartObj.series = [{data:kumiteSeries, color:'#07C', name:'Kumite',dataLabels: {
                    enabled: true,

                    color: '#222222',
                    align: 'center',
                    x: 0,
                    y: 1,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'

                    }
                }},
        {data:mikumiteSeries, name:'Mi-Kumite', color: '#0C7', dataLabels: {
                    enabled: true,
                    color: '#222222',
                    align: 'center',
                    x: 0,
                    y: 1,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif',
                    }
                }},
        {data:firsttimeSeries, name:'Primeira Vez', color: '#C07', dataLabels: {
                    enabled: true,
                    color: '#222222',
                    align: 'center',
                    x: 0,
                    y: 1,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif',
                    }
                }}];

        $('#chart').highcharts($scope.chartObj);
    });
});