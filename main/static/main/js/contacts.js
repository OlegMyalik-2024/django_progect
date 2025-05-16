let map;
let marker;
function initMap (){
    map = new ymaps.Map("yandexmap", {center: [53.919664, 27.638718], zoom: 16});
    marker = new ymaps.Placemark([53.919664, 27.638718], {hintContent: 'Расположение', 
        balloonContent: 'Это наша организация'});
    map.geoObjects.add(marker);
}
ymaps.ready(initMap);