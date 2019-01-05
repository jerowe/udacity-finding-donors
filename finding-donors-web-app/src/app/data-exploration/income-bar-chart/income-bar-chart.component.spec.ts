import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IncomeBarChartComponent } from './income-bar-chart.component';

describe('IncomeBarChartComponent', () => {
  let component: IncomeBarChartComponent;
  let fixture: ComponentFixture<IncomeBarChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IncomeBarChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IncomeBarChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
