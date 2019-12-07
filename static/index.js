var svg = d3.select("#world");
var width = parseInt(svg.style("width"));
var height = parseInt(svg.style("height"));

// Scales ---------------------------------------
var x = d3.scaleLinear()
  .range([ 0, width ])
  .domain([ -180, 180]);

var y = d3.scaleLinear()
    .range([ 0, height ])
    .domain([ 84, -80 ]);

var color = d3.scaleLinear()
    .range( ['#a3be8c', '#a3be8c', '#b48ead'] )
    .domain( [0, 100] );

var alpha = d3.scaleLinear()
    .range( [0, 1, 1] )
    .domain( [0, 100] );

svg.classed("svg-content-responsive", true);

d3.json("/data", function(data) {
    console.log(data);
    svg.selectAll()
	   .data(data.points)
	   .enter()
	   .append("rect")
	   .attr("class", "point")
	   .attr("x", function(d) { return x(d.x) })
	   .attr("y", function(d) { return y(d.y) })
	   .attr("width", "8")
	   .attr("height", "8")
	   .attr("fill", function(d) { return color(d.power) })
	   .attr("fill-opacity", function(d) { return alpha(d.power) })
	   .on("mouseover", handleMouseOver)
	   .on("mouseout", handleMouseOut);
});

// Functions ------------------------------------
function handleMouseOver(d, i) {
    d3.select(this)
	   .transition()
	   .duration(200)
	   .attr("width", "30")
	   .attr("height", "30")
	   .attr("x", function(d) { return x(d.x) - 15 })
	   .attr("y", function(d) { return y(d.y) - 15 });

    svg.append("text")
	   .attr("class", "power-value")
	   .attr("id", "point-" + i)
	   .attr("x", function() { return x(d.x) - 15})
	   .attr("y", function() { 
		  if (y(d.y) < 50) { return y(d.y) + 50 }
		  else { return y(d.y) - 20 }
	   })
	   .text(function() {
              return d.power + "%";
	   });
}

function handleMouseOut(d, i) {
    d3.select(this)
	   .transition()
	   .duration(200)
	   .attr("width", "7")
	   .attr("height", "7")
	   .attr("x", function(d) { return x(d.x) })
	   .attr("y", function(d) { return y(d.y) });

    d3.select("#point-" + i).remove();
}
