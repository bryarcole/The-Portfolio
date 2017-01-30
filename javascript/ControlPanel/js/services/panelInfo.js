app.factory('events', ['$http', function($http){
  return $http.get('<getJSON>')
  .success(function(data){
    return data;
  })
  .error(function(err){
    return err;
  });
}]);