console.log("Loading search...");
var searchBox = document.createElement("div");
searchBox.id = "searchBox";
document.body.prepend(searchBox);
searchBox.style.display = "none";
var otherElements = document.getElementById("main-container");

document.addEventListener("keydown", (event) => {
	if (event.ctrlKey && event.key === "o"){
		event.preventDefault();
		console.log("Initializing search");
		loadSearch();
	}
	if (event.key === "Escape"){
		closeSearchBox();
	}
	});

async function loadSearch()
{
	if(searchBox.style.display === "none")
	{
		var inputField = document.createElement("input");
		var resultsField = document.createElement("div");
		otherElements.style.filter = "blur(4px)";
		searchBox.style.display = "flex";

		const data = await fetchJSON('/index.json');
		searchBox.appendChild(inputField);
		searchBox.appendChild(resultsField);
		inputField.focus();
		document.addEventListener("click", (event) => {
			let i = 0;
			for(; i<event.path.length; i++)
			{
				if(event.path[i].id === "searchBox"){
					break;
				}
			}
			if (i === event.path.length){
				closeSearchBox();
			}
		})
		inputField.addEventListener('input', function()
		{
			resultsField.innerHTML = "";
			var text = inputField.value;
			if(text !== ""){
				var filteredData = data.filter(item => {
					return (
						item.title.toLowerCase().includes(text.toLowerCase())
					)
				});
				for(let i=0; i < filteredData.length && i < 10; i++){
					itemHTML = "<a href=\"" + filteredData[i].link + "\">" + filteredData[i].title + "</a>";
					resultsField.innerHTML += itemHTML; 	
				}
				// SELECT BY ARROWS TODO
				// var x = 0;
				// document.addEventListener("keydown", (event) =>{
				// 	console.log(event.which);
				// 	if (event.which === "40"){
				// 		x += 1;
				// 	}
				// 	resultsField.children[x].focus();
				// })
			}
		});

	}
	else
	{
		closeSearchBox();
	}
}

function closeSearchBox() {
	otherElements.style.filter = "none";
	searchBox.innerHTML = "";
	searchBox.style.display = "none";
}

async function fetchJSON(url) {
	const response = await fetch(url);
	const data = await response.json();
	return data;
}