const dining = document.querySelector("#dining")
const content = document.querySelector("#content")

dining.addEventListener("mouseover", function(){
content.classList.remove("show")
dining.addEventListener("mouseout", function(){
content.classList.add("show")

});

});
