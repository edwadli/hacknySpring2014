define(['map', 'firebase'], function (Map, Firebase) {

    var fireRef;

    var App = {
        init: function(firebaseUrl) {
            fireRef = new Firebase(firebaseUrl);
            Map.onLoad = function() {
                setCallback();
                // Map.setMarkers([{
                //     lat: 40.6700,
                //     lng: -73.9400,
                //     tweets: ["hi", "hello"],
                //     instagrams: ["https://developers.google.com/_static/images/silhouette36.png"]
                // }]);
            };
            Map.onBoundsChanged = setBounds;
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (location) {
                    Map.load(location.coords.latitude, location.coords.longitude);
                }, function error (msg) {
                    console.log("Error: " + msg);
                    Map.load();
                });
            } else {
                Map.load();
            }
        }
    };

    function setCallback() {
        fireRef.child('heatmap').once('value', function(snapshot) {
            if (snapshot.val() === null) return;
            console.log("received heatmap: " + snapshot.val() + Object.keys(snapshot.val()).length);
            var data = snapshot.val();
            var vals = Object.keys(data).map(function (key) {
                return data[key];
            });
            Map.setHeatmapPoints(vals);
        });
        fireRef.child('heatmap').on('child_added', function(snapshot) {
            if (snapshot.val() === null) return;
            // console.log("received heatmap point: " + snapshot.val());
            Map.setHeatmapPoint(snapshot.val());
        });
        fireRef.child('markers').on('value', function(snapshot) {
            if (snapshot.val() === null) return;
            console.log("received markers: " + snapshot.val().length);
            Map.setMarkers(snapshot.val());
        });
    }

    function setBounds(bounds) {
        console.log("bounds set: " + bounds);
        ne = bounds.getNorthEast();
        sw = bounds.getSouthWest();
        fireRef.child('bounds').set([
            {lat: ne.lat(), lng: ne.lng()},
            {lat: sw.lat(), lng: sw.lng()} ]);
        fireRef.child('changed').set(true);
    }

    return App;
});