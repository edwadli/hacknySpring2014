define(['map'], function (Map) {

    var App = {
        init: function() {
            Map.onBoundsChanged = setBounds;
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

    function setBounds(bounds) {
        console.log("bounds set: " + bounds);
    }

    return App;
});