define(['jquery','underscore'], function($, _) {
    var infoWindow, map;
    var Infobox = {
        init: function (info, gmap) {
            infoWindow = info;
            map = gmap;
        },
        setMarker: function (marker, data) {
            infoWindow.setContent(makeContent(data));
            infoWindow.open(map, marker);
            console.log(data);
        },
        close: function () {
            infoWindow.close();
        }
    };

    var infoboxTemplate = _.template("<table id='infobox'><td><div id='tweets'><%= tweets %></div></td><td><div id='pics'><%= pics %></div></td></table>");
    var tweetTemplate = _.template("<p class='tweet'><%= tweet %></p>");
    var picTemplate = _.template("<img src='<%= url %>'>");

    function makeContent(data) {
        var tweetsDom = "";
        data.tweets.forEach(function (tweet) {
            tweetsDom += tweetTemplate({tweet: tweet});
        });
        var picsDom = "";
        data.instagrams.forEach(function (url) {
            picsDom += picTemplate({url: url});
        });
        return infoboxTemplate({tweets: tweetsDom, pics: picsDom});
    }

    return Infobox;
});