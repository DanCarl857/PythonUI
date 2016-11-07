'use strict';

/**
 * @ngdoc overview
 * @name kevinApp
 * @description
 * # kevinApp
 *
 * Main module of the application.
 */
angular
  .module('kevinApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ui.router'
  ])
  .config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/home',
        templateUrl: 'views/home.html',
        controller: 'homeCtrl'
      });

    $urlRouterProvider.otherwise('/home');
  });
