import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AppRoutingModule} from './app.routing';
import {FormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';


// Core UI Stuff
import {
  AppAsideModule,
  AppBreadcrumbModule,
  AppHeaderModule,
  AppFooterModule,
  AppSidebarModule,
} from '@coreui/angular';

import {PerfectScrollbarModule} from 'ngx-perfect-scrollbar';
import {PERFECT_SCROLLBAR_CONFIG} from 'ngx-perfect-scrollbar';
import {PerfectScrollbarConfigInterface} from 'ngx-perfect-scrollbar';

const DEFAULT_PERFECT_SCROLLBAR_CONFIG: PerfectScrollbarConfigInterface = {
  suppressScrollX: true
};

// Ag Grid - Data tables
import {AgGridModule} from 'ag-grid-angular';

// Components
import {AppComponent} from './app.component';
import {HomeComponent} from './home/home.component';
import {DataExplorationComponent} from './data-exploration/data-exploration.component';
import { CorrelationChartComponent } from './data-exploration/correlation-chart/correlation-chart.component';
import { IncomeBarChartComponent } from './data-exploration/income-bar-chart/income-bar-chart.component';
import { IncomeBarChartRouteComponent } from './data-exploration/income-bar-chart-route/income-bar-chart-route.component';
import { CorrelationChartRouteComponent } from './data-exploration/correlation-chart-route/correlation-chart-route.component';
import { ModelExplorationComponent } from './model-exploration/model-exploration.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DataExplorationComponent,
    CorrelationChartComponent,
    IncomeBarChartComponent,
    IncomeBarChartRouteComponent,
    CorrelationChartRouteComponent,
    ModelExplorationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    PerfectScrollbarModule,
    AgGridModule.withComponents([]),
    AppFooterModule,
    AppHeaderModule,
    AppSidebarModule,
    AppAsideModule,
    AppBreadcrumbModule.forRoot(),
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
