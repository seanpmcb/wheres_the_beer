var map;

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

$(document).ready(function() {
    WEB_SOCKET_SWF_LOCATION = "/static/WebSocketMain.swf";
    WEB_SOCKET_DEBUG = true;

    // connect to the websocket
    var socket = io.connect('/tweets');

    $(window).bind("beforeunload", function() {
        socket.disconnect();
    });

    // Listen for the event "chat" and add the content to the log
    socket.on("tweet", function(e) {
        console.log(e.coordinates + ' ' + e.text);
        var coords = e.coordinates;
        var myLatLng = new google.maps.LatLng(coords[0], coords[1]);
        var marker = new google.maps.Marker({
            animation: google.maps.Animation.DROP,
            position: myLatLng,
            map: map,
            title: e.username + ": " + e.text
        });
    });
});