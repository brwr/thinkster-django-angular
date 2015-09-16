(function ()
{
    'use strict';

    angular
        .module('thinkster', [
            'thinkster.config',
            'thinkster.routes',
            'thinkster.accounts',
            'thinkster.authentication',
            'thinkster.layout',
            'thinkster.posts',
            'thinkster.translocatome',
            'thinkster.utils',
            'angular-growl'
        ]);

    angular
        .module('thinkster.config', []);

    angular
        .module('thinkster.routes', ['ngRoute', 'ui.router']);

    angular
        .module('thinkster')
        .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http)
    {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
