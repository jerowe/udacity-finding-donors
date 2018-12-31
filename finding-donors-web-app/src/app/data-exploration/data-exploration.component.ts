import {Component, OnInit} from '@angular/core';
import {FindingDonorsService} from '../services/finding-donors.service';
import {capitalize} from 'lodash';

import 'ag-grid-community';

@Component({
  // selector: 'app-data-exploration',
  templateUrl: './data-exploration.component.html',
  styleUrls: ['./data-exploration.component.css']
})
export class DataExplorationComponent implements OnInit {

  public fetchDataError = null;
  // public columnDefs: Array<{ headerName, field }> = [];
  // public rowData: Array<any> = null;

  private gridApi;
  private gridColumnApi;

  columnDefs = [
    {headerName: 'Make', field: 'make' },
    {headerName: 'Model', field: 'model' },
    {headerName: 'Price', field: 'price'}
  ];

  rowData = [
    { make: 'Toyota', model: 'Celica', price: 35000 },
    { make: 'Ford', model: 'Mondeo', price: 32000 },
    { make: 'Porsche', model: 'Boxter', price: 72000 }
  ];

  constructor(private findingDonorsService: FindingDonorsService) {
    // this.getData();
  }

  ngOnInit() {
  }

  getData() {
    this.fetchDataError = null;
    this.findingDonorsService.getData()
      .subscribe((results) => {
        // this.rowData = results;
        this.rowData = results.slice(0, 10);
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
    console.log(this.columnDefs);
  }

}
