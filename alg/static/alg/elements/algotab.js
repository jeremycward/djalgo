var colorScheme = {
    "waiting": "#F0F0F0",
    "warn": "#FF6600",
    "error": "#FF0000",
    "success": "#6DC13A"
};

(function () {
    'use strict';
    customElements.define('algo-phase', class extends HTMLElement {
        constructor() {
            super();
            var phaseTemplate = document.querySelector("#batchRunPhaseTemplate");
            this.phaseClone = document.importNode(phaseTemplate.content, true);
            var phaseCaption = this.attributes['caption'].value;
            this.phaseClone.querySelector("#batchPhaseCaption").appendChild(document.createTextNode(phaseCaption));
            var pieData = [];
            this.querySelectorAll("summary slice").forEach(function (thisSlice) {
                pieData.push({
                    value: thisSlice.attributes['value'].value,
                    status: thisSlice.attributes['status'].value
                })
            })

            var pieElement = this.phaseClone.querySelector("#phasePie");
            if (this.attributes['active']) {
                pieElement.classList.add("blinking")
            }

            drawPie(d3.select(pieElement), pieData);
            this.appendChild(this.phaseClone)

        }
        connectedCallback(){
            this.boundEventListner = this._onTitleClick.bind(this)
            let listener = this.boundEventListner
            this.querySelectorAll(".btn").forEach(function (thisBtn) {
                    thisBtn.addEventListener("click", listener)
                }
            )
            let accordionButton = this.querySelector(".btn")
            accordionButton.id =  this.attributes.controllerId.value
            accordionButton.setAttribute("data-toggle", "collapse")
            accordionButton.setAttribute("aria-expanded", "false")
            let dataTargetId = this.attributes.detailsId.value;
            accordionButton.setAttribute("data-target", dataTargetId);
            accordionButton.setAttribute("aria-controls",dataTargetId);

        }
        _onTitleClick(event) {

        }

    });
    customElements.define('algo-header', class extends HTMLElement {
        constructor() {
            super();
            var template = document.querySelector("#batchRunPhaseHeaderTemplate");
            var templateClone = document.importNode(template.content, true);


            let eventselement = this.querySelector("lifecycleEvents");
            let shadowTable = templateClone.querySelector("table")
            eventselement.querySelectorAll("event").forEach(function (thisEvent) {
                let rowElement = document.createElement("tr")
                let typeCell = rowElement.appendChild(document.createElement("td"))
                typeCell.appendChild(document.createTextNode(thisEvent.attributes['type'].value))
                let timestampCell = rowElement.appendChild(document.createElement("td"))
                timestampCell.appendChild(document.createTextNode(thisEvent.attributes['timestamp'].value))
                shadowTable.appendChild(rowElement)

            });
            let headerCaption = this.attributes.caption.value
            templateClone.querySelector("#batchReportCaption").appendChild(document.createTextNode(headerCaption));
            this.appendChild(templateClone)
        }
    });



})();

function drawPie(pieElement, data) {
    const width = 60,
        radius = width / 2;

    const arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(radius - 30);

    const pie = d3.pie()
        .sort(null)
        .value(function (d) {
            return d.value;
        });

    const svg = pieElement.append("svg")
        .attr("width", width)
        .attr("height", width)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + width / 2 + ")");

    const g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
        .attr("class", "arc")
        .attr("opacity", 1.0);

    g.append("path")
        .attr("d", arc)
        .style("fill", function (d) {
            return colorScheme[d.data.status]
        });
}

