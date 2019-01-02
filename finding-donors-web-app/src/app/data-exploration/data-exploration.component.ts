import {Component, OnInit, ViewChild, ElementRef} from '@angular/core';
import {FindingDonorsService} from '../services/finding-donors.service';
import {capitalize} from 'lodash';
import * as d3 from 'd3';

import 'ag-grid-community';

@Component({
  // selector: 'app-data-exploration',
  templateUrl: './data-exploration.component.html',
  styleUrls: ['./data-exploration.component.css']
})
export class DataExplorationComponent implements OnInit {

  public fetchDataError = null;
  public columnDefs: Array<{ headerName, field }> = [];
  public rowData: Array<any> = null;

  private gridApi;
  private gridColumnApi;
  @ViewChild('correlationChart') chartElement: ElementRef;

  constructor(private findingDonorsService: FindingDonorsService) {
    this.getData();
  }

  ngOnInit() {
  }

  getData() {
    this.fetchDataError = null;
    this.findingDonorsService.getData()
      .subscribe((results) => {
        this.rowData = results;
        this.createColumnDefs();
      }, (error) => {
        this.fetchDataError = error;
      });
  }

  onGridReady(params) {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;
  }

  createColumnDefs() {
    const firstRow = this.rowData[0];
    this.columnDefs = [];
    Object.keys(firstRow).map((key) => {
      this.columnDefs.push({headerName: capitalize(key), field: key});
    });
  }

}
