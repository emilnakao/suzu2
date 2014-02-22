suzuClientApp.directive('keyTrap', function() {
  return function( scope, elem ) {
    elem.bind('keydown', function( event ) {
        console.log('keydown');
      scope.$broadcast('keydown', event.keyCode );
    });
  };
});