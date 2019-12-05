var svg = d3.select("#world")

d3.json("/data", function(data) {
    console.log(data);
    svg.selectAll()
	   .append("rect")
})
