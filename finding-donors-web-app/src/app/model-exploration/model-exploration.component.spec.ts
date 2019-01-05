import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ModelExplorationComponent } from './model-exploration.component';

describe('ModelExplorationComponent', () => {
  let component: ModelExplorationComponent;
  let fixture: ComponentFixture<ModelExplorationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ModelExplorationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ModelExplorationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
