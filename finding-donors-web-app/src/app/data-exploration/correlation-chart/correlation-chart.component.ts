import {Component, OnInit, ViewChild, ElementRef} from '@angular/core';
import * as d3 from 'd3';
import {minBy, maxBy, indexOf, round} from 'lodash';
import {FindingDonorsService} from '../../services/finding-donors.service';

@Component({
  selector: 'app-correlation-chart',
  templateUrl: './correlation-chart.component.html',
  styleUrls: ['./correlation-chart.component.css']
})
export class CorrelationChartComponent implements OnInit {

  public correlationData: Array<any> = null;
  public fetchCorrelationDataError: any = null;
  public correlationDataLabels: Array<string> = [];
  public chartProps: { x, y } = {x: null, y: null};
  @ViewChild('chart') chartElement: ElementRef;

  constructor(private findingDonorsService: FindingDonorsService) {
    this.getCorrelationData();
  }

  ngOnInit() {
  }

  getCorrelationData() {
    this.correlationData = null;
    this.findingDonorsService.getCorrelation()
      .subscribe((results) => {
        this.correlationData = [];
        Object.keys(results).map((topLevelKey) => {
          Object.keys(results[topLevelKey]).map((innerKey) => {
            const t = {v1: topLevelKey, v2: innerKey, corr: results[topLevelKey][innerKey]};
            this.correlationData.push(t);
          });
          this.correlationDataLabels.push(topLevelKey);
        });
        this.buildCorrelationDataChart();
      }, (error) => {
        this.fetchCorrelationDataError = error;
      });
  }

  buildCorrelationDataChart() {
    /**
     * Data looks like this:
     * {'age': {'age': correlation_value, 'income': 'correlation_value'}}
     */
    const margin = {top: 30, right: 20, bottom: 100, left: 100},
      width = 800 - margin.left - margin.right,
      height = 800 - margin.top - margin.bottom;

    // d3.interpolateInferno(t

    const itemSize = this.correlationDataLabels.length;
    const gridSize = Math.floor(width / this.correlationDataLabels.length);
    const legendElementWidth = gridSize * 2;

    const x_elements = d3.set(this.correlationData.map(function (item) {
        return item.v1;
      })).values(),
      y_elements = d3.set(this.correlationData.map(function (item) {
        return item.v2;
      })).values();

    const xScale = d3.scaleOrdinal()
      .domain(x_elements)
      .range([0, x_elements.length * itemSize]);

    const yScale = d3.scaleOrdinal()
      .domain(y_elements)
      .range([0, y_elements.length * itemSize]);

    // Set the ranges
    const x = d3.scaleLinear().range([0, width]);
    const y = d3.scaleLinear().range([height, 0]);
    this.chartProps.x = x;
    this.chartProps.y = y;

    const colorScale = d3.scaleLinear()
      .range([0, 1])
      .domain([minBy(this.correlationData, 'corr')['corr'], maxBy(this.correlationData, 'corr')['corr']]);

    // d3.schemeRdYlBu

    // Have this around so we can access inside the chart
    const _this = this;

    // Set the initial chart
    const svg = d3.select(this.chartElement.nativeElement)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    svg.selectAll('.leftLabels')
      .data(_this.correlationDataLabels)
      .enter().append('text')
      .text((d) => d)
      .attr('x', 0)
      .attr('y', function (d, i) {
        return i * gridSize;
      })
      .style('text-anchor', 'middle')
      .attr('transform', 'translate(-6,' + gridSize / 1.5 + ')')
      .attr('class', 'leftLabel');

    svg.selectAll('.timeLabel')
      .data(this.correlationDataLabels)
      .enter().append('text')
      .text((d) => d)
      .attr('x', function (d, i) {
        return i * gridSize;
      })
      .attr('y', 0)
      .style('text-anchor', 'middle')
      .attr('transform', 'translate(' + gridSize / 2 + ', -6)')
      .attr('class', 'bottomLabel');

    // Start filling in the heatmap

    const cards = svg.selectAll('.corr')
      .data(this.correlationData, function (d) {
        return d.v1 + ':' + d.v2;
      });

    cards.append('title');

    cards
      .enter().append('rect')
      .attr('x', function (d, i) {
        const index = indexOf(_this.correlationDataLabels, d.v1) * gridSize;
        return index;
      })
      .attr('y', function (d, i) {
        const index = indexOf(_this.correlationDataLabels, d.v2) * gridSize;
        return index;
      })
      .attr('rx', 4)
      .attr('ry', 4)
      .attr('class', 'hour bordered')
      .attr('width', gridSize)
      .attr('height', gridSize)
      .style('fill', function (d) {
        // d3.schemeRdYlBu
        let color: any;
        if (d.corr > 0) {
          color = d3.interpolateBlues(colorScale(d.corr));
        } else {
          color = d3.interpolateReds(colorScale(d.corr));
        }
        return color;
      });

    cards.enter().append('text')
      .attr('x', function (d, i) {
        const index = indexOf(_this.correlationDataLabels, d.v1) * gridSize;
        return index + (gridSize / 2);
      })
      .attr('y', function (d, i) {
        const index = indexOf(_this.correlationDataLabels, d.v2) * gridSize;
        return index + (gridSize / 2);
      })
      .text((d) => round(d.corr, 2));


    cards.select('title').text(function (d) {
      return d.value;
    });

    cards.exit().remove();

  }

}
