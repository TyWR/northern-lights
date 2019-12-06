var svg = d3.select("#world");
var width = parseInt(svg.style("width"));
var height = parseInt(svg.style("height"));

var x = d3.scaleLinear()
  .range([ 0, width ])
  .domain([ -180, 180 ]);

var y = d3.scaleLinear()
    .range([ 0, height ])
    .domain([ -90, 90 ]);

var color = d3.scaleLinear()
    .range( ['#a3be8c', '#a3be8c', '#b48ead'] )
    .domain( [0, 100] );

var alpha = d3.scaleLinear()
    .range( [0, 1, 1] )
    .domain( [0, 100] );

d3.json("/data", function(data) {
    console.log(data);
    svg.selectAll()
	   .data(data.points)
	   .enter()
	   .append("rect")
	   .attr("x", function(d) { return x(d.longitude) })
	   .attr("y", function(d) { return y(d.latitude) })
	   .attr("width", "7")
	   .attr("height", "7")
	   .attr("fill", function(d) { return color(d.power) })
	   .attr("fill-opacity", function(d) { return alpha(d.power) });
})
