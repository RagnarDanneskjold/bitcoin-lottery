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
		app.model = data;
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
		    height: 200
		    // colorDark : "#000000",
		    // colorLight : "#ffffff",
		    // correctLevel : QRCode.CorrectLevel.H
		});

		new Ticker(document.querySelector('.ticker-container'));

		var $addrInput = $("#ticket-query input");
		var $ticketQueryForm = $('#ticket-query');
		$ticketQueryForm.submit(function(e){
			e.preventDefault();
			var addr = $addrInput[0].innerHTML;
			console.log(addr);
			$.get('api/ticketsByAddress?addr=' + addr).done(function(numSatoshi){
				console.log(numSatoshi)
				$ticketQueryForm.find('.result')[0].innerHTML = parseInt(numSatoshi) / 100000 + ' tickets';
			});
		})

	}
};

var utils = {

	log:function(){
		console.log('log:', arguments)
	}

}