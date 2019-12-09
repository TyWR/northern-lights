var svg = d3.select("#world");
var width = parseInt(svg.style("width"));
var height = parseInt(svg.style("height"));
var h = height/233;		// Cube size
var w = width/512;
var zoom = 2;				// Cube size when zoomed

// Scales ---------------------------------------
var x = d3.scaleLinear()
  .range([ 0, width ])
  .domain([ -180, 180]);

var y = d3.scaleLinear()
    .range([ 0, height ])
    .domain([ 84, -80 ]);

var color = d3.scaleLinear()
    .range( ['#a3be8c', '#a3be8c', '#b48ead'] )
    .domain( [0, 50, 100] );

var alpha = d3.scaleLinear()
    .range( [0, 1, 1] )
    .domain( [0, 50, 100] );

svg.classed("svg-content-responsive", true);


// Legend ---------------------------------------
var legend_data = [...Array(11).keys()].map((d) => 10*d);
var legend_len = 15;
var pad = 5;
svg.selectAll()
    .data(legend_data)
    .enter()
    .append("rect")
    .attr("class", "legend")
    .attr("x", function(d, i) { return width/40 })
    .attr("y", function(d, i) { 
	   return height/2 + (i - 5) * (legend_len + pad) 
    })
    .attr("width", legend_len)
    .attr("height", legend_len)
    .attr("fill", function(d) { return color(d) })
    .attr("fill-opacity", function(d) { return alpha(d) });

svg.append("text")
    .attr("class", "legend-text")
    .attr("x", width/40)
    .attr("y", height/2 - 5*(legend_len + pad) + 10)
    .text("HIGH");
    

svg.append("text")
    .attr("class", "legend-text")
    .attr("x", width/40)
    .attr("y", height/2 + 6*(legend_len + pad) + 15)
    .text("LOW");

// Main data ------------------------------------
d3.json("/data", function(data) {
    svg.selectAll()
	   .data(data.points)
	   .enter()
	   .append("rect")
	   .attr("class", "point")
	   .attr("x", function(d) { return x(d.x) - w/2 })
	   .attr("y", function(d) { return y(d.y) - h/2 })
	   .attr("width", w)
	   .attr("height", h)
	   .attr("fill", function(d) { return color(d.power) })
	   .attr("fill-opacity", function(d) { return alpha(d.power) })
	   .on("mouseover", handleMouseOver)
	   .on("mouseout", handleMouseOut);
});

// Functions ------------------------------------
function handleMouseOver(d, i) {
    d3.select(this)
	   .attr("width", w*zoom)
	   .attr("height", h*zoom)
	   .attr("x", function(d) { return x(d.x) - (w*zoom)/2 })
	   .attr("y", function(d) { return y(d.y) - (h*zoom)/2 });

    svg.append("text")
	   .attr("class", "power-value")
	   .attr("id", "point-" + i)
	   .attr("x", function() { 
		  if (x(d.x) > w*zoom/2) { return x(d.x) - w*zoom/2 }
		  else { return x(d.x) }
	   })
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
	   .attr("width", w)
	   .attr("height", h)
	   .attr("x", function(d) { return x(d.x) - w/2 })
	   .attr("y", function(d) { return y(d.y) - h/2 });

    d3.select("#point-" + i).remove();
}


