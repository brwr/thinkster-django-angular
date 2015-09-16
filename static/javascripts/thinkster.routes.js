(function ()
{
    'use strict';

    angular
        .module('thinkster.routes')
        .config(config);

    //config.$inject = ['$routeProvider'];
    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    //function config($routeProvider) {
    function config($stateProvider, $urlRouterProvider)
    {

        // For any unmatched URL
        $urlRouterProvider.otherwise('/');

        // States
        $stateProvider
            .state('index', {
                url: '/',
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layout/index.html'
            })
            .state('register', {
                url: '/register',
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layout/index.html'
            })
            .state('login', {
                url: '/login',
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/login.html'
            })
            .state('interaction', {
                url: '/translocatome/interaction',
                controller: 'TranslocatomeInteractionController',
                templateUrl: '/static/templates/translocatome/interaction.html'
            })
            .state('interaction.edit', {
                url: '/:id',
                onEnter: ['$stateParams', '$state', '$modal', function($stateParams, $state, $modal) {
                    $modal.open({
                        templateUrl: '/static/templates/translocatome/interaction.editor.html',
                        controller: 'TranslocatomeInteractionEditorController'
                    }).result.finally(function() {
                            $state.go('^');
                        });
                }]
            })
            .state('node', {
                url: '/translocatome/node',
                controller: 'TranslocatomeNodeController',
                templateUrl: '/static/templates/translocatome/node.html'
            })
            .state('node.edit', {
                url: '/:id',
                onEnter: ['$stateParams', '$state', '$modal', function($stateParams, $state, $modal) {
                    $modal.open({
                        templateUrl: 'static/templates/translocatome/node.editor.html',
                        controller: 'TranslocatomeNodeEditorController'
                    }).result.finally(function() {
                            $state.go('^');
                        });
                }]
             })
            .state('user', {
                url: '/+:username',
                controller: 'AccountController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/accounts/account.html'
            })
            .state('user.settings', {
                url: '/+:username/settings',
                controller: 'AccountSettingsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/accounts/settings.html'
            });
    }
})();
