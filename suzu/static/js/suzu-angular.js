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

var module = angular.module("suzu", ['$strap.directives']);

/**
 * Definindo servico para comunicacao entre controllers
 */
module.factory('comm-bus', function () {

});

/**
 * HTML directive to capture key up events
 *
 * From: http://jsfiddle.net/bYUa3/2/
 */
module.directive('onKeyupFn', function () {
    return function (scope, elm, attrs) {
        //Evaluate the variable that was passed
        //In this case we're just passing a variable that points
        //to a function we'll call each keyup
        var keyupFn = scope.$eval(attrs.onKeyupFn);
        elm.bind('keyup', function (evt) {
            //$apply makes sure that angular knows
            //we're changing something
            scope.$apply(function () {
                keyupFn.call(scope, evt.which);
            });
        });
    };
});

function ReportController($scope, $http) {

    $scope.event_list = [];

    $scope.han_list = [];

    $scope.selected_event;

    $scope.selected_han;

    $scope.today = Date.today().toString('yyyy-MM-dd');

    $scope.last_month = (1).months().ago().toString('yyyy-MM-dd');

    $scope.end_date = $scope.today;

    $scope.start_date = $scope.last_month;

    $scope.inactive_end_date = $scope.today;

    $scope.inactive_start_date = $scope.last_month;

    $scope.initialize_event_list = function () {
        $http.get('/api/v1/event/?format=json').success(function (data) {
            $scope.event_list = data.objects;
            $.each($scope.event_list, function (index, event) {
                event.description = event.event_type.name + ' ' + event.begin_date_time;
            });

            $scope.selected_event = $scope.event_list[0];
//            $scope.$apply();
        });
    };

    $scope.initialize_han_list = function () {
        $http.get('/api/v1/han/?format=json').success(function (data) {
            $scope.han_list = data.objects;
            $scope.selected_han = $scope.han_list[0];
//            $scope.$apply();
        });
    };

    $scope.initialize_event_list();
    $scope.initialize_han_list();

//    $('#dp_presences_by_period_start').datepicker();
    //$('#dp_presences_by_period_end').datepicker();


}


/**
 *
 *
 * @param $scope
 * @param $http
 * @constructor
 */
function DesktopYokoshiSearchController($scope, $http) {
    $scope.doSearch = function (key) {
        if (($scope.searchTerm.length > 2)) {
            //  $http.get('/api/v1/yokoshi/?format=json&complete_name__iregex=' + $scope.searchTerm.replace(' ', '.*')).success(function (data) {
            var eventId = $('.event_id')[0].value;

            $http.get('/api/v1/yokoshi_presence/?format=json&event_id=' + eventId + '&complete_name__iregex=' + $scope.searchTerm.replace(' ', '.*')).success(function (data) {
                $scope.searchResult = data;
                $scope.users = $scope.searchResult.objects;
            });
        }
    };

    $scope.shouldShowConfirmPresenceBtn = function (presence_count) {
        if (presence_count > 0) {
            return true;
        }

        return false;
    };

    $scope.confirmPresence = function (user_id) {
        $http.get('/confirm_presence/?yokoshi=' + user_id).success(function (data) {
            $scope.doSearch(null);

        });
    }
}

/**
 * Controller for Event screen
 * @param $scope
 * @param $http
 * @constructor
 */
function EventController($scope, $http, $document) {
    /**
     * Initializing stopFetching variable
     */
    $scope.stopFetching = false;

    $scope.presences = [];

    $scope.eventId = $document.find('.event_id')[0].value;

    /**
     * This is called when the user clicks in Load More Data Button of Present Participants list
     */
    $scope.loadMorePresentParticipants = function () {
        if (($scope.searchUrl == null) && (!($scope.stopFetching == true))) {
            $scope.searchUrl = '/api/v1/presence/?event=' + $scope.eventId + '&format=json';
        }

        $http.get($scope.searchUrl).success(function (data) {
            var nextUrl = data.meta.next;
            if (nextUrl == null) {
                $scope.stopFetching = true;

            } else {
                $scope.searchUrl = nextUrl;
            }

            $scope.presences = data.objects;
        });
    };
}

/**
 * AngularJS Controller for the m_event_create screen
 * @param $scope
 * @param $document
 * @constructor
 */
function EventCreateController($scope, $document) {
//    $document.find('#additional_gohoshis_table .inline_gohoshi').formset();

}

/**
 * Controller for the notification bar. Captures broadcasted messages from other
 * controllers and displays in the top part of the screen.
 *
 * Every controller that wants to display a message should broadcast a message
 * according to the example:
 * $rootScope.$broadcast('notification', {message: 'The message to show in a h3 tag', details:'The message to show in a p tag below h3'});
 *
 * @param $scope
 * @constructor
 */
function NotificationController($scope, $rootScope, $document) {

    var messageContainer = $document.find('[ng-model="notification_message"]')[0];

//    if($scope.notification_message != undefined && $scope.notification_message != ''){
    if (messageContainer != undefined) {
        var message = messageContainer.innerHTML;
        if (message != '') {
            $document.find('.notification-bar').slideDown(500,function () {
            }).delay(5000).slideUp(500, function () {
                messageContainer.innerHTML = ''
//                $rootScope.notification_message = undefined;
//                $rootScope.notification_details = '';
            })
        }
    }

}