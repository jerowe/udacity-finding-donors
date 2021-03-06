import {NgModule} from '@angular/core';
import {Routes, RouterModule, ExtraOptions} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {DataExplorationComponent} from './data-exploration/data-exploration.component';
import {ModelExplorationComponent} from './model-exploration/model-exploration.component';

export const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {
    path: 'home',
    component: HomeComponent,
  },
  {
    path: 'model-exploration',
    component: ModelExplorationComponent,
  },
  {
    path: 'data-exploration',
    component: DataExplorationComponent,
  },
];

const config: ExtraOptions = {
  enableTracing: false,
  useHash: true,
};

@NgModule({
  imports: [RouterModule.forRoot(routes, config)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
