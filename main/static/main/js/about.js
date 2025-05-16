var timeElement = document.getElementById('currentTime');
    setInterval(function () {
      var currentTime = new Date();
      timeElement.textContent = currentTime.toLocaleTimeString();
    }, 1000);