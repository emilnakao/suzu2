suzuClientApp.controller('ModalYokoshiEditController', function ($scope, $http, $cookieStore, $modalInstance, yokoshiService, selectedYokoshi, callbackFunction) {

    $scope.selectedYokoshi = selectedYokoshi;

    $scope.callback = callbackFunction;

    $scope.cancel = function(){
        $modalInstance.close(true);
    }

    $scope.submit = function(){
        if($scope.selectedYokoshi.is_mikumite == true){
            $scope.selectedYokoshi.is_mtai = false;
        }
        yokoshiService.saveYokoshi($scope.selectedYokoshi, $scope.callback);
        $modalInstance.close(true);
    }

});