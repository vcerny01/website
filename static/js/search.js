console.log("Loading search...");
var searchBox = document.createElement("div");
searchBox.id = "searchBox";
document.body.prepend(searchBox);
searchBox.style.display = "none";
var allContent = document.getElementById("main-container");
var otherElements = document.getElementById("main-content");
var data;
fetchJSON('/index.json').then(resp => {
	data = resp;
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
});

function loadSearch()
{
	if(searchBox.style.display === "none")
	{
		var inputField = document.createElement("input");
		var resultsField = document.createElement("div");
		resultsField.id = "resultsField";
		allContent.style.filter = "blur(4px)";
		searchBox.style.display = "flex";

		searchBox.appendChild(inputField);
		searchBox.appendChild(resultsField);
		inputField.focus();
		document.addEventListener("click", (event) => {
			let i = 0;
			let temp = false;
			for(; i<event.path.length; i++)
			{
				let id = event.path[i].id
				if(id === "searchBox" || id === "searchbtn"){
					temp = true;
					break;
				}
			}
			if (!temp){
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
					itemHTML = "<a class=\"result\" href=\"" + filteredData[i].link  + "\">" + "<span class=\"title\">" + filteredData[i].title + "</span><span class=\"path\">" + filteredData[i].path + "</span></a>";
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
	allContent.style.filter = "none";
	searchBox.innerHTML = "";
	searchBox.style.display = "none";
}
async function fetchJSON(url) {
	const response = await fetch(url);
	const data = await response.json();
	return data;
}