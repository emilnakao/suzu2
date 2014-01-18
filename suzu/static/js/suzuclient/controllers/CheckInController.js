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
suzuClientApp.controller('CheckInController', function ($scope, $http, $cookieStore, yokoshiService, eventService, notificationService, focusService) {

    focusService.focus('focusCheckinSearch');

    $scope.search = function ($event) {
        eventService.findYokoshiForCheckin($scope.searchText, function (data) {
            $scope.yokoshis = data;
        });
    };

    $scope.isYokoshiPresent = function (yokoshi) {
        return yokoshi.presence_count > 0;
    };

    /**
     * TODO: passar lógica para o eventService
     * @param yokoshi
     */
    $scope.togglePresence = function (yokoshi) {
        var eventId = $cookieStore.get('event').id;

        if ($scope.isYokoshiPresent(yokoshi)) {

            eventService.cancelPresence(yokoshi, function (data) {
                notificationService.success("Presença cancelada", yokoshi.complete_name);
                $scope.search(null);
                focusService.focus('focusCheckinSearch');

            });
        } else {
            eventService.confirmPresence(yokoshi, function (data) {
                notificationService.success("Presença confirmada", yokoshi.complete_name);
                $scope.search(null);
                focusService.focus('focusCheckinSearch');

            });
        }
    };

    $scope.getTogglePresenceBtnLabel = function(yokoshi){
        if($scope.isYokoshiPresent(yokoshi)){
            return "Cancelar Presença";
        }

        return "Confirmar Presença";
    };
})