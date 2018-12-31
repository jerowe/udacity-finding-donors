import { TestBed } from '@angular/core/testing';

import { FindingDonorsService } from './finding-donors.service';

describe('FindingDonorsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: FindingDonorsService = TestBed.get(FindingDonorsService);
    expect(service).toBeTruthy();
  });
});
