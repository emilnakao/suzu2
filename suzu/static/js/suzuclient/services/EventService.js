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
suzuClientApp.factory('eventService', ['$http', '$cookieStore', 'notificationService', function ($http, $cookieStore, notificationService) {
    var currentEvent = {};

    return {
        currentEvent: currentEvent,

        /**
         * Procura por todos os tipos de evento disponiveis
         * @param clbk uma funcao que recebe um argumento; nele serah passado a lista de tipos de evento
         */
        findEventTypes: function (clbk) {
            $http.get('/api/v1/event_type/?format=json').success(function (data) {
                clbk(data.objects);
            });
        },

        /**
         * Procura por eventos que tenham tipo de evento com o id passado, e a data especificada. Se nenhum parâmetro
         * for especificado, retorna todos os eventos disponíveis (qtde. limitada pela paginação).
         *
         * @param clbk uma função que recebe um argumento; nele será passada a lista de eventos encontrados
         * @param eventTypeId opcional; o id do tipo de evento
         * @param date opcional; a data do evento (yyyy-MM-dd)
         */
        findEvent: function (clbk, eventTypeId, date) {
            var searchUrl = '/api/v1/event/?format=json';

            var parsedDate = moment(date);

            if (eventTypeId != undefined) {
                searchUrl += '&event_type=' + eventTypeId;
            }

            if (date != undefined && parsedDate.isValid()) {
                searchUrl += '&begin_date_time__gte=' + parsedDate.startOf().format();
                // por algum motivo no chrome se não somar 1 dia ele pega o dia anterior
                searchUrl += '&begin_date_time__lt=' + parsedDate.add('d', 1).endOf().format();
            }

            $http.get(searchUrl).success(function (data) {
                clbk(data.objects);
            });
        },

        /**
         * Procura por yokoshis cujo nome satisfaça searchToken, incluindo no resultado se o yokoshi está presente ou não no evento corrente.
         * @param clbk
         * @param searchTerm
         */
        findYokoshiForCheckin: function (searchTerm, clbk) {
            var event = $cookieStore.get('event');

            if (event == undefined) {
                notificationService.error('Oops!!', 'Selecione um evento antes de começar a fazer checkin =)!');
                return;
            }

            if (searchTerm.length > 0) {
                var eventId = event.id;
                var upperCaseRegex = new RegExp('^[A-Z]+$');
                var usedSearchTerm = searchTerm;

                var nameQueryFilter = '&complete_name__iregex=';
                if (upperCaseRegex.test(searchTerm)) {
                    var upperSearchToken = '.*[ ]';
                    // TODO: melhorar essa regex
                    var uppercaseSearchTerm = searchTerm.replace(/(?=[A-Z])([A-Z]?)/g, upperSearchToken + "$1");
                    usedSearchTerm = uppercaseSearchTerm.substring(upperSearchToken.length) + '.*';
                    nameQueryFilter = '&complete_name__regex='
                } else {
                    // TODO: refatorar isso daqui; solucao paleativa!!
                    usedSearchTerm = usedSearchTerm.replace(' ', '.*');
                    usedSearchTerm = usedSearchTerm.replace('e', '[eéêè]');
                    usedSearchTerm = usedSearchTerm.replace('a', '[aãáäâ]');
                    usedSearchTerm = usedSearchTerm.replace('i', '[ií]');
                    usedSearchTerm = usedSearchTerm.replace('u', '[uúü]');
                    usedSearchTerm = usedSearchTerm.replace('o', '[oôö]');
                }

                $http.get('/api/v1/presence_count/?format=json&event_id=' + eventId + nameQueryFilter + usedSearchTerm).success(function (data) {
                    clbk(data.objects);
                });
            }
            else if (searchTerm.length == 0) {
                clbk([]);
            }
        },

        /**
         *
         * @param user
         * @param clbk
         */
        confirmPresence: function (user, clbk) {
            var url = '/attendancebook/confirm_presence/?current_event='+$cookieStore.get('event').id + '&yokoshi=' + user.id;

            if(user.firsttime === true){
                url = url + '&is_first_time=true';
            }else{
                url = url + '&is_first_time=false';
            }

            $http.get(url).success(function (data) {
                clbk(user);

            });
        },

        /**
         *
         * @param user
         * @param clbk
         */
        cancelPresence: function (user, clbk) {
            $http.get('/attendancebook/cancel_presence/?current_event='+ $cookieStore.get('event').id +'&yokoshi=' + user.id).success(function (data) {
                clbk(user);

            });
        },

        findOrCreateToday: function(eventType, clbk){
            $http.post('/attendancebook/find_or_create_event_for_today/?event_type_id='+ eventType).success(function(data){
                clbk(JSON.parse(data));
            });
        }
    }
}]);
