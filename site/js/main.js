window.addEventListener('load', function(){
	_.templateSettings = {
  		interpolate: /\{\{(.+?)\}\}/g
	};


	var mainTemplateEl = document.querySelector('#main.template');
	mainTemplateEl.remove();
	mainTemplateEl.classList.remove('template');

	app.template = _.template(mainTemplateEl.outerHTML);

	// getting the target address for this week
	$.get('api/targetAddress').done(function(dataStr){
		var data = JSON.parse(dataStr);
		console.log(data);

		app.model.rawData = data;
		app.model.address = data.address;
		app.model.satoshi = data.total_received;
		app.render();

	});

});

var app = {
	model:{},
	render:function(){
		document.body.innerHTML = this.template(this.model);
		console.log(this)

		var qrAnchor = document.querySelector('#address-container .qr-code');
		var qrcode = new QRCode(qrAnchor, {
		    text: 'bitcoin:' + this.model.address,
		    width: 200,
		    height: 200,
		    colorDark : "#000000",
		    colorLight : "#ffffff",
		    correctLevel : QRCode.CorrectLevel.H
		});

		new Ticker(document.querySelector('.ticker-container'), this.model.rawData.secondsLeft);

	}
};

var utils = {

	log:function(){
		console.log('log:', arguments)
	}

}