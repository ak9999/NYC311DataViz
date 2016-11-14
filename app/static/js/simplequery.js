var myreq = new Request('http://localhost:5000/bees');

var bees = fetch(myreq)
	.then(function(response) {
		if(response.status == 200) return response.json();
		else throw new Error('Response is NOT OK');
	})
	.catch(function(error) {
		console.error(error);
	});

for (var i = 0; i < bees.length; i++) {
	console.log(bees[i]);
}