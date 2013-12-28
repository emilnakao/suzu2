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
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE
 *
 */

/**
 * Angular JS controller for the current_event widget (check_in/widgets/current_event.html).
 *
 * @param $scope injected by angular js factory (default service). The widget's scope.
 * @param $http injected by angular js factory (default service). For ajax requests.
 * @constructor
 */
function CurrentEventWidgetController($scope, $http){

    $scope.refreshPresences = function(event_id){
        $http.get('/api/v1/presence/?event='+event_id+'&format=json').success(function(data){

            $scope.presences = data.objects;
            $scope.number_of_presences = data.meta.total_count;
            $scope.$apply();

        });
    };
}

/**
 * Angular JS controller for the event selection modal (check_in/widgets/event_selection_modal.html).
 *
 * @param $scope injected by angular js factory (default service). The modal's scope.
 * @param $http injected by angular js factory (default service). For ajax requests.
 * @constructor
 */
function EventSelectionModalController($scope, $http){
    /**
     * Fetches available events from the server
     */
    $scope.fetchEvents = function(){
        $http.get('/api/v1/event/?format=json').success(function(data){
            $scope.events = data.objects;
        });
    };

    /**
     *
     * @param event_id the selected event id
     */
    $scope.defineEventAsCurrent = function(event_id){
        $http.get('/event/define_as_current/' + event_id).success(function(data){
            $('#event_selection_modal .close')[0].click()
            window.location.reload();
        });
    };
}

/**
 *
 *
 * @param $scope
 * @param $http
 * @constructor
 */
function PresenceSearchController($scope, $http){
    $scope.upRgx = new RegExp('^[A-Z]+$');

    $scope.upperSearchToken = '.*[ ]';

    $scope.doSearch = function (key) {
        if (($scope.searchTerm.length > 0)) {
            var eventId = $('.event_id')[0].value;
            var usedSearchTerm = $scope.searchTerm;
            var nameQueryFilter = '&complete_name__iregex=';
            if($scope.upRgx.test($scope.searchTerm)){
                // TODO: melhorar essa regex
                var uppercaseSearchTerm = $scope.searchTerm.replace(/(?=[A-Z])([A-Z]?)/g, $scope.upperSearchToken + "$1");
                usedSearchTerm = uppercaseSearchTerm.substring($scope.upperSearchToken.length) + '.*';
                nameQueryFilter = '&complete_name__regex='
            }else{
                // TODO: refatorar isso daqui; solucao paleativa!!
                usedSearchTerm = usedSearchTerm.replace(' ', '.*');
                usedSearchTerm = usedSearchTerm.replace('e', '[eéê]');
                usedSearchTerm = usedSearchTerm.replace('a', '[aãáä]');
                usedSearchTerm = usedSearchTerm.replace('i', '[ií]');
                usedSearchTerm = usedSearchTerm.replace('u', '[uúü]');
                usedSearchTerm = usedSearchTerm.replace('o', '[oôö]');
            }

            $http.get('/api/v1/presence_count/?format=json&event_id='+eventId+ nameQueryFilter + usedSearchTerm).success(function (data) {
                $scope.searchResult = data;
                $scope.users = $scope.searchResult.objects;
            });
        }
        else if (($scope.searchTerm.length == 0)){
            $scope.searchResult = {};
            $scope.users = {};
        }
    };

    $scope.shouldShowConfirmPresenceBtn = function(presence_count){
        if(presence_count > 0){
            return true;
        }

        return false;
    };

    $scope.confirmPresence = function(user_id){
        $http.get('/confirm_presence/?person=' + user_id).success(function(data){
            $scope.doSearch(null);

        });
    }

    $scope.cancelPresence = function(user_id){
        $http.get('/cancel_presence/?person=' + user_id).success(function(data){
            $scope.doSearch(null);

        });
    }
}