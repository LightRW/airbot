import { Component, OnInit, OnDestroy } from '@angular/core';
import { MokanixServiceService } from './mokanix-service.service';
import { Observable } from 'rxjs/Observable';
import { IntervalObservable } from 'rxjs/observable/IntervalObservable';
import {MatToolbarModule} from '@angular/material/toolbar';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'AirBot Tracker';
  zoom = 14;
  lat: number;
  lng: number;
  locationData: any;
  private alive: boolean;

  constructor(private mokanixService: MokanixServiceService) {
    this.alive = true;
  }

  ngOnInit() {
    this.mokanixService.getLocation()
      .subscribe((res) => {
          this.locationData = res;
          this.lat = res['location']['lat'];
          this.lng = res['location']['lng'];
          console.log(this.locationData);
      });
        // get our data every subsequent 10 seconds
        IntervalObservable.create(10000)
        .subscribe(() => {
          this.mokanixService.getLocation()
            .subscribe(res => {
              this.locationData = res;
              this.lat = res['location']['lat'];
              this.lng = res['location']['lng'];
              console.log(this.locationData);
            });
        });
      }

      ngOnDestroy() {
      this.alive = false; // switches your IntervalObservable off
      }
}
