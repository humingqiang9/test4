import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface DataServiceResponse {
  id: number;
  name: string;
  description: string;
}

@Injectable({
  providedIn: 'root'
})
export class RandomHttpService {
  private apiUrl = 'https://jsonplaceholder.typicode.com/users';

  constructor(private http: HttpClient) { }

  getData(): Observable<DataServiceResponse[]> {
    return this.http.get<DataServiceResponse[]>(this.apiUrl);
  }

  getDataById(id: number): Observable<DataServiceResponse> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.get<DataServiceResponse>(url);
  }
}