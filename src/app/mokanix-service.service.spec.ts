import { TestBed, inject } from '@angular/core/testing';

import { MokanixServiceService } from './mokanix-service.service';

describe('MokamixServiceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MokanixServiceService]
    });
  });

  it('should be created', inject([MokanixServiceService], (service: MokanixServiceService) => {
    expect(service).toBeTruthy();
  }));
});
