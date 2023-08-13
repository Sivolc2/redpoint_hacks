var mermaidAPI = mermaid.mermaidAPI;

mermaidAPI.initialize({
  startOnLoad:false
});

var element = document.getElementById("app");
var insertSvg = function(svgCode, bindFunctions) {
  element.innerHTML = svgCode;
};
var graphDefinition = `graph LR; Nodetext-->SomeIcon(<img src='https://store.nytimes.com/cdn/shop/products/notebook-chambray_1024x1024.jpg?v=1571439076' width='40' height='40' />)`;
var graphDefinition2
var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);

