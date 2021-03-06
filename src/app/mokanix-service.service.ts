import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';


@Injectable()
export class MokanixServiceService {

  constructor(private http: Http) { }
  private queryLocationApi = '/v1/assets/8944501101188633300/location';



  getLocation() {
    const headers = new Headers({
      'Content-Type': 'application/json',
      'X-API-Key' : 't-e5b6e668-4612-477d-ab71-8be0c672b7d2'
    });
    const options = new RequestOptions({ headers: headers }); // Create a request option

    return this.http.get(this.queryLocationApi, options)
                    .map((res: Response) => res.json());
  }

}
