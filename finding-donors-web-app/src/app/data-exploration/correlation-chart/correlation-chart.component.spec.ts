import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CorrelationChartComponent } from './correlation-chart.component';

describe('CorrelationChartComponent', () => {
  let component: CorrelationChartComponent;
  let fixture: ComponentFixture<CorrelationChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CorrelationChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CorrelationChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
