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
suzuClientApp.controller('InformYokoshiUpdateController', function ($scope, $http, $cookieStore, hanService, yokoshiService, focusService, notificationService) {

    $scope.yokoshi = {};

    $scope.selectedYokoshis = [];

    $scope.refreshYokoshi = function (name) {

        return $http.get(
                '/api/v1/yokoshi/?format=json&complete_name__iregex=' + name
        ).then(function (response) {
                $scope.yokoshis = response.data.objects;
            });
    };

    $scope.addYokoshi = function(item, select){
        $scope.selectedYokoshis.push(item);
        select.focus = true;
    };

    $scope.removeYokoshi = function(yokoshi){
        var index = $scope.selectedYokoshis.indexOf(yokoshi);
        if(index > -1){
            $scope.selectedYokoshis.splice(index, 1);
        }
    };

    $scope.confirmUpdates = function(){
        if($scope.selectedYokoshis.length > 0){
            // mandar para o servidor um post
            var ids = [];

            $($scope.selectedYokoshis).each(function(idx, elem){
               ids.push(elem.id);
            });

            $http.post('/registration/inform_yokoshi_update/',
                {
                    selectedYokoshis : angular.toJson(ids)
                }).success(function(data){
               notificationService.success('Atualização registrada!');
               $scope.selectedYokoshis = [];
               $scope.yokoshi = {};
            });
        }
    }

});