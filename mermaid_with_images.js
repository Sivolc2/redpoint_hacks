var mermaidAPI = mermaid.mermaidAPI;

mermaidAPI.initialize({
  startOnLoad: false
});

function renderMermaid(elementId, graphDefinition) {
    var element = document.getElementById(elementId);
    var insertSvg = function(svgCode, bindFunctions) {
        element.innerHTML = svgCode;
    };

    var graph = mermaidAPI.render("mermaid", graphDefinition, insertSvg);
}
