import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ApplicationRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AgmCoreModule } from '@agm/core';
import { MokanixServiceService } from './mokanix-service.service';
import { HttpModule } from '@angular/http';

import {MatDividerModule, MatListModule, MatToolbarModule} from '@angular/material';
import { AppComponent } from './app.component';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    FormsModule,
    HttpModule,
    MatToolbarModule,
    MatDividerModule,
    MatListModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyAboLHXpZ-1XHCtelvgaIohTRtUEYmUMpI'
    })
  ],
  providers: [MokanixServiceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
