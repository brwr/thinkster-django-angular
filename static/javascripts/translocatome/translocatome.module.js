(function () {
    'use strict';

    angular
        .module('thinkster.translocatome', [
            'thinkster.translocatome.controllers'
        ]);

    angular
        .module('thinkster.translocatome.controllers', ['ui.bootstrap', 'scrollable-table']);
})();
