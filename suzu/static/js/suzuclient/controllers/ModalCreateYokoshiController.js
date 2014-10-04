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
suzuClientApp.controller('ModalCreateYokoshiController', function ($scope, $http, $cookieStore, $modalInstance, yokoshiService, newYokoshiName, callbackFunction) {
    $scope.checkInPhase = "confirmRegistration";

    $scope.yokoshi = {
        complete_name: newYokoshiName
    };

    $scope.isConfirmRegistration = function(){
        return $scope.checkInPhase == "confirmRegistration";
    };

    $scope.isConfirmIsGuest = function(){
        return $scope.checkInPhase == "confirmIsGuest";
    };

    $scope.isConfirmIsFirstTime = function(){
        return $scope.checkInPhase == "confirmIsFirstTime";
    };

    /**
     * Passa à pergunta seguinte
     */
    $scope.proceedRegistration = function(){
        $scope.checkInPhase = "confirmIsGuest";
    }

    $scope.cancelRegistration = function(){
        $modalInstance.close(true);
    }

    $scope.setAsGuest = function(){
        $scope.checkInPhase = "confirmIsFirstTime";
        $scope.yokoshi.is_mikumite = true;
    }

    $scope.setAsNotGuest = function(){
        $scope.checkInPhase = "confirmIsFirstTime";
        $scope.yokoshi.is_mikumite = false;
        $scope.yokoshi.firsttime = false;
        yokoshiService.saveYokoshi($scope.yokoshi, callbackFunction);
        $modalInstance.close(true);
    }

    $scope.setAsFirstTime = function(){
        $scope.yokoshi.firsttime = true;
        yokoshiService.saveYokoshi($scope.yokoshi, callbackFunction);
        $modalInstance.close(true);
    }

    $scope.setAsNotFirstTime = function(){
        $scope.yokoshi.firsttime = false;
        yokoshiService.saveYokoshi($scope.yokoshi, callbackFunction);
        $modalInstance.close(true);
    }
});