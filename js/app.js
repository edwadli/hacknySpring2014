define(['gmaps'], function (gmaps) {

    function loadMap(lat, lng) {
        // default location NYC
        var mapOptions = {
            center: {lat: lat || 40.6700, lng: lng || -73.9400},
            zoom: 13
        };
        this.map = new gmaps.Map(document.getElementById("map-canvas"),
            mapOptions);
    }

    App = {
        init: function() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function (location) {
                    loadMap(location.coords.latitude, location.coords.longitude);
                }, function error (msg) {
                    console.log("Error: " + msg);
                    loadMap();
                });
            }
        }
    };

    return App;
});