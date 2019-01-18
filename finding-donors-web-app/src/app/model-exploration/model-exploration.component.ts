import {Component, OnInit} from '@angular/core';
import {FindingDonorsService} from '../services/finding-donors.service';
import {isEqual, get, find} from 'lodash';
import {select} from 'd3-selection';
import 'ag-grid-community';

@Component({
  // selector: 'app-model-exploration',
  templateUrl: './model-exploration.component.html',
  styleUrls: ['./model-exploration.component.css']
})
export class ModelExplorationComponent implements OnInit {

  public potentialModels: Array<string> = ['SVC', 'KNeighborsClassifier', 'GaussianNB',
    'ADABoostClassifier', 'RandomForestClassifier', 'GradientBoostingClassifier'];
  public dataSize = 36178;
  // TODO Should have this as percentages
  public potentialSampleSizes: Array<number> = [100, 1000, 10000, 36178];
  public models: any = {};
  public sampleSizes: any = {};

  // Data we display in the table
// {
//   "acc_test": 0.8328358208955224,
//   "acc_train": 0.8380186306216657,
//   "f_test": 0.8231106945482053,
//   "f_train": 0.8287826467803742,
//   "fetched_from_cache": true,
//   "model": "SVC",
//   "pred_time": 115.20346212387085,
//   "sample_size": 36177,
//   "train_time": 160.48580646514893
// },
  public trainingData: Array<{ acc_test, acc_train, f_test, f_train, model, pred_time, sample_size, train_time, fetched_from_cache }> = [];
  public columnDefs: Array<{ headerName, field }> = [
    {
      headerName: 'AccTest', field: 'acc_test'
    },
    {
      headerName: 'AccTrain', field: 'acc_train'
    },
    {
      headerName: 'FTest', field: 'f_test',
    },
    {
      headerName: 'FTrain', field: 'f_train',
    },
    {
      headerName: 'Model', field: 'model',
    },
    {
      headerName: 'Pred Time', field: 'pred_time',
    },
    {
      headerName: 'Sample Size', field: 'sample_size'
    },
    {
      headerName: 'Train Time', field: 'train_time'
    }
  ];
  private gridApi;
  private gridColumnApi;

  constructor(private findingDonorsService: FindingDonorsService) {
  }

  ngOnInit() {
  }

  submitModelTraining() {
    const selectedSampleSizes = [];
    const modelParameters = [];

    Object.keys(this.sampleSizes).map((sampleSize) => {
      if (get(this.sampleSizes, sampleSize)) {
        selectedSampleSizes.push(sampleSize);
      }
    });

    Object.keys(this.models).map((model) => {
      if (get(this.models, model)) {
        if (selectedSampleSizes.length) {
          selectedSampleSizes.map((sampleSize) => {
            modelParameters.push({model_name: model, sample_size: Number(sampleSize)});
          });
        } else {
          modelParameters.push({model_name: model, sample_size: Number(this.dataSize)});
        }
      }
    });

    modelParameters.map((modelParams) => {
      this.getTrainingStats(modelParams);
    });
  }

  clearData() {
    this.gridApi.setRowData([]);
  }

  onAddRow(newItem: {}) {
    if (this.gridApi) {
      this.gridApi.updateRowData({add: [newItem]});
    }
  }

  getTrainingStats(params) {
    this.findingDonorsService
      .train(params)
      .subscribe((results) => {
        this.findRecord(results);
      }, (error) => {
        console.log(error);
      });
  }

  findRecord(newItem: any) {
    const t = find(this.trainingData, (data) => {
      return isEqual(data.sample_size, newItem.sample_size) && isEqual(data.model, newItem.model);
    });
    if (!t) {
      this.trainingData.push(newItem);
      this.onAddRow(newItem);
    }
  }

  onGridReady(params) {
    this.gridApi = params.api;
    this.gridColumnApi = params.columnApi;
  }

}
