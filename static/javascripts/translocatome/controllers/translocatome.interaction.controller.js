(function ()
{
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeInteractionController', TranslocatomeInteractionController);

    TranslocatomeInteractionController.$inject = ['$scope', '$http'];

    function TranslocatomeInteractionController($scope, $http)
    {

        function init()
        {
            $scope.interactions_with_meta = [];

            $scope.loadingNodes = {};
            $scope.noResults = {};

            $scope.showColumnSorter = false;
            $scope.displayedInteractionColumns = [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F'
            ];
            $scope.interactionColumns = [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ];
            loadFields();
        }

        function loadFields()
        {
            $http.get('api/translocatome/api/interaction/fields/')
                .then(function (response)
                {
                    $scope.fields = response.data.fields;
                });
        }

        $scope.queryNodesByUniProtAc = function (uniProtAc)
        {
            return $http.get('api/translocatome/rest-api/query-nodes/', {
                params: {
                    uni_prot_ac: uniProtAc
                }
            }).then(function (response)
            {
                return response.data;
            });
        };

        $scope.queryNodesByGeneName = function (geneName)
        {
            return $http.get('api/translocatome/rest-api/query-nodes/', {
                params: {
                    gene_name: geneName
                }
            }).then(function (response)
            {
                return response.data;
            });
        };

        $scope.onSourceSelect = function ($item)
        {
            $scope.sourceNode = angular.copy($item);
        };

        $scope.onTargetSelect = function ($item)
        {
            $scope.targetNode = angular.copy($item);
        };

        $scope.swapNodes = function ()
        {
            var tempNode = $scope.sourceNode;
            $scope.sourceNode = $scope.targetNode;
            $scope.targetNode = tempNode;
        };

        $scope.removeColumn = function (columnIndex)
        {
            $scope.interactionColumns.splice(columnIndex, 1);
        };

        $scope.fetchInteractionsWithMeta = function ()
        {
            var params = {};

            if ($scope.sourceNode)
            {
                params.source_node_id = $scope.sourceNode.id;
            }

            if ($scope.targetNode)
            {
                params.target_node_id = $scope.targetNode.id;
            }

            $http.get('api/translocatome/rest-api/query-interactions/', {
                params: params
            }).then(function (response)
            {
                $scope.interactions_with_meta = response.data;
            });
        };

        init();
    }
})();
