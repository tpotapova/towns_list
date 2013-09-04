var app = angular.module('abc',[]);

function MyController($scope, $http) {
   $scope.currentPage = 0;
   $scope.pageSize = 10;
   $http({
	method:"GET",
url:'/towns'}).success(function(result){
$scope.towns = result});
	$scope.numberOfPages=function(){
        if (!$scope.towns) {
			return;
		}
		return Math.ceil($scope.towns.length/$scope.pageSize);                
    }
    
}
app.filter('startFrom', function() {
    return function(input, start) {
        start = +start; 
        if (!input) {
			return;
		}
		return input.slice(start);
    }
});


