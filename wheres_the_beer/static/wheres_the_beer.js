var map;
var markers = [];

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(38, -98),
        zoom: 2,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
                                  mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);

function make_marker(tweet){
        var coords = tweet.coordinates;
        var myLatLng = new google.maps.LatLng(coords[0], coords[1]);
        var marker = new google.maps.Marker({
            animation: google.maps.Animation.DROP,
            position: myLatLng,
            title: tweet.username + ": " + tweet.text
        });
        return marker;
}

function plot_marker(marker){
    if ( typeof(marker) != "undefined") {
        marker.setMap(map);
    }
}

function plot_markers(){
    plot_marker(markers.shift());
    setTimeout(plot_markers, 25);
}

$(document).ready(function() {
    WEB_SOCKET_SWF_LOCATION = "/static/WebSocketMain.swf";
    WEB_SOCKET_DEBUG = true;

    // connect to the websocket
    var socket = io.connect('/tweets');

    $(window).bind("beforeunload", function() {
        socket.disconnect();
    });

    // Listen for the event "chat" and add the content to the log
    socket.on("tweet", function(tweet) {
        marker = make_marker(tweet);
        plot_marker(marker);
    });

    $.getJSON("old_data", function(json){
        $.each(json.data, function(index, tweet){
            markers.push(make_marker(tweet));
        });
        plot_markers();
    });
});