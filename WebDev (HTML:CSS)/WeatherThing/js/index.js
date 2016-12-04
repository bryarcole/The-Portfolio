//Variables

var lat;
var lon;
var weatherAPI;
var apiURL;

//Selector

function startApp() {
    navigator.geolocation.getCurrentPosition(function(pos){
        var lat = Position.coords.latitude;
        var lon = Position.coords.longitude;
        setWeatherUrl(lat,lon);
        getWeatherAPI();
        setWeather();

    });
}
function setWeather() {
  fOrC();
  if (typeof weatherAPI === "object") {
    setCurrentWeather(formatConditions(weatherAPI.currently.icon));
    setForecastWeather();
  }
}
function setWeatherUrl(lat,lon) {
    apiURL = "https://api.forecast.io/forecast/e633c6f89f0b17cd90a483c50272da7f/" + lat+ "," +lon;
}

function getWeatherAPI() {
    setWeatherUrl();
    $.ajax({
        type: 'GET',
        dataType: 'jsonp',
        url: apiURL,
        success: function(stuff) {
            weatherAPI = stuff;
            setWeather();
        }
    }).done(function(){
        alert("Alldone loading API!")
    });
}
