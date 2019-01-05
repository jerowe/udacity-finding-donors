import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IncomeBarChartRouteComponent } from './income-bar-chart-route.component';

describe('IncomeBarChartRouteComponent', () => {
  let component: IncomeBarChartRouteComponent;
  let fixture: ComponentFixture<IncomeBarChartRouteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IncomeBarChartRouteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IncomeBarChartRouteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
