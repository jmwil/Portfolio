var weather = new XMLHttpRequest();
var forecast = new XMLHttpRequest();

// Pulls the Data form the API and plugs it into HTML page
function changeWeather(){
  var w = JSON.parse(weather.response);
  var currentLocation = w.current_observation.display_location.full;
  var currentCondition = w.current_observation.weather;
  var currentTemp = w.current_observation.temp_f + "&#8457";
  var currentIcon = w.current_observation.icon_url;
  document.getElementById("currentWeather").innerHTML = currentCondition;
  document.getElementById("currentTemp").innerHTML = currentTemp;
  document.getElementById("currentLoc").innerHTML = currentLocation;
  document.getElementById("currentIcon").src = currentIcon;
  document.getElementById("currentTemps").innerHTML = currentTemp;
  document.getElementById("currentLocs").innerHTML = currentLocation;
  document.getElementById("currentIcons").src = currentIcon;
  document.getElementById("currentWeathers").innerHTML = currentCondition;
};

// Pulls Data from API and plugs it into HTML page.
function changeForecaset(){
  var f = JSON.parse(forecast.response);
  var f2day = f.forecast.simpleforecast.forecastday[1].date.weekday;
  var f3day = f.forecast.simpleforecast.forecastday[2].date.weekday;
  var f4day = f.forecast.simpleforecast.forecastday[3].date.weekday;
  var f2degree = f.forecast.simpleforecast.forecastday[1].high.fahrenheit + "&#8457";
  var f3degree = f.forecast.simpleforecast.forecastday[2].high.fahrenheit + "&#8457";
  var f4degree = f.forecast.simpleforecast.forecastday[3].high.fahrenheit + "&#8457";
  var f2icon = f.forecast.txt_forecast.forecastday[2].icon_url;
  var f3icon = f.forecast.txt_forecast.forecastday[4].icon_url;
  var f4icon = f.forecast.txt_forecast.forecastday[6].icon_url;
  document.getElementById("f2day").innerHTML = f2day;
  document.getElementById("f3day").innerHTML = f3day;
  document.getElementById("f4day").innerHTML = f4day;
  document.getElementById("f2degree").innerHTML = f2degree;
  document.getElementById("f3degree").innerHTML = f3degree;
  document.getElementById("f4degree").innerHTML = f4degree;
  document.getElementById("f2icon").src = f2icon;
  document.getElementById("f3icon").src = f3icon;
  document.getElementById("f4icon").src = f4icon;
  document.getElementById("f2days").innerHTML = f2day;
  document.getElementById("f3days").innerHTML = f3day;
  document.getElementById("f4days").innerHTML = f4day;
  document.getElementById("f2degrees").innerHTML = f2degree;
  document.getElementById("f3degrees").innerHTML = f3degree;
  document.getElementById("f4degrees").innerHTML = f4degree;
  document.getElementById("f2icons").src = f2icon;
  document.getElementById("f3icons").src = f3icon;
  document.getElementById("f4icons").src = f4icon;
};

// Loads the current Portland Weather from the API
function getPortlandWeather(){
  weather.open("GET", "http://api.wunderground.com/api/8722966887363966/conditions/q/97225.json", false);
  weather.send(null);
  changeWeather();
};

// Loads the current Portland forecast from the API
function getPortlandForecast(){
  forecast.open("GET", "http://api.wunderground.com/api/8722966887363966/forecast/q/97225.json", false);
  forecast.send(null);
  changeForecaset();
};

// Grabs new Zip to change weather
function newWeather(){
  var newZip = document.getElementById("zip").value;
  var beginning = "http://api.wunderground.com/api/8722966887363966/conditions/q/";
  var ending = ".json";
  var newWeatherString = beginning + newZip + ending;
  weather.open("GET", newWeatherString, false);
  weather.send(null);
  changeWeather();
};

// Grabs new zip code to change forecast
function newForecast(){
  var newZip = document.getElementById("zip").value;
  var forebeginning = "http://api.wunderground.com/api/8722966887363966/forecast/q/";
  var ending = ".json";
  var newForecastString = forebeginning + newZip + ending;
  forecast.open("GET", newForecastString, false);
  forecast.send(null);
  changeForecaset();
};

// Changes the forecast to the newly entered Zipcode
function getZip(){
  newWeather();
  newForecast();
};

// Loads HTML with current weather on startup
getPortlandWeather();
getPortlandForecast();
