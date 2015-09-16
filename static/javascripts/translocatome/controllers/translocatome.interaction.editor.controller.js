(function ()
{
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeInteractionEditorController', TranslocatomeInteractionEditorController);

    TranslocatomeInteractionEditorController.$inject = ['$scope', '$http', 'growl', '$stateParams', '$modalInstance'];

    function TranslocatomeInteractionEditorController($scope, $http, growl, $stateParams, $modalInstance)
    {

        function init()
        {
            var interactionId = $stateParams.id;

            $scope.interaction = $scope.interaction || {};
            if (interactionId)
            {
                loadInteraction(interactionId);
            }

            $scope.loading = false;
        }

        function loadInteraction(interactionId)
        {
            $http.get('api/translocatome/rest-api/interaction/' + interactionId + '/')
                .then(function(response)
                {
                    $scope.interaction = response.data;
                }, function(response) {
                    growl.addErrorMessage('Errors: ' + response.data);
                });
        }

        $scope.save = function ()
        {
            $scope.loading = true;
            if ($scope.interaction.id)
            {
                $http.put('api/translocatome/rest-api/interaction/' + $scope.interaction.id + '/', $scope.interaction)
                    .then(function ()
                    {
                        growl.addSuccessMessage('successfully updated');
                    }, function (response)
                    {
                        growl.addErrorMessage('Errors: ' + response.data);
                    })
                    .finally(function ()
                    {
                        $scope.loading = false;
                    });
            } else
            {
                $http.post('api/translocatome/rest-api/interaction/', $scope.interaction)
                    .then(function ()
                    {
                        growl.addSuccessMessage('successfully updated');
                    }, function (response)
                    {
                        growl.addErrorMessage('Errors: ' + response.data);
                    })
                    .finally(function ()
                    {
                        $scope.loading = false;
                    });
            }
        };

        $scope.deleteInteraction = function()
        {
            $scope.loading = true;
            if (confirm('Are you sure you want to delete this node?'))
            {
                $http.delete('api/translocatome/rest-api/interaction/' + $scope.interaction.id + '/')
                    .then(function ()
                    {
                        growl.addSuccessMessage('successfully deleted');
                        $scope.cancel();
                    }, function (response)
                    {
                        growl.addErrorMessage('Errors: ' + response.data);
                    })
                    .finally(function ()
                    {
                        $scope.loading = false;
                    });
            }
        };

        $scope.cancel = function ()
        {
            $modalInstance.dismiss('cancel');
        };

        init();
    }
})();
