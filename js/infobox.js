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
    var picTemplate = _.template("<a href='<%= url %>'><img src='<%= thumb %>'></a>");

    function makeContent(data) {
        var tweetsDom = "";
        data.tweets.forEach(function (tweet) {
            tweetsDom += tweetTemplate({tweet: tweet.text});
        });
        var picsDom = "";
        data.images.forEach(function (image) {
            picsDom += picTemplate({thumb: image.thumbnail.url, url: image.standard_resolution.url});
        });
        return infoboxTemplate({tweets: tweetsDom, pics: picsDom});
    }

    return Infobox;
});