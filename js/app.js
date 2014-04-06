define(['map', 'firebase'], function (Map, Firebase) {

    var fireRef;

    var App = {
        init: function(firebaseUrl) {
            fireRef = new Firebase(firebaseUrl);
            Map.onLoad = setBounds;
            Map.onBoundsChanged = setBounds;
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (location) {
                    Map.load(location.coords.latitude, location.coords.longitude);
                }, function error (msg) {
                    console.log("Error: " + msg);
                    Map.load();
                });
            }
            fireRef.child('heatmap').on('value', function(snapshot) {
                Map.setHeatmapPoints(snapshot.val());
            });
            fireRef.child('markers').on('value', function(snapshot) {
                Map.setMarkers(snapshot.val());
            });
        }
    };

    function setBounds(bounds) {
        console.log("bounds set: " + bounds);
        ne = bounds.getNorthEast();
        sw = bounds.getSouthWest();
        fireRef.child('bounds').set([
            {lat: ne.lat(), lng: ne.lng()},
            {lat: sw.lat(), lng: sw.lng()} ]);
    }

    return App;
});