function iniciarMap(){
    var coord = {lat:-33.43270640927492, lng:-70.61489957158626};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 10,
        center:coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}