var app = angular.module('ControlPanelApp', ['ngRoute']);

app.config(function($routeProvider){
  $routeProvider
    .when('/',{
    controller: '#',
    templateUrl: '#'
  })
  .when('/:id', {
    controller: '#',
    templateUrl: '#'
  })
    .otherwise({
    redirectTo: '/'
  });
});