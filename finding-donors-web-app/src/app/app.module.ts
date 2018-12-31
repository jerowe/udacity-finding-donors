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

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    DataExplorationComponent
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
