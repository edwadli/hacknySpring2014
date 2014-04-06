requirejs.config({
    paths: {
        'async': 'lib/async',
        'jquery': "http://code.jquery.com/jquery-1.11.0.min",
        'underscore': "http://underscorejs.org/underscore-min"
    },
    shim: {
        'jquery': {
            'exports': "$"
        },
        'underscore': {
            'exports': "_"
        }
    }
});

// convert Google Maps into an AMD module
define('gmaps', ['async!https://maps.googleapis.com/maps/api/js?key=AIzaSyDahbc1_iJT8jmCpMpbIZ6p7Pm1ryyIaK4&sensor=true&libraries=visualization'],
function(){
    // return the gmaps namespace for brevity
    return window.google.maps;
});


require( ['jquery', 'app'], function ( $, App ) {
    
    $(document).ready(App.init);

});