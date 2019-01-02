import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CorrelationChartRouteComponent } from './correlation-chart-route.component';

describe('CorrelationChartRouteComponent', () => {
  let component: CorrelationChartRouteComponent;
  let fixture: ComponentFixture<CorrelationChartRouteComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CorrelationChartRouteComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CorrelationChartRouteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
