Ticker = function(element, countdownSeconds){

	var secondsLeft = countdownSeconds;

	var lastTime = Date.now();
	function tick(){
		secondsLeft -= (Date.now() - lastTime) / 1000; 
		// console.log(secondsLeft);
		// console.log(Date.now() - lastTime);
		lastTime = Date.now();

		var hours, minutes, seconds;

		hours = Math.floor(secondsLeft / 3600);
		// console.log('hours', hours);

		minutes = Math.floor((secondsLeft/60) % 60)
		seconds = Math.floor(secondsLeft % 60);

		element.innerHTML = hours + ':' + minutes + ':' + seconds;
	}

	setInterval(tick, 1000);

};