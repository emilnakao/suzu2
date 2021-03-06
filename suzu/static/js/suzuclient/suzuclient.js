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
'use strict';

var suzuClientApp = angular.module('suzuClientApp', ['ngCookies', 'ui.select', 'ngRoute', 'ngSanitize', 'ui.bootstrap']).config(['$routeProvider', function($routeProvider){
   $routeProvider.when('/registration', {templateUrl:'templates/suzuclient/registration/home.html', controller:'DummyController'});
   $routeProvider.when('/edit_yokoshi', {templateUrl:'templates/suzuclient/registration/edit_yokoshi.html', controller:'YokoshiEditController'});
   $routeProvider.when('/inform_yokoshi_update', {templateUrl:'templates/suzuclient/registration/inform_yokoshi_update.html', controller:'InformYokoshiUpdateController'});
   $routeProvider.when('/update_han', {templateUrl:'templates/suzuclient/registration/update_han.html', controller:'UpdateHanController'});
   $routeProvider.when('/checkin', {templateUrl:'templates/suzuclient/checkin/home.html', controller:'CheckInController'});
   $routeProvider.when('/reports', {templateUrl:'templates/suzuclient/reports/home.html', controller:'DummyController'});
   $routeProvider.when('/reports/singleevent', {templateUrl:'templates/suzuclient/reports/singleevent.html', controller:'SingleEventReportController'});
   $routeProvider.when('/reports/yokoshihistory', {templateUrl:'templates/suzuclient/reports/yokoshihistory.html', controller:'YokoshiHistoryReportController'});
   $routeProvider.when('/reports/mikumitereport', {templateUrl:'templates/suzuclient/reports/mikumitereport.html', controller:'MikumiteReportController'});
   $routeProvider.when('/reports/export', {templateUrl:'templates/suzuclient/reports/export.html', controller:'ExportReportController'});
   $routeProvider.otherwise({redirectTo: '/view1', templateUrl: 'templates/suzuclient/home.html'});
}
]);

/**
 * Configuração necessária para fazer POSTs. Inclui o token CSRF em toda request, para evitar erros 403 (unauthorized)
 */
suzuClientApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

/* Para testes: definindo fake backend */
//suzuClientApp.config(function($provide){
//   $provide.decorator('$httpBackend', angular.mock.e2e.$httpBackendDecorator);
//});

//suzuClientApp.run(function($httpBackend){
//   //$httpBackend.whenGET('template1.html').respond('content');
//   $httpBackend.whenGET().passThrough();
//   $httpBackend.whenJSONP().passThrough();
//});

/**
 * Filtros
 */

/**
 * Exemplo de uso: <div>{% ng msg | isempty: 'Msg vazia' %}</div>
 */
suzuClientApp.filter('isempty', function(){
    return function(input, replaceText){
        if(input) return input;
        return replaceText;
    }
});

/**
 * Funcionalidades globais
 */

Date.prototype.toDateInputValue = (function() {
    var local = new Date(this);
    local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
    return local.toJSON().slice(0,10);
});