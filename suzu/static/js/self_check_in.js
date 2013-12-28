/**
 *
 * Copyright (c) 2012 The Suzu Team
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

/**
 *
 *
 * @param $scope
 * @param $http
 * @constructor
 */
function SelfCheckInController($scope, $http) {
    $scope.searchTerm = '';

    $scope.typeaheadFn = function (query, callback) {
        var eventId = $('.event_id')[0].value;

        $http.get('/api/v1/presence_count/?format=json&event_id=' + eventId + '&complete_name__iregex=' + query.replace(' ', '.*')).success(function (data) {
            $scope.searchResult = data;
            $scope.users = $scope.searchResult.objects;
            $scope.names = [];
            $.each($scope.users, function(index, val){
                $scope.names.push(val.complete_name);
            });

            callback($scope.names);
        });
    };


    $scope.shouldShowConfirmPresenceBtn = function (presence_count) {
        if (presence_count > 0) {
            return true;
        }

        return false;
    };

    $scope.confirmPresence = function (user_id) {
        $http.get('/confirm_presence/?person=' + user_id).success(function (data) {
            $scope.doSearch(null);

        });
    }

    $scope.cancelPresence = function (user_id) {
        $http.get('/cancel_presence/?person=' + user_id).success(function (data) {
            $scope.doSearch(null);

        });
    }

    $scope.selectPerson = function () {

    }
}