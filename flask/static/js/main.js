var Message;
$messages = $('.messages');
Message = function (arg) {
		this.text = arg.text, this.message_side = arg.message_side, this.time = arg.time;
		this.draw = function (_this) {
				return function () {
						var $message;
						$message = $($('.message_template').clone().html());
						$message.addClass(_this.message_side).find('.text').html(addBr(_this.text));
						$message.addClass(_this.message_side).find('.timestamp').html(_this.time);
						$('.messages').append($message);
						return setTimeout(function () {
								return $message.addClass('appeared');
						}, 0);
				};
		}(this);
		return this;
};

function addBr(text){
		//console.log("text was: "+text)
		newText=text.replace(/\n/g, "<br />")
		newText=newText.replace(/\\n/g, "<br />")//for \n from dialogflow
		//console.log("text is: "+text)
		return newText;

};

function changeTitle(title){
		document.getElementById("title").innerHTML=title;
};

function getCurrentTimestamp()
{
	// var d=new Date(c["timestamp"][0],c["timestamp"][1],c["timestamp"][2],c["timestamp"][3],c["timestamp"][4],c["timestamp"][5],c["timestamp"][6]);
	var d = new Date();
	return d;
};

function url_google(url){
	document.getElementById("googleMap").src = url
};


function main(msg,d, data){
	var options = {month: 'short', day: 'numeric', hour:'numeric', minute: 'numeric'  };
	message = new Message({
			text: msg,
			time: d.toLocaleString("en-IN", options),
			message_side: 'right'
	});
	message.draw();
	$messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
	$('#msg_input').val('');


	showBotMessage("Une petite seconde, le temps que le son arrive à mon cerveau...", d)
	setTimeout(function(){
		showBotMessage(data['data'], d)
		url_google(data['google_url'], d)
	}, 2000)

};

function showBotMessage(msg,d){
	var options = {month: 'short', day: 'numeric', hour:'numeric', minute: 'numeric'  };
	//console.log("in showBotMessage");
	message = new Message({
				text: msg,
				time: d.toLocaleString("en-IN", options),
				message_side: 'left'
	});
	message.draw();
	$messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
};


$('#input_message').on("submit", function (event) {
	$.ajax({
		data: {
			query: $("#msg_input").val()
		},
		type: 'POST',
		url:'/process',
	})
	.done(function(data){
		console.log(data)
		main(document.getElementById("msg_input").value, getCurrentTimestamp(), data);

	});
	
	event.preventDefault();
});