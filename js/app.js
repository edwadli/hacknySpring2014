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
            setTimeout(addTestPoints, 3000);
            }
        }
    };


    // center: {lat: lat || 40.6700, lng: lng || -73.9400},

    function addTestPoints() {
        var points = [],
        s = 40.79,
        w = -74.00,
        n = 40.80,
        e = -73.90;

        for (var i = 0; i < 100; i++) {
            points.push({
                lat: 0.4*(n-s) + s + 0.2*(n-s)*Math.random(),
                lng: 0.4*(e-w) + w + 0.2*(e-w)*Math.random()
            });
        }
        Map.addHeatmapPoints(points);
    }

    function setBounds(bounds) {
        console.log("bounds set: " + bounds);
    }

    return App;
});