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

		var qrAnchor = document.querySelector('#address-container .qr-code');
		var qrcode = new QRCode(qrAnchor, {
		    text: 'bitcoin:' + this.model.address,
		    width: 200,
		    height: 200
		});

		new Ticker(document.querySelector('.ticker-container'));

		var $addrInput = $("#ticket-query input");
		var $ticketQueryForm = $('#ticket-query');
		$ticketQueryForm.submit(function(e){
			e.preventDefault();
			var addr = $addrInput[0].innerHTML;
			$.get('api/ticketsByAddress?addr=' + addr).done(function(numSatoshi){
				var tix = parseInt(numSatoshi) / 100000;
				console.log('tix', tix);
				var chance = tix / Math.floor(app.model.final_balance / 100000) * 100;
				$ticketQueryForm.find('.result')[0].innerHTML = tix + ' tickets. ' + chance + '% chance to win';
			});
		})

	}
};

var utils = {

	log:function(){
		console.log('log:', arguments)
	}

}