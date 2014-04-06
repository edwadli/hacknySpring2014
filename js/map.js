define(['gmaps'], function (gmaps) {
    var map;

    var Map = {
        load: function loadMap(lat, lng) {
            // default location NYC
            var mapOptions = {
                center: {lat: lat || 40.6700, lng: lng || -73.9400},
                zoom: 13
            };
            map = new gmaps.Map(document.getElementById("map-canvas"),
                mapOptions);
        }
    };

    return Map;
});