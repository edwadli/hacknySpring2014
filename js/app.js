define(['map'], function (Map) {

    var App = {
        init: function() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (location) {
                    Map.load(location.coords.latitude, location.coords.longitude);
                }, function error (msg) {
                    console.log("Error: " + msg);
                    Map.load();
                });
            }
        }
    };

    return App;
});