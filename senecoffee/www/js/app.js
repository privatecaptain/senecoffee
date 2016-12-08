// Ionic Starter App
// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {

    if(window.cordova && window.cordova.plugins.Keyboard) {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

      // Don't remove this line unless you know what you are doing. It stops the viewport
      // from snapping when text inputs are focused. Ionic handles this internally for
      // a much nicer keyboard experience.
      cordova.plugins.Keyboard.disableScroll(true);
    }
	if (window.cordova) {
		console.log(cordova.platformId);
	}
    if(window.StatusBar) {
      StatusBar.hide();
	//   StatusBar.backgroundColorByHexString("#ffffff");
  }

  });
}).config(function($stateProvider, $urlRouterProvider) {
        $stateProvider
            .state('index', {
                url: '/',
                templateUrl: 'index.html',
				abstract: 'true'
            }).state('nh',{
				url: '/nh',
				templateUrl: 'templates/nh.html'
			}).state('campus',{
				url: '/campus',
				templateUrl : 'templates/campus.html'
			}).state('sy',{
				url: '/sy',
				templateUrl : 'templates/sy.html'
			}).state('mk',{
				url: '/mk',
				templateUrl : 'templates/mk.html'
			}).state('kg',{
				url: '/kg',
				templateUrl : 'templates/kg.html'
			}).state('comingsoon',{
				url: '/comingsoon',
				templateUrl : 'templates/comingsoon.html'
			})
			$urlRouterProvider.otherwise('/campus');

    }).config(function($ionicConfigProvider) {
  $ionicConfigProvider.scrolling.jsScrolling(false);
 
  // Or for only a single platform, use
  // if( ionic.Platform.isAndroid() ) {
    // $ionicConfigProvider.scrolling.jsScrolling(false);
  // }
}).controller('MyCtrl',function($scope){

});
