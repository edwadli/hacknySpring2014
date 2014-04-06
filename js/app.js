define(['map'], function (Map) {

    var App = {
        init: function() {
            Map.onLoad = Map.setMarkers.bind(Map, getTestPoints());
            Map.onBoundsChanged = setBounds;
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (location) {
                    Map.load(location.coords.latitude, location.coords.longitude);
                }, function error (msg) {
                    console.log("Error: " + msg);
                    Map.load();
                });
            getTestPoints();

            }
        }
    };


    // center: {lat: lat || 40.6700, lng: lng || -73.9400},

    function getTestPoints(sw, ne) {
        var points = [],
        s = 40.79,
        w = -74.00,
        n = 40.80,
        e = -73.90;
        if (sw && ne) {
            s = sw.lat();
            w = sw.lng();
            n = ne.lat();
            e = ne.lng();
        }

        for (var i = 0; i < 50; i++) {
            points.push({
                lat: s + (n-s)*Math.random(),
                lng: w + (e-w)*Math.random()
            });
        }
        return points;
    }

    function setBounds(bounds) {
        console.log("bounds set: " + bounds);
        Map.setMarkers(getTestPoints(bounds.getSouthWest(), bounds.getNorthEast()));
    }

    return App;
});