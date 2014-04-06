define(['gmaps'], function (gmaps) {
    var map,
    heatmap = new gmaps.visualization.HeatmapLayer({data:[]}),
    heatmapData = [],
    BOUNDS_CHANGE_DELAY = 1000,
    bounds_change_timer = null;

    var Map = {
        load: function loadMap(lat, lng) {
            // default location NYC
            var mapOptions = {
                center: {lat: lat || 40.6700, lng: lng || -73.9400},
                zoom: 13
            };
            map = new gmaps.Map(document.getElementById("map-canvas"),
                mapOptions);
            gmaps.event.addListener(map, 'bounds_changed', function () {
                var bounds = map.getBounds();
                clearTimeout(bounds_change_timer);
                bounds_change_timer = setTimeout(function(){
                    removeUnboundedPoints(bounds);
                    this.onBoundsChanged(bounds);
                }.bind(this), BOUNDS_CHANGE_DELAY);
            }.bind(this));
        },
        // default onBoundsChanged function
        onBoundsChanged: function (bounds) {
            console.log("bounds changed");
        },
        addHeatmapPoints: function (points) {
            points.forEach(function (point) {
                var p =new gmaps.LatLng(point.lat, point.lng);
                heatmapData.push(p);
            });
            updateHeatmap();
        }
    };

    function removeUnboundedPoints(bounds) {
        var oldLength = heatmapData.length;
        heatmapData = heatmapData.filter(function(point) {
            return bounds.contains(point);
        });
        if (heatmapData.length !== oldLength) {
            updateHeatmap();
        }
    }

    function updateHeatmap() {
        heatmap.setMap(null);
        heatmap = new gmaps.visualization.HeatmapLayer({data: heatmapData});
        heatmap.setMap(map);
    }

    return Map;
});