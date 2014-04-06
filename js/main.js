requirejs.config({
    paths: {
        'async': 'lib/async',
        'jquery': "http://code.jquery.com/jquery-1.11.0.min",
        'underscore': "http://underscorejs.org/underscore-min",
        'firebase': "https://cdn.firebase.com/js/client/1.0.11/firebase"
    },
    shim: {
        'jquery': {
            'exports': "$"
        },
        'underscore': {
            'exports': "_"
        },
        'firebase': {
            'exports': "Firebase"
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
    
    $(document).ready(App.init.bind(App, "https://hotspots.firebaseio.com/"));

});