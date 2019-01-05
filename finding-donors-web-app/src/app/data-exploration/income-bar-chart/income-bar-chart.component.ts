import {Component, OnInit, ViewChild, ElementRef, Input} from '@angular/core';
import * as d3 from 'd3';
import {minBy, maxBy, indexOf, orderBy} from 'lodash';
import {FindingDonorsService} from '../../services/finding-donors.service';

// @ts-ignore
@Component({
  selector: 'app-income-bar-chart',
  templateUrl: './income-bar-chart.component.html',
  styleUrls: ['./income-bar-chart.component.css']
})
export class IncomeBarChartComponent implements OnInit {

  public frequenciesByIncomeData: Array<{ category, name, value, lvalue }> = null;
  public frequenciesByIncomeError: any = null;
  public chartProps: { x, y } = {x: null, y: null};
  @Input('frequencyKey') frequencyKey: string;
  @ViewChild('lchart') lchartElement: ElementRef;
  @ViewChild('gchart') gchartElement: ElementRef;

  constructor(private findingDonorsService: FindingDonorsService) {
    this.getFrequenciesByIncomeData();
  }

  ngOnInit() {
  }

  getFrequenciesByIncomeData() {
    this.frequenciesByIncomeError = null;
    this.frequenciesByIncomeData = null;
    this.findingDonorsService.getFrequenciesByIncome()
      .subscribe((results) => {
        let gData = [];
        const g = results[this.frequencyKey]['g'];
        const l = results[this.frequencyKey]['l'];
        Object.keys(g).map((innerKey) => {
          const gPerc = Number(g[innerKey]) / (Number(g[innerKey]) + Number(l[innerKey]));
          const lPerc = Number(l[innerKey]) / (Number(g[innerKey]) + Number(l[innerKey]));
          gData.push({category: this.frequencyKey, name: innerKey, value: +gPerc, lvalue: +lPerc});
        });
        gData = orderBy(gData, 'value');
        this.frequenciesByIncomeData = gData;
        this.buildBarChart(this.gchartElement, 'blue', 'value');
        this.buildBarChart(this.lchartElement, 'grey', 'lvalue');
      }, (error) => {
        this.frequenciesByIncomeError = error;

      });
  }

  buildBarChart(chartElement: ElementRef, color: string, key: string) {
    // TODO Figure out how to make this responsive!!!
    const margin = {top: 30, right: 20, bottom: 80, left: 20},
      width = 600 - margin.left - margin.right,
      height = 600 - margin.top - margin.bottom;

    // Set the ranges
    this.chartProps.x = d3.scaleLinear().range([0, width]);
    this.chartProps.y = d3.scaleLinear().range([height, 0]);

    const _this = this;

    const x = d3.scaleBand()
      .domain(this.frequenciesByIncomeData.map(d => d.name))
      .range([margin.left, width - margin.right])
      .padding(0.2);
    const maxG = maxBy(this.frequenciesByIncomeData, 'value')['value'];
    const maxL = maxBy(this.frequenciesByIncomeData, 'lvalue')['lvalue'];
    const max = Math.max(maxG, maxL);

    const y = d3.scaleLinear()
    // .domain([0, d3.max(this.frequenciesByIncomeData, d => d.value)])
      .domain([0, max])
      .nice()
      .range([height - margin.bottom, margin.top]);

    // TODO Get text to display vertically
    const xAxis = g => g
      .attr('transform', `translate(0,${height - margin.bottom})`)
      // .attr('transform', 'rotate(90)')
      .call(d3.axisBottom(x)
        .tickSizeOuter(0));

    const yAxis = g => g
      .attr('transform', `translate(${margin.left},0)`)
      .call(d3.axisLeft(y))
      .call(g => g.select('.domain').remove());

    // Set the initial chart
    const svg = d3.select(chartElement.nativeElement)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    svg.append('g')
      .attr('fill', color)
      .selectAll('rect')
      .data(this.frequenciesByIncomeData)
      .enter().append('rect')
      .attr('x', d => x(d.name))
      .attr('y', d => y(d[key]))
      .attr('height', d => y(0) - y(d[key]))
      .attr('width', x.bandwidth());

    svg.append('g')
      .call(xAxis)
      .selectAll('text')
      .attr('y', 0)
      .attr('x', 9)
      .attr('dy', '.35em')
      .attr('transform', 'rotate(90)')
      .style('text-anchor', 'start');

    svg.append('g')
      .call(yAxis);
  }

}
