define(['gmaps'], function (gmaps) {
    var map, outerBounds, // outer bounding box
    heatmap = new gmaps.visualization.HeatmapLayer({data:[]}),
    heatmapData = [],
    markers = [],
    OUTER_BOUNDS_RATIO = 3;

    var Map = {
        load: function loadMap(lat, lng) {
            // default location NYC
            var mapOptions = {
                center: {lat: lat || 40.6700, lng: lng || -73.9400},
                zoom: 13
            };
            map = new gmaps.Map(document.getElementById("map-canvas"),
                mapOptions);
            gmaps.event.addListenerOnce(map, 'idle', this.onLoad);
            gmaps.event.addListener(map, 'idle', function () {
                var bounds = map.getBounds();
                if (!insideOuterBounds(bounds)) {
                    outerBounds = expandBounds(bounds, OUTER_BOUNDS_RATIO);
                    this.onBoundsChanged(outerBounds);
                }
            }.bind(this));
            gmaps.event.addListener(map, 'zoom_changed', function () {
                var bounds = map.getBounds();
                outerBounds = expandBounds(bounds, OUTER_BOUNDS_RATIO);
                this.onBoundsChanged(outerBounds);
            }.bind(this));
        },
        // default onBoundsChanged function, is given outer bounds as argument
        onBoundsChanged: function (bounds) {
            console.log("bounds changed");
        },
        onLoad: function(){console.log("loaded");},
        setHeatmapPoints: function (points) {
            heatmapData = [];
            points.forEach(function (point) {
                var p =new gmaps.LatLng(point.lat, point.lng);
                heatmapData.push(p);
            });
            updateHeatmap();
        },
        setMarkers: function (markerData) {
            // remove old markers
            markers.forEach(function (marker) {
                marker.setMap(null);
            });
            markers = [];
            markerData.forEach(function(data) {
                var marker = new gmaps.Marker({
                    position: new gmaps.LatLng(data.lat, data.lng),
                    map: map
                });
                markers.push(marker);
                // add meta data
            });
        }
    };

    function updateHeatmap() {
        heatmap.setMap(null);
        heatmap = new gmaps.visualization.HeatmapLayer({data: heatmapData});
        heatmap.setMap(map);
    }

    // true if outerBounds exists and viewport corners are inside outerBounds
    function insideOuterBounds(bounds) {
        return outerBounds && outerBounds.contains(bounds.getNorthEast()) &&
        outerBounds.contains(bounds.getSouthWest());
    }

    function expandBounds(bounds, ratio) {
        var ne = bounds.getNorthEast(),
        sw = bounds.getSouthWest(),
        c = bounds.getCenter();
        sw = expandLatLng(c, sw, ratio);
        ne = expandLatLng(c, ne, ratio);
        return new gmaps.LatLngBounds(sw, ne);
    }

    function expandLatLng(center, corner, ratio) {
        var dlat = corner.lat() - center.lat(),
        dlng = corner.lng() - center.lng();
        return new gmaps.LatLng(center.lat() + ratio*dlat, center.lng() + ratio*dlng);
    }

    return Map;
});