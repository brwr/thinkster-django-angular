(function () {
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeNodeController', TranslocatomeNodeController);

    TranslocatomeNodeController.$inject = ['$scope', '$http'];

    function TranslocatomeNodeController($scope, $http) {

        function init() {
            $scope.search = {};
        }

        $scope.autoSearchNode = function() {
            var queryUniProtAc = undefined;
            var queryGeneName = undefined;

            if ($scope.search.uni_prot_ac && $scope.search.uni_prot_ac.length > 2) {
                queryUniProtAc = $scope.search.uni_prot_ac;
            }

            if ($scope.search.gene_name && $scope.search.gene_name.length > 2) {
                queryGeneName = $scope.search.gene_name;
            }

            $scope.searchNode(queryUniProtAc, queryGeneName);
        };

        $scope.searchNode = function(uniProtAc, geneName) {
            var queryParams = {};

            if (uniProtAc) {
                queryParams.uni_prot_ac = uniProtAc;
            }

            if (geneName) {
                queryParams.gene_name = geneName;
            }

            $http.get('api/translocatome/query-nodes/', {
                params: queryParams
            }).then(function(response) {
                $scope.nodes = response.data.nodes;
            });
        };

        init();
    }
})();
