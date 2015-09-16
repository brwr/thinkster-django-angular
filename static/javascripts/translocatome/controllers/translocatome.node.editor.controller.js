(function ()
{
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeNodeEditorController', TranslocatomeNodeEditorController);

    TranslocatomeNodeEditorController.$inject = ['$scope', '$http', 'growl', '$stateParams', '$modalInstance'];

    function TranslocatomeNodeEditorController($scope, $http, growl, $stateParams, $modalInstance)
    {

        function init()
        {
            var nodeId = $stateParams.id;

            $scope.node = $scope.node || {};
            if (nodeId)
            {
                loadNode(nodeId);
            }

            $scope.loading = false;
        }

        function loadNode(nodeId)
        {
            $http.get('api/translocatome/rest-api/node/' + nodeId + '/')
                .then(function(response)
                {
                    $scope.node = response.data;
                }, function(response) {
                    growl.addErrorMessage('Errors: ' + response.data);
                });
        }

        $scope.deleteNode = function ()
        {
            $scope.loading = true;
            if (confirm('Are you sure you want to delete this node?'))
            {
                $http.delete('api/translocatome/rest-api/node/' + $scope.node.id + '/')
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

        $scope.save = function ()
        {
            $scope.loading = true;
            if ($scope.node.id)
            {
                $http.put('api/translocatome/rest-api/node/' + $scope.node.id + '/', $scope.node)
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
                $http.post('api/translocatome/rest-api/node/', $scope.node)
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

        $scope.cancel = function ()
        {
            $modalInstance.dismiss('cancel');
        };

        init();
    }
})();
