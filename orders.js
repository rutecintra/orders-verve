var app = angular.module('OrderApp', []);

app.controller('OrderController', function($scope, $http) {
  $scope.orderNumber = ''; // Número do pedido digitado pelo usuário
  $scope.order = null;     // Dados do pedido
  $scope.errorMessage = null;

  // Função para buscar o pedido
  $scope.fetchOrder = function() {
    if (!$scope.orderNumber) {
      $scope.errorMessage = 'Por favor, digite o número do pedido.';
      $scope.order = null;
      return;
    }

    // Substitua a URL abaixo pela URL da sua API
    var apiUrl = `https://sua-api.com/pedidos/${$scope.orderNumber}`;

    $http.get(apiUrl)
      .then(function(response) {
        $scope.order = response.data;
        $scope.errorMessage = null;
      })
      .catch(function(error) {
        $scope.errorMessage = 'Erro ao buscar o pedido. Verifique o número e tente novamente.';
        $scope.order = null;
      });
  };
});