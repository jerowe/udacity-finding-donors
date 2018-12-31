import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';
import {environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FindingDonorsService {

  // This worked before. I don't know why it doesn't work now
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      // 'Access-Control-Allow-Origin': '*',
      // 'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token, Access-Control-Allow-Origin',
      // 'Access-Control-Allow-Methods': [
      //   'Access-Control-Allow-Headers,',
      //   'Access-Control-Request-Method,',
      //   'Access-Control-Request-Headers,',
      //   'HEAD, GET, POST, PUT, PATCH, DELETE'
      // ].join(''),
    })
  };

  constructor(private http: HttpClient) {
  }

  healthCheck(): Observable<any> {
    return this.http.post(`${environment.apiUrl}/health`, {'hello': 'world'}, this.httpOptions);
  }

  getData(): Observable<any> {
    return this.http.get(`${environment.apiUrl}/read-data`,
      this.httpOptions);
  }

  getStats(): Observable<any> {
    return this.http.get(`${environment.apiUrl}/get-stats`,
      this.httpOptions);
  }

  // getTree(params: { max_depth }): Observable<any> {
  //   return this.http.post(`${environment.apiUrl}/model-learning`,
  //     params, this.httpOptions);
  // }
  //
  // modelComplexity(): Observable<any> {
  //   return this.http.post(`${environment.apiUrl}/model-complexity`,
  //     {}, this.httpOptions);
  //
  // }
}
