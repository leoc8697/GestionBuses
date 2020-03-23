//Usando fetch, hacemos la solicitud para leer el json

fetch('consultaLastStop').then(function(response) { return response.json();
})
.then(function(myJson){ 
	
	console.log(myJson);

	let res = document.querySelector('#res');
	res.innerHTML = '';
		
	for(let item of myJson){
			
	res.innerHTML += `
		<tr>
		  <th>${item.beaconMAC}</th>
		  <th>${item.hourDetection}</th>
		  <th>${item.dayDetection}</th>
		  <th>${item.monthDetection}</th>
		  <th>${item.yearDetection}</th>
		</tr>
			`
}});
