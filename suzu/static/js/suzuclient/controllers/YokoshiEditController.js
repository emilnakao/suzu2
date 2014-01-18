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
suzuClientApp.controller('YokoshiEditController', function ($scope, $http, $cookieStore, hanService, yokoshiService, focusService, eventService, notificationService) {

    $scope.isEventSelected = $cookieStore.get('event') != undefined;

    $scope.resetYokoshiStatus = function () {
        $scope.confirmPresence = $scope.isEventSelected;

        $scope.kumiteStatus = 'kumite';

        $scope.isMtai = false;

        $scope.mikumiteFirstTime = false;
    };

    /** Por padrão, cadastramos um kumite */
    $scope.resetYokoshiStatus();
    focusService.focus('focusCompleteName');


    hanService.findAll(function (data) {
        $scope.hans = data
    });

    $scope.save = function () {
        var formYokoshi = $scope.createYokoshiObject();

        var clbk = function (yokoshi) {
        };

        if ($scope.confirmPresence === true) {
            clbk = function (yokoshi) {
                yokoshi.firsttime = formYokoshi.firsttime;
                eventService.confirmPresence(yokoshi, function (yokoshi) {
                    notificationService.success('Presença confirmada!', yokoshi.complete_name);
                })
            };
        }

        yokoshiService.saveYokoshi(formYokoshi, clbk);
        $scope.clear();
    };


    $scope.createYokoshiObject = function () {
        var yokoshi = {};

        yokoshi.complete_name = $scope.completeName;
        yokoshi.han = _.template('/api/v1/han_read_only/<%=hanId%>/')({hanId: $scope.hanId});
        yokoshi.email = $scope.email;


        if ($scope.kumiteStatus == 'kumite') {
            yokoshi.is_mikumite = false;

            if ($scope.isMtai == 'true') {
                yokoshi.is_mtai = true;
            }
        } else {
            yokoshi.is_mikumite = true;

            if ($scope.mikumiteFirstTime == 'true') {
                yokoshi.firsttime = true;
            }
        }

        return yokoshi;
    };

    $scope.clear = function () {
        $scope.completeName = '';
        $scope.email = '';
        $scope.resetYokoshiStatus();
        focusService.focus('focusCompleteName');
    };

    $scope.shouldConfirmPresence = function () {
        $scope.confirmPresence = true;
    }

    $scope.shouldNotConfirmPresence = function () {
        $scope.confirmPresence = false;
    }

})
