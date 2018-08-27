$('.range')[$('.range').length-1].value = 0
$('.number')[$('.number').length-1].value = 0

otherInput = document.createElement('textarea');
otherInput.placeholder = "Leave this blank and set this slider to 0, unless you can think of some other aspect you'd like to cover";
otherInput.resize = 'both';
otherInput.id = 'otherInput';
otherInput.name = 'other_text';
$('.section')[$('.section').length-1].append(otherInput);


var randomQuote = pd['quotes'][Math.floor(Math.random()*pd['quotes'].length)];
$('#comments').attr('placeholder', 'Confucius say: \n' + randomQuote);

var totNum = $('.range').toArray().length;

$('.range').each(function(i, item){
	this.oninput = function(){
		$(this).siblings('.number')[0].value = this.value;

		idx = $('.range').index(this);
		changeRanges();
	}
})

$('.number').each(function(i, item){
	this.oninput = function(){
		$(this).siblings('.range')[0].value = this.value;

		idx = $('.number').index(this);
		changeRanges();
	}
})

function changeRanges() {
	values = $('.range').toArray().map(a => parseInt($(a)[0].value))
	idx = nextNum(idx);
	while ( sum(values) !== 100 ) {
		delta = 100 - sum(values);
		values[idx] = constrain(values[idx] + delta, 0, 100);
		idx = nextNum(idx);
	}
	
	for (var i = 0; i < values.length; i++) {
		$('.range')[i].value = values[i];
		$('.number')[i].value = values[i];
	}
}

function sumRanges() {
	return $('.range').toArray().map(a => parseInt($(a)[0].value)).reduce((a, b) => a + b)
}

function nextNum(i) {
	if (i < totNum - 1) {
		return i + 1;
	} else if (i === totNum - 1) {
		return 0;
	} else {
		console.log('ERROR');
	}
}

function constrain(val, min, max) {
	var number = Math.min(Math.max(parseInt(val), min), max);
	return number
}

function between(val, min, max) {
	if (val >= min && val <= max) {
		return true;
	} else {
		return false;
	}
}

function sum(arr) {
	return arr.reduce((a, b) => a + b, 0);
}