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

suzuClientApp.controller('SidebarController', function($scope, $rootScope, $http, $cookieStore, eventService){

    $scope.presences = [];
    $scope.kumiteCount = 0;
    $scope.mikumiteCount = 0;
    $scope.mtaiCount = 0;
    $scope.firstTimeCount = 0;
    $scope.loading = false;

    // inicializacao
    if($cookieStore.get('event') != undefined){
        $scope.currentEvent = $cookieStore.get('event');
    }

    $scope.$on('eventSelected', function(eventMsg, event){
        $scope.currentEvent = event;
        $scope.refreshPresences();
    });

    $rootScope.$on('refreshCounters', function(eventMsg, event){
        $scope.refreshPresences();
    });

    $scope.refreshPresences = function(){
        if($scope.currentEvent != undefined){
            $scope.loading = true;
            $http.get('api/v1/presence/?format=json&event__id=' + $scope.currentEvent.id).success(function(data){
                $scope.presences = data.objects;

                var kumite = 0, mikumite = 0, mtai = 0, ftime = 0;

                $.each($scope.presences, function(idx, elem){
                    if(elem.is_first_time == true){
                        ftime++;
                    }
                    if(elem.is_mtai == true){
                        mtai++;
                    }
                    if(elem.is_mikumite == true){
                        mikumite++;
                    }else{
                        kumite++;
                    }

                    $scope.kumiteCount = kumite;
                    $scope.mikumiteCount = mikumite;
                    $scope.mtaiCount = mtai;
                    $scope.firstTimeCount = ftime;
                });
            }).finally(function(){
                $scope.loading = false;
            });
        }


    };

    $scope.refreshPresences();

});